from rest_framework import status
from rest_framework.views import Response, Request, APIView
from items_app.models import Item
from items_app.serializers import ItemSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from items_app.permissions import IsSuperuser


class ItemList(ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()

    '''
    def post(self, request):
        data = request.data
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''


class ItemDetail(APIView):
    def get(self, request, uuid):
        try:
            reader = Item.objects.get(pk=uuid)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(reader)
        return Response(serializer.data, status=status.HTTP_200_OK)

    '''
    def patch(self, request, uuid):
        try:
            reader = Item.objects.get(pk=uuid)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(instance=reader, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        try:
            reader = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        reader.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    '''


class ItemChange(APIView):
    permission_classes = (IsSuperuser, )
    def patch(self, request, uuid):
        try:
            reader = Item.objects.get(pk=uuid)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(instance=reader, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        try:
            reader = Item.objects.get(uuid=uuid)
        except Item.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        reader.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)