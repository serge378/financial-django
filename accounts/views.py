import requests
from django.shortcuts import render


def userActivation(request, uid, token):
    requests.post(
        f"{request.scheme}://{request.get_host()}/auth/users/activation/",
        data={"uid": uid, "token": token},
    )
    return render(request, "activate.html")
