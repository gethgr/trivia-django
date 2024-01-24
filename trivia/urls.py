
from django.urls import path
from trivia import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/", views.question_index, name="question_index"),

]

