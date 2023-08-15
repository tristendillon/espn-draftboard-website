from django.urls import path
from .views import *

urlpatterns = [
    path('create-draft/', PostDraftView.as_view(),),
    path('create-team/', PostTeamView.as_view(),),
    path('create-pick/', PostPickView.as_view(),),
    path('create-timer/', PostTimerView.as_view(),),

    path('get-draft/<str:draft_id>/', GetDraftView.as_view(),),
    path('get-teams/<str:draft_id>/', GetTeamView.as_view(),),
    path('get-picks/<str:draft_id>/', GetPickView.as_view(),),
    path('get-timer/<str:draft_id>', GetTimerView.as_view(),),
]