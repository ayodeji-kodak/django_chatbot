from .views import messageAPI
from django.urls import path


app_name="apis"
urlpatterns = [
    path('message/', messageAPI, name="get-response"),
]