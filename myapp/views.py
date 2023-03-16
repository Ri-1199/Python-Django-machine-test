
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ClientSerializer
from .models import Client
from rest_framework.views import APIView
from rest_framework import status, viewsets

@api_view(['GET', 'POST', 'PATCH'])
def myapp(request):
    if request.method == 'GET':
        client_objs = Client.objects.all()
        serializer = ClientSerializer(client_objs, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED
    )

    elif request.method == 'POST':
        return Response(
            {
                'status': 200,
                'message': "Yes! Django rest framework is working!!!",
                'method_called': 'You called POST method'
            }
        )

    elif request.method == 'PATCH':
        return Response(
            {
                'status': 200,
                'message': "Yes! Django rest framework is working!!!",
                'method_called': 'You called PATCH method'
            }
        )

    else:
        return Response(
            {
                'status': 400,
                'message': "Yes! Django rest framework is working!!!",
                'method_called': 'You called INVALID method'
            }
        )

@api_view(['GET'])
def get_client(request):
    client_objs = Client.objects.all()
    serializer = ClientSerializer(client_objs, many=True)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def post_client(request):
    try:
        data = request.data
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK
            )

        return Response(
            {
                'status': False,
                'message': "invalid data!!!",
                'data': serializer.errors

            }
        )


    except Exception as e:
        print(e)

    return Response(
        {
            'status': False,
            'message': "Something went wrong!!!",
            'method_called': 'You called INVALID method'
        }
    )

    # ClientSerializer

@api_view(['PATCH'])
def patch_client(request):
    try:
        data = request.data
        if not data.get('client_name'):
            return Response({
                'status': False,
                'message': "client name is required!!!",
                'data': {}
            })

        obj = Client.objects.get(client_name = data.get('client_name'))
        serializer = ClientSerializer(obj ,  data = data , partial = True)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED
            )
        return Response(
            {
                'status': False,
                'message': "invalid data!!!",
                'data': serializer.errors

            }
        )

    except Exception as e:
        print(e)
    return Response(
            {
                'status': False,
                'message': "invalid uid!!!",
                'data': {}

            }
        )

@api_view(['DELETE'])
def delete_client(request):
    try:
        obj = Client.objects.get(client_name=get_client)
    except Client.DoesNotExist:
        msg = {"msg": "NOT FOUND"}
        return Response(msg, status=status.HTTP_400_BAD_REQUEST)


class ClientView(APIView):
    def get(self , request):
        client_objs = Client.objects.all()
        serializer = ClientSerializer(client_objs, many=True)

        return Response({
            'status': True,
            'message': 'Client fetched',
            'data': serializer.data
        })


    def post(self , request):
        try:
            data = request.data
            serializer = ClientSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': True,
                        'message': "valid data!!!",
                        'data': serializer.data

                    })

            return Response(
                {
                    'status': False,
                    'message': "invalid data!!!",
                    'data': serializer.errors

                })


        except Exception as e:
            print(e)

        return Response(
            {
                'status': False,
                'message': "Something went wrong!!!",
                'method_called': 'You called INVALID method'
            })

    def patch(self , request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({
                    'status': False,
                    'message': "uid is required!!!",
                    'data': {}
                })

            obj = Client.objects.get(uid=data.get('uid'))
            serializer = ClientSerializer(obj, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'status': True,
                        'message': "valid data!!!",
                        'data': serializer.data

                    })
            return Response(
                {
                    'status': False,
                    'message': "invalid data!!!",
                    'data': serializer.errors

                })

        except Exception as e:
            print(e)
        return Response(
            {
                'status': False,
                'message': "invalid uid!!!",
                'data': {}

            })

    def delete(self, request):
        try:
            obj = Client.objects.get(client_name = get_client)
        except Client.DoesNotExist:
            msg ={"msg":"NOT FOUND"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer



