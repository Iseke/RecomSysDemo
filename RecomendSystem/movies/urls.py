from django.urls import path

from movies import views

urlpatterns = [
    path('genre/', views.GenreList.as_view()),
    path('genre/<int:pk>/', views.GenreDetail.as_view()),
    path('genre/<int:pk>/movies/', views.MovieList.as_view()),
    path('genre/<int:pk1>/movies/<int:pk2>/', views.MovieDetail.as_view()),
    path('genre/<int:pk1>/movies/<int:pk2>/rating/', views.SetRating.as_view()),
    path('movies/getBest/', views.getBest.as_view())
]