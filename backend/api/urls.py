from django.urls import path
from .views import *

urlpatterns = [
    path('create-draft/', PostDraftView.as_view(),),
    path('create-team/', PostTeamView.as_view(),),
    path('create-pick/', PostPickView.as_view(),),
    
    path('get-draft/', GetDraftView.as_view(),),
    path('get-team/', GetTeamView.as_view(),),
    path('get-pick/', GetPickView.as_view(),),
]