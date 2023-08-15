from django.urls import path
from .views import PostTest

urlpatterns = [
    path('post-test/', PostTest.as_view()),
]