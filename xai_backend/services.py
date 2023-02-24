import json
from django.http import HttpResponse
import pylast
import pandas as pd
import numpy as np
import json
import pylast
from shap.plots import heatmap
from bs4 import BeautifulSoup
import xgboost as xgb
import lime
import os
import shap
import matplotlib.pyplot as plt
import matplotlib.figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.transforms import Bbox
from lime import lime_tabular
from econml.dml import CausalForestDML, LinearDML, NonParamDML, KernelDML, SparseLinearDML, DML
from econml.sklearn_extensions.linear_model import StatsModelsLinearRegression


from xai_backend.serializer import SongSerializer
from xai_backend.models import Song, TopSong
from django.db.models import Count, F, Sum, Case, When, Max, FloatField
from django.db.models.functions import Cast
from django.views.decorators.csrf import csrf_exempt
from skcriteria.madm import simple
from skcriteria import Data

import matplotlib
matplotlib.use('SVG')

# return sampled list of songs
def sample_ranking(*args):
    songs = TopSong.objects.filter().order_by('?')[:10]
    song_list = SongSerializer(songs, many=True)
    data = song_list.data

    df = pd.DataFrame(list(songs.values()))

    df['name'] = df['song']
    df['rank'] = df['id'].rank()
    df['year'] = 2021
    

    return HttpResponse(json.dumps(df.sort_values(by=['rank']).to_dict(orient='records')))




# Receiving 2 Rankings from frontend
@csrf_exempt
def compare_rankings(request):
    if request.method == 'GET':
        data = request.GET
        data = data.dict()
        user_ranking = json.loads(data['user_ranking'])
        thrid_ranking = json.loads(data['third_ranking'])

        u = pd.DataFrame(user_ranking).set_index('id')
        t = pd.DataFrame(thrid_ranking).set_index('id')

        X = t.copy()
        X['user_rank'] = u[['rank']]
        X['change'] = X['rank'] - X['user_rank']

        cols = ['acousticness', 'danceability', 'energy',
        'instrumentalness', 'key', 'liveness',
       'loudness', 'popularity', 'rank',
       'speechiness', 'tempo', 'valence', 'user_rank', 'change']
        # generate IF and IE using model (default xgbrank)
        
        feature_importance, item_explanations = which_model(X[cols], 0)
        print(X[cols])

        # save a shap graph in root folder, it also tells how important a feature is to the ranking
        DML_(X[cols])

        html_str = bar_html(X[cols])

        res = {'feature_importance': feature_importance, 'item_explanations': item_explanations, 'html_str': html_str}
        return HttpResponse(json.dumps(res))


def which_model(X, model_num=0):
    if model_num == 0:
        return xgb_rank(X)


def xgb_rank(X):
    model = xgb.XGBRegressor(objective='rank:pairwise')

    id = X.index
    _ = X.pop('rank')
    _ = X.pop('change')
    y = X.pop('user_rank')

    # X=(X-X.mean())/X.std()
    # X=(X-X.min())/(X.max()-X.min())

    model = model.fit(X, y)
    print(model.feature_importances_)
    FI = dict(zip(X.columns, model.feature_importances_.tolist()))

    explainer = lime_tabular.LimeTabularExplainer(
    training_data=np.array(X),
    feature_names=X.columns,
    class_names=['down', 'up'],
    mode='regression'
    )

    Ex_item = {}

    for i, v in enumerate(id):
        exp = explainer.explain_instance(data_row=X.iloc[i], predict_fn=model.predict)
        Ex_item[v] = exp.as_list()

    return FI, Ex_item


def xgb_classifier(X):
    model = xgb.XGBClassifier()

    id = X.index
    _ = X.pop('rank')
    y = X.pop('change')
    _ = X.pop('user_rank')

    y = y.apply(lambda x: 0 if x < 0 else 1)

    model.fit(X, y)
    FI = dict(zip(X.columns, model.feature_importances_.tolist()))

    explainer = lime_tabular.LimeTabularExplainer(
        training_data=np.array(X),
        feature_names=X.columns,
        class_names=['down', 'up'],
        mode='classification'
    )

    Ex_item = {}

    for i, v in enumerate(id):
        exp = explainer.explain_instance(data_row=X.iloc[i], predict_fn=model.predict)
        Ex_item[v] = exp.as_list()

    return FI, Ex_item


