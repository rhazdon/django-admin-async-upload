from django.urls import path

from . import views

urlpatterns = [
    path("upload/", views.UploadView.as_view(), name="admin_async_upload"),
]
