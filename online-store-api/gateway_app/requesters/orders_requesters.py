from gateway_app.requesters.requester import Requester
from gateway_app.requesters.authrequester import AuthRequester


class OrdersRequester(Requester):
    ORDERS_HOST = Requester.HOST + ':8002/'

    def get_order(self, uuid, token=None):
        headers = {}
        if token:
            headers = AuthRequester()._create_auth_header(token)
        response = self.get_request(self.ORDERS_HOST + str(uuid) + '/', headers=headers)
        if response is None:
            return self.BASE_HTTP_ERROR
        return response, response.status_code

    def get_all_orders(self, token):
        headers = {}
        if token:
            headers = AuthRequester()._create_auth_header(token)
        response = self.get_request(self.ORDERS_HOST, headers=headers)
        if response is None:
            return self.BASE_HTTP_ERROR

        return response, response.status_code
