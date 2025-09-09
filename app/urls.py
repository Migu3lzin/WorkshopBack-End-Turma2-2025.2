
from django.urls import path
from .views import *

urlpatterns = [

    path("index/", view=index, name="index"),
]
