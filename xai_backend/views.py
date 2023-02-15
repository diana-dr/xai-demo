from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from xai_backend.models import Song

# from xai_backend.models import Artist
from xai_backend.serializer import SongSerializer
# from django.db.models import Count, F, Sum, Case, When, Max, FloatField
# from django.db.models.functions import Cast
# from xai_backend.services import normalize_dict


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

# class ArtistViewSet(viewsets.ModelViewSet):
#     queryset = Artist.objects.all()
#     serializer_class = ArtistSerializer

#     # user's score for each tag
#     def get_user_preference(self, user_id):
#         tag_weights = Artist.objects.filter(userartists__userID=user_id)\
#             .annotate(tagcount=Count('usertaggedartist__tag'), 
#                     score=Cast(F('userartists__weight') / 10000.0 * F('tagcount'), FloatField()))\
#             .values(
#                     'usertaggedartist__tag',
#                     'usertaggedartist__tag__tagValue',
#                     'userartists__weight',
#                     'tagcount',
#                     'score'
#                     ).order_by('-score').filter(tagcount__gt=5)

#         tagcount = {}
#         tagname = {}
#         tagscore = {}
#         for row in tag_weights:
#             tagcount[row['usertaggedartist__tag__tagValue']] = row['tagcount']
#             tagname[row['usertaggedartist__tag__tagValue']] = row['usertaggedartist__tag__tagValue']
#             tagscore[row['usertaggedartist__tag__tagValue']] = row['score']

#         return{'ID': user_id, 'tagscore': normalize_dict(tagscore), 'tagname': tagname, 'tagcount': tagcount}

#     # artist's features
#     def get_artist(self, artist_id):
#         artists_tag_weights = Artist.objects.filter(artistID=artist_id)\
#             .annotate(tagcount=Count('usertaggedartist__tag'), 
#                     )\
#             .values('artistID',
#                     'name',
#                     'usertaggedartist__tag',
#                     'usertaggedartist__tag__tagValue',
#                     'tagcount',
#                     ).order_by('-tagcount')

#         ID = artists_tag_weights[0]['artistID']
#         name = artists_tag_weights[0]['name']
#         tagcount = {}
#         tagname = {}
#         for row in artists_tag_weights:
#             tagcount[row['usertaggedartist__tag__tagValue']] = row['tagcount']
#             tagname[row['usertaggedartist__tag']] = row['usertaggedartist__tag__tagValue']

#         return{'ID': ID, 'name': name, 'tagcount': tagcount, 'tagname': tagname}

#     # random 3rd ranking
#     def sample_artist_list(self, request):
#         if request.method == 'GET':
#             artists = Artist.objects.order_by('?')[:10]
#             artists = [artist.artistID for artist in artists]

#             artist_list = map(self.get_artist, artists)
#             return(list(artist_list))

