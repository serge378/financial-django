from django.urls import path

from . import views

urlpatterns = [
    path(
        "categories-formations-list",
        views.CategorieFormationList.as_view(),
        name="categories-formations-list",
    ),
    path(
        "videos-formations-list",
        views.VideoFormationList.as_view(),
        name="videos-formations-list",
    ),
    path(
        "notification-payment",
        views.NotificationPaymentView.as_view(),
        name="notification-payment",
    ),
    path(
        "initialize-payment",
        views.InitializePaymentVideo.as_view(),
        name="initialize-payment",
    ),
]
