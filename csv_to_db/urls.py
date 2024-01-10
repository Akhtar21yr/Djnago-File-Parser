from django.urls import path
from .views import Parser,AdditionInfo

urlpatterns = [
    path('parsing-file/', Parser.as_view()),
    path('parsing-file/additional/', AdditionInfo.as_view()),
]
