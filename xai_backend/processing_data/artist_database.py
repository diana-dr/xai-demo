from ast import Delete
import sys
import os
import django

BDIR = os.path.abspath(os.path.join(sys.argv[0], '../..'))

# run this file in project floder
sys.path.insert(0, BDIR)

# need this to run django models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xai_demo.settings')
django.setup()

import pandas as pd
from xai_backend.models import Artist, UserArtists, UserTaggedArtist, Tag

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



# Logic:

# stage 1:
# frontend: input 1 userID (user login)
# backend: sample a list of items (can make use of user's preference), user's weight over tags, item's weights over tags, calculate rank score(from item's weights)

# stage 2:
# frontend: dragging to make user ranking, send back 2 rankings
# backend: compare changes (on the ranking score), generate explanations


# suppose user's weights over tags will not change while ranking. Therefore, changes occurs on artists' weights over tags.

# cal user's preference
#       artist.weight * artist's number of tags,  normalize to 1000 per user
