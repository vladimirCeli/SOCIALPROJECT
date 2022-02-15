from rest_framework.decorators import api_view
from rest_framework.response import Response
from social.apiSocial.CRUD.crudModels.CRUDProfile import *


@api_view(['GET', 'POST'])
def rest_profile(request):
    print(request)
    if request.method == 'GET':
        data = all_profile()
        return Response(data)
    elif request.method == 'POST':
        data = save_profile(request.data)
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def rest_single_profile(request, pk=None):
    if request.method == 'GET':
        data = get_profile(get=pk)
        return Response(data)
    elif request.method == 'PUT':
        data = update_profile(update=pk, update_object=request.data)
        return Response(data)
    elif request.method == 'DELETE':
        data = delete_profile(delete=pk)
        return Response(data)


@api_view(['GET'])
def rest_get_profile(request, pk=None):
    if request.method == 'GET':
        data = get_profile_username(pk)
        return Response(data)
