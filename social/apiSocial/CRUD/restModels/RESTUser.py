from rest_framework.decorators import api_view
from rest_framework.response import Response

from social.apiSocial.CRUD.crudModels.CRUDUser import *


@api_view(['GET', 'POST'])
def rest_user(request):
    if request.method == 'GET':
        data = all_user()
        return Response(data)
    elif request.method == 'POST':
        data = save_user(request.data)
        return Response(data)


@api_view(['GET', 'PUT', 'DELETE'])
def rest_single_user(request, pk=None):
    if request.method == 'GET':
        data = get_user(get=pk)
        return Response(data)
    elif request.method == 'PUT':
        data = update_user(update=pk, update_object=request.data)
        return Response(data)


@api_view(['GET'])
def rest_single_user_username(request, pk=None):
    if request.method == 'GET':
        data = get_user_username(get=pk)
        return Response(data)

@api_view(['GET'])
def rest_single_user_email(request, pk=None):
    if request.method == 'GET':
        data = get_user_email(get=pk)
        return Response(data)


@api_view(['POST'])
def rest_auth_username(request):
    if request.method == 'POST':
        data = authentication(data=request.data)
        return Response(data)
