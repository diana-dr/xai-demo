from copy import copy, deepcopy
import numpy as np
import pandas as pd
import json
from random import randint
from re import S
from unicodedata import name
from django.test import TestCase
from skcriteria.madm import simple
from skcriteria import Data
from django.db.models import Count, F, Sum, Case, When, Max, FloatField, Min



import os
import sys
import django
BDIR = os.path.abspath(os.path.join(sys.argv[0], '../..'))

# run this file in project floder
sys.path.insert(0, BDIR)

# need this to run django models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xai_demo.settings')
django.setup()

from xai_backend.models import Song, TopSong
from xai_backend.serializer import SongSerializer


def sample_ranking():
    songs = TopSong.objects.filter().order_by('?')[:10]
    song_list = SongSerializer(songs, many=True)
    data = song_list.data

    print(len(data[0]))

    
    df = pd.DataFrame(list(songs.values()))
    df_numerical = df.iloc[:, 6:-1]
    num_f = len(df_numerical.columns)
    w = np.random.dirichlet(np.ones(num_f),size=1).squeeze().tolist()
    
    criteria_data = Data(
        df_numerical,          # the pandas dataframe
        [True for i in range(num_f)],      # direction of goodness for each column
        anames = df['song'], # each entity's name, here car name
        cnames = df_numerical.columns, # attribute/column name
        # weights = w          # weights for each attribute (optional)
    )

    dm = simple.WeightedSum(mnorm="sum")
    dec = dm.decide(criteria_data)
    print(dec)
    print(dec.e_.points)
    print(dec.rank_)


    ret = pd.DataFrame()
    for index, row in df.iterrows():
        row['name'] = row['song']
        row['rank'] = dec.rank_[index]
        row['score'] = dec.e_.points[index]
        ret = ret.append(row)

    print(ret.shape)

    return json.dumps(ret.to_dict(orient='records'))

def sample_ranking1(*args):
    songs = TopSong.objects.filter().order_by('?')[:10]
    song_list = SongSerializer(songs, many=True)
    data = song_list.data

    df = pd.DataFrame(list(songs.values()))

    df['name'] = df['song']
    df['rank'] = df['id'].rank()
    df['year'] = 2021

    print(df.shape)

    return json.dumps(df.to_dict(orient='records'))

# sample_ranking()
# data = sample_ranking1()

# print(len(data))




# # Create your tests here.


# # logic:
# # frontend: input 1 userID (user login)
# # backend: sample a list of items (can make use of user's preference), user's weight over tags, item's weights over tags (counts of tags), calculate rank score(from item's weights)

# # frontend: dragging to make user ranking
# # backend: compare changes (on the ranking score), generate explanations



# # suppose user's weights over tags will not change while ranking. Therefore, changes occurs on artists' weights over tags.

# # cal user's preference
# #       artist.weight * artist's number of tags,  normalize to 1000 per user

# from django.db.models import Count, F, Sum, Case, When, Max, FloatField
# from django.db.models.functions import Cast


# user_id = 120

# # normalize values in dictionary to (0, 1)
# def normalize_dict(d, target=1.0):
#    raw = sum(d.values())
#    factor = target / raw
#    return {key: value * factor for key, value in d.items()}

# # user's score for each tag
# def get_user_preference(user_id):
#     tag_weights = Artist.objects.filter(userartists__userID=user_id)\
#         .annotate(tagcount=Count('usertaggedartist__tag'), 
#                 score=Cast(F('userartists__weight') / 10000.0 * F('tagcount'), FloatField()))\
#         .values(
#                 'usertaggedartist__tag',
#                 'usertaggedartist__tag__tagValue',
#                 'userartists__weight',
#                 'tagcount',
#                 'score'
#                 ).order_by('-score').filter(tagcount__gt=5)

#     tagcount = {}
#     tagname = {}
#     tagscore = {}
#     for row in tag_weights:
#         tagcount[row['usertaggedartist__tag__tagValue']] = row['tagcount']
#         tagname[row['usertaggedartist__tag__tagValue']] = row['usertaggedartist__tag__tagValue']
#         tagscore[row['usertaggedartist__tag__tagValue']] = row['score']

