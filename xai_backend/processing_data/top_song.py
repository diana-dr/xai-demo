import sys
import os
import django

BDIR = os.path.abspath(os.path.join(sys.argv[0], '../../..'))

# run this file in project floder
sys.path.insert(0, BDIR)

# need this to run django models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xai_demo.settings')
django.setup()

import pandas as pd
from xai_backend.models import TopSong
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data/spotify_top50_2021.csv')
# df.drop_duplicates(inplace=True)


df = df.rename({'artist_name': 'artist', 'track_name': 'song'}, axis='columns')
df = df.drop(columns=['track_id', 'time_signature']).fillna(0)

# print(TopSong.objects.all())

# put Songs to database
for index, row in df.iterrows():

    d = row.to_dict()
    song = TopSong(**d)
    song.save()
    if index % 10 == 0:
        print(index)



# to SongNormalize

# SongNormalize.objects.all().delete()

# numerical = df.columns[5:-1]

# mm = MinMaxScaler()
# df[numerical] = mm.fit_transform(df[numerical])

# for index, row in df.iterrows():

#     d = row.to_dict()
#     song = SongNormalize(**d)
#     song.save()
#     if index % 100 == 0:
#         print(index)
