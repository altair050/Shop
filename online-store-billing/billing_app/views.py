from rest_framework import status
from rest_framework.views import Response, Request, APIView
from billing_app.models import Billing
from billing_app.serializers import BillingSerializer
from rest_framework.generics import ListCreateAPIView
from billing_app.requesters.requester import Requester
from billing_app.permissions import IsAuthenticated


class BillingList(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = BillingSerializer

    def get_queryset(self):
        return Billing.objects.all()


class BillingDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, uuid):
        try:
            billing = Billing.objects.get(pk=uuid)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BillingSerializer(billing)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, uuid):
        try:
            billing = Billing.objects.get(pk=uuid)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BillingSerializer(instance=billing, data=request.data)
        #print(serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid):
        try:
            billing = Billing.objects.get(uuid=uuid)
        except Billing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        billing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