#     return{'ID': user_id, 'tagscore': normalize_dict(tagscore), 'tagname': tagname, 'tagcount': tagcount}


# pr = get_user_preference(user_id)
# print(pr, '\n\n\n')

# # sample items
# # artists = Artist.objects.filter(userartists__weight__gt=2000).distinct().order_by('?')[:10]
# # artists = [artist.artistID for artist in artists]
# # print(artists)


# def get_artist_list(artist_id):
#     artists_tag_weights = Artist.objects.filter(artistID=artist_id)\
#         .annotate(tagcount=Count('usertaggedartist__tag'), 
#                 )\
#         .values('artistID',
#                 'name',
#                 'usertaggedartist__tag',
#                 'usertaggedartist__tag__tagValue',
#                 'tagcount',
#                 ).order_by('-tagcount')

#     ID = artists_tag_weights[0]['artistID']
#     name = artists_tag_weights[0]['name']
#     tagcount = {}
#     tagname = {}
#     for row in artists_tag_weights:
#         tagcount[row['usertaggedartist__tag__tagValue']] = row['tagcount']
#         tagname[row['usertaggedartist__tag']] = row['usertaggedartist__tag__tagValue']

#     return{'ID': ID, 'name': name, 'tagcount': tagcount, 'tagname': tagname}

# def sample_artist_list():
#     artists = Artist.objects.filter(userartists__weight__gt=300,
#                                     userartists__userID=user_id).order_by('?')[:10]
#     artists = [artist.artistID for artist in artists]

#     artist_list = list(map(get_artist_list, artists))
    
#     # assign rank
#     for i in range(len(artist_list)):
#         artist_list[i]['rank'] = i + 1
#     print(artist_list)

#     return(artist_list)


# # artist_list = map(get_artist_list, artists)
# # print(list(artist_list))



# # dictionary= pr['tagscore']

# # print({k: v for k, v in sorted(dictionary.items(), key=lambda item: item[1])})


# # from PIL import Image
# # import matplotlib.pyplot as plt
# # from wordcloud import WordCloud

# # wc = WordCloud(background_color="white",width=900,height=900, max_words=1000,relative_scaling=0.1,normalize_plurals=False)\
# #     .generate_from_frequencies(dictionary)
# # wc.to_file('user_tags_wordcloud.png')

# # comparing 2 rankings
# #   idea: minimal changes between maximal rank_diff

# user_r = sample_artist_list()
# third_r = deepcopy(user_r)

# ran_i = randint(0, 9)
# ran_j = randint(0, 9)

# temp = user_r[ran_i]['rank']
# user_r[ran_i]['rank'] = user_r[ran_j]['rank']
# user_r[ran_j]['rank'] = temp

# user_r = sorted(user_r, key=lambda d: d['ID']) 
# # newlist = sorted(list_to_be_sorted, key=lambda d: d['name']) 

# rank_diff = {}
# for i in range(len(user_r)):
#     rank_diff[user_r[i]['ID']] = user_r[i]['rank'] - third_r[i]['rank']

# print(rank_diff, '\n\n\n')

# rank_diff = sorted(rank_diff.items(), key=lambda x:x[1])
# rank_diff = dict(rank_diff)


# print(user_r[0]['tagcount'], '\n\n\n')
# print(user_r[1]['tagcount'], '\n\n\n')


# # sum up all dict values
# def cal_sum(lst):
#     final_dict = dict()
#     for l in lst:
#         sum_dict(final_dict,l)
#     return final_dict

# def sum_dict(final_dict,iter_dict):
#     for k, v in iter_dict.items():
#         if isinstance(v, dict):
#             sum(final_dict.setdefault(k, dict()), v)
#         elif isinstance(v, int):
#             final_dict[k] = final_dict.get(k, 0) + v


# tagcount_dicts = [user_r[i]['tagcount'] for i in range(len(user_r))]
# all_tagcount = cal_sum(tagcount_dicts)
# all_tagcount = sorted(all_tagcount.items(), key=lambda x:-x[1])

# # print(dict(all_tagcount))

# # define change? 

# # for rank_diff > 0, generate counterfactual explanation
#     # if it has not these tags, it would not be top

# # for rank_diff < 0, generate normal explanation



