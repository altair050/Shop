from gateway_app.requesters.requester import Requester
from gateway_app.requesters.authrequester import AuthRequester


class ItemsRequester(Requester):
    ITEMS_HOST = Requester.HOST + ':8001/'

    def get_item(self, uuid, token):
        headers = AuthRequester()._create_auth_header(token=token)
        response = self.get_request(self.ITEMS_HOST + str(uuid) + '/', headers=headers)
        if response is None:
            return self.BASE_HTTP_ERROR

        return response, response.status_code

    def get_all_items(self, token):
        headers = AuthRequester()._create_auth_header(token=token)
        response = self.get_request(self.ITEMS_HOST, headers=headers)
        if response is None:
            return self.BASE_HTTP_ERROR

        return response, response.status_code
