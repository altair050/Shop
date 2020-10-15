from django.shortcuts import render
from rest_framework import status
from rest_framework.views import Response, Request, APIView
from gateway_app.requesters.items_requester import ItemsRequester
from gateway_app.requesters.orders_requesters import OrdersRequester
from gateway_app.requesters.authrequester import AuthRequester
from gateway_app.requesters.requester import Requester
from gateway_app.permissions import IsAuthenticated, IsAppTokenCorrect


class ItemsList(APIView):
    permission_classes = (IsAuthenticated,)
    REQUESTER = Requester()
    ITEMS_REQUESTER = ItemsRequester()

    def get(self, request):
        print('1')
        token = self.REQUESTER.get_token_from_request(request)
        print('2')
        response, status_code = self.ITEMS_REQUESTER.get_all_items(token)
        print('3')
        if status_code != 200:
            return Response(status=status_code)
        print('4')
        data_from_response = self.REQUESTER.get_data_from_response(response)
        return Response(data_from_response, status=status.HTTP_200_OK)

class ItemDetail(APIView):
    permission_classes = (IsAuthenticated,)
    REQUESTER = Requester()
    ITEMS_REQUESTER = ItemsRequester()

    def get(self, request, uuid):
        print('1')
        token = self.REQUESTER.get_token_from_request(request)
        print('2')
        response, status_code = self.ITEMS_REQUESTER.get_item(uuid, token)
        print('3')
        if status_code != 200:
            return Response(status=status.HTTP_502_BAD_GATEWAY)
        print('4')
        data_from_response = self.REQUESTER.get_data_from_response(response)
        return Response(data_from_response, status=status.HTTP_200_OK)


class OrdersList(APIView):
    permission_classes = (IsAuthenticated, IsAppTokenCorrect)
    REQUESTER = Requester()
    ORDERS_REQUESTER = OrdersRequester()

    def get(self, request):
        print('1')
        token = self.REQUESTER.get_token_from_request(request)
        print('2')
        response, status_code = self.ORDERS_REQUESTER.get_all_orders(token)
        print('3')
        if status_code != 200:
            return Response(status=status_code)
        print('4')
        data_from_response = self.REQUESTER.get_data_from_response(response)
        return Response(data_from_response, status=status.HTTP_200_OK)

class OrderDetail(APIView):
    permission_classes = (IsAuthenticated, IsAppTokenCorrect)
    REQUESTER = Requester()
    ORDERS_REQUESTER = OrdersRequester()

    def get(self, request, uuid):
        print('1')
        token = self.REQUESTER.get_token_from_request(request)
        print('2')
        response, status_code = self.ORDERS_REQUESTER.get_order(uuid, token)
        print('3')
        if status_code != 200:
            return Response(status=status_code)
        print('4')
        data_from_response = self.REQUESTER.get_data_from_response(response)
        return Response(data_from_response, status=status.HTTP_200_OK)


