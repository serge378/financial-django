import requests
from django.shortcuts import render


def userActivation(request, uid, token):
    requests.post(
        "http://127.0.0.1:8000/auth/users/activation/",
        data={"uid": uid, "token": token},
    )
    return render(request, "activate.html")
