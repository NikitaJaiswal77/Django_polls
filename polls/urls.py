from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # /polls/
    # path("", views.index, name="index"),
    path("", views.IndexView.as_view(), name="index"),
    # /polls/deatils/
    # path("details/",views.detail,name="details")
    # ex: /polls/5/
    # path("<int:question_id>/", views.detail, name="detail"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
