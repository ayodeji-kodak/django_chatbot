from chatbot.views import homeController
from django.urls import path


app_name="chatbot"
urlpatterns = [
    path('', homeController, name="home"),
]
