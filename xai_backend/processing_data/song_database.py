from ast import Delete
from operator import imod
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
from xai_backend.models import Song, SongNormalize
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data/songs_normalize.csv')
df.drop_duplicates(inplace=True)


# # put Songs to database
# for index, row in df.iterrows():

#     d = row.to_dict()
#     song = Song(**d)
#     song.save()
#     if index % 100 == 0:
#         print(index)



# to SongNormalize

SongNormalize.objects.all().delete()

numerical = df.columns[5:-1]

mm = MinMaxScaler()
df[numerical] = mm.fit_transform(df[numerical])

for index, row in df.iterrows():

    d = row.to_dict()
    song = SongNormalize(**d)
    song.save()
    if index % 100 == 0:
        print(index)




# artists = pd.read_csv('data/artists.dat', sep='\t')
# user_taggedartists = pd.read_csv('data/user_taggedartists.dat', sep='\t')
# tags = pd.read_csv('data/tags.dat', sep='\t')
# user_artists = pd.read_csv('data/user_artists.dat', sep='\t')


# for row in zip(artists['id'], artists['name']):
#     artist = Artist()
#     artist.id = row[0]
#     artist.name = row[1]
#     artist.save()

# for row in zip(user_taggedartists['userID'], user_taggedartists['artistID'], user_taggedartists['tagID']):
#     item = UserTaggedArtist()
#     item.userID = row[0]
#     item.artistID = row[1]
#     item.tagID = row[2]
#     item.save()

# for row in zip(tags['tagID'], tags['tagValue']):
#     tag = Tag()
#     tag.tagID = row[0]
#     tag.tagValue = row[1]
#     tag.save()

# for row in zip(user_artists['userID'], user_artists['artistID'], user_artists['weight']):
#     user_artist = UserArtists()
#     user_artist.userID = row[0]
#     user_artist.artistID = row[1]
#     user_artist.weight = row[2]
#     user_artist.save()

# delete invalid artistID
# valid = Artist.objects.all()
# q = UserTaggedArtist.objects.exclude(artistID__in=valid)
# print(len(q))
# q.delete()
# q = UserTaggedArtist.objects.exclude(artistID__in=valid)
# print(len(q))
