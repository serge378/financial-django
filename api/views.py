import environ
import requests
from django.shortcuts import get_object_or_404
from rest_framework import generics, status, views
from rest_framework.response import Response

from . import models, serializers

env = environ.Env()
# reading .env file
environ.Env.read_env()


class CategorieFormationList(generics.ListAPIView):
    # permission_classes = [permissions.AllowAny]
    queryset = models.CategorieFormation.objects.all()
    serializer_class = serializers.CategorieFormationSerializer


class VideoFormationList(generics.ListAPIView):
    # permission_classes = [permissions.AllowAny]
    queryset = models.VideoFormation.objects.all()
    serializer_class = serializers.VideoFormationSerializer


class InitializePaymentVideo(views.APIView):
    def post(self, request):
        try:
            data = request.data
            user = self.request.user
            video = get_object_or_404(models.VideoFormation, pk=data["video_id"])
            payment = models.PaymentVideo(
                transaction_id=data["transaction_id"],
                video=video,
                author=user,
                description=data["description"],
                site_id=env("CINET_PAY_SITE_ID"),
            )
            payment.save()
            return Response(
                {"response": "transaction initialized"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {"response": "error during initialize"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class NotificationPaymentView(views.APIView):
    def get(self, request, format=None):
        return Response({"response": "OK"}, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        try:
            data = request.data
            print(data)
            cpm_trans_id = data["cpm_trans_id"]
            payment = get_object_or_404(
                models.PaymentVideo, transaction_id=cpm_trans_id
            )
            payment.phone_number = data["cel_phone_num"]
            payment.phone_prefix = data["cpm_phone_prefixe"]
            if payment.status is False:
                response = self.check_payment(cpm_trans_id)
                payment.devise = response.data["currency"]
                payment.payment_method = response.data["payment_method"]
                payment.amount = response.data["amount"]
                payment.description = response.data["description"]
                if response["message"] == "SUCCESS":
                    payment.transaction_date = response.data["payment_date"]
                    payment.status = True
                else:
                    payment.error_message = response["message"]
                payment.save()
                video = payment.video
                video.access_by.add()
            else:
                pass
            return Response({"response": "received"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {"response": "error"},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def check_payment(self, transaction_id):
        try:
            apikey = env("CINET_PAY_API_KEY")
            site_id = env("CINET_PAY_SITE_ID")
            data = {
                "apikey": apikey,
                "site_id": site_id,
                "transaction_id": transaction_id,
            }
            response = requests.post(
                "https://api-checkout.cinetpay.com/v2/payment/check", data=data
            )
            return response
        except Exception as e:
            return e
