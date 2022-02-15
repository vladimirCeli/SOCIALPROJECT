from rest_framework.decorators import api_view
from rest_framework.response import Response
from social.apiSocial.CRUD.crudModels.CRUDSubscribe import *


@api_view(['GET'])
def get_all_subscribe_user(request, pk):
    data = ''
    if request.method == 'GET':
        data = get_subscript(pk)
    else:
        data = "NO ITEM"
    return Response(data)


@api_view(['GET'])
def set_subscribe_user(request, to, of_from):
    data = ''
    if request.method == 'GET':
        data = set_subscribe(to, of_from)
    else:
        data = "NO ITEM"
    return Response(data)


@api_view(['GET'])
def delete_subscribe_user(request, to, of_from):
    if request.method == 'GET':
        data = delete_subscribe(to, of_from)
    else:
        data = "NO ITEM"
    return Response(data)


@api_view(['GET'])
def get_all_subscription_user(request, pk):
    data = ''
    if request.method == 'GET':
        data = get_subscript_user(pk)
    else:
        data = "NO ITEM"
    return Response(data)
