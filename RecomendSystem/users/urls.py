from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
    # path('profiles/', views.UserList.as_view()),
    # path('profiles/<int:pk>/', views.FavMov.as_view()),
]