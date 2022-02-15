from rest_framework.decorators import api_view
from rest_framework.response import Response
from social.apiSocial.CRUD.crudModels.CRUDPost import *


@api_view(['GET', 'POST'])
def rest_post(request):
    if request.method == 'GET':
        data = all_post()
        return Response(data)
    if request.method == 'POST':
        data = save_post(request.data)
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def rest_single_post(request, pk=None):
    if request.method == 'GET':
        data = get_post(get=pk)
        return Response(data)
    elif request.method == 'PUT':
        data = update_post(update=pk, update_object=request.data)
        return Response(data)
    elif request.method == 'DELETE':
        data = delete_post(delete=pk)
        return Response(data)


@api_view(['GET'])
def rest_get_singles_posts_profile(request, pk=None):
    if request.method == 'GET':
        data = get_post_single_profile(pk)
        return Response(data)