def DML_(X, path='shap_graph.svg'):
    np.random.seed(100)
    _ = X.pop('rank')
    T = X.pop('change')
    y = X.pop('user_rank')

    # X=(X-X.mean())/X.std()
    # X=(X-X.min())/(X.max()-X.min())

    print(y, T, X)
    est = LinearDML()
    # est = CausalForestDML()

    est.fit(y, T, X=X, W=None)

    effect = est.effect(X)
    FI = dict(zip(X.columns, est.coef_))

    # generate importance heatmap
    ind=0
    shap_values = est.shap_values(X)
    # shap.plots.force(shap_values["rank_user"]["change"][ind], matplotlib=True)
    # shap.summary_plot(shap_values["rank_user"]["change"])
    shap.plots.heatmap(shap_values["user_rank"]["change"], show=False)
    ax = plt.gca()
    ax.set_xlabel('User Rank')
    # ax.set_ylabel('Change on items\' rank')
    # ax.set_yticklabels(['Change on Items\'s Rank'])
    yt = ax.get_yticklabels()
    yt[0] = 'Change on Items\'s Rank'
    xl = ax.get_xticklabels()
    ax.set_yticklabels(yt)
    ax.set_xticklabels([-2] + [i for i in range(1, 11, 2)])

    # canvas = FigureCanvasAgg(ax)
    # ax.canvas.draw()
    # renderer = ax._cachedRenderer
    # tightbox = ax.get_tightbbox(renderer)
    # w,h = ax.get_size_inches()
    # bbox = Bbox.from_extents(min(tightbox.x0,0), min(tightbox.y0,0),
    #                         max(tightbox.x1,w), max(tightbox.y1,h))

    # if os.path.exists(path):
    #     os.remove(path)

    plt.savefig(path, format='svg', dpi=1200, bbox_inches = 'tight')


def get_shap(*args):
    path = "shap_graph.svg"
    file_one = open(path, "rb")
    return HttpResponse(file_one.read(), content_type='image/png')

import plotly.graph_objs as go 
import plotly.offline as offline 
from plotly.offline import plot 
from sklearn.cluster import KMeans

def bar_html(X): 
    songs = TopSong.objects.all() 
    song_list = SongSerializer(songs, many=True) 
    data = song_list.data 
    df = pd.DataFrame(list(songs.values()))

    mask = ['acousticness', 'danceability', 'energy',
        'instrumentalness', 'key', 'liveness',
    'loudness', 'popularity',
    'speechiness', 'tempo', 'valence']
    kmeans = KMeans(n_clusters=5, random_state=20).fit(df[mask])
    cat = kmeans.predict(X[mask])

    X=(X-X.min())/(X.max()-X.min())
    _ = X.pop('rank')
    change = X.pop('change')
    user_rank = X.pop('user_rank')
    # colors = ['rgba(255, 174, 255, 0.5)', # red
    #  'rgba(255, 255, 128, 0.5)', # yellow
    #   'rgba(199, 174, 255, 0.5)', # green
    #   ]
    colors = ['rgba(255, 174, 255, 0.5)', 'rgba(255, 255, 128, 0.5)', 'rgba(128, 255, 200, 0.5)',
    'rgba(199, 174, 255, 0.5)', 'rgba(39, 140, 255, 0.5)', 'rgba(255, 122, 133, 0.5)', 'rgba(55, 174, 99, 0.5)',
    'rgba(140, 100, 255, 0.5)', 'rgba(80, 150, 74, 0.5)', 'rgba(255, 255, 255, 0.5)', 'rgba(255, 174, 0, 0.5)'
    ]

    res = []
    for rank in range(10):
        res.append(
            go.Bar(
                x=X.columns,
                y=X.iloc[rank],
                name=rank,
                marker = dict(color = colors[cat[rank]],
                                line=dict(color='rgb(0,0,0)',width=1.5)),
            )
        )

    layout = go.Layout(
        barmode='overlay'
    )
    fig = go.Figure(data=res, layout=layout)
    fig.write_html('bar.html', full_html=False)

    return fig.to_html(full_html=False)