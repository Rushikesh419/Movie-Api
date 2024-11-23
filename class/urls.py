from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movieinfo/',views.MovieAPI.as_view()),
    path('movieinfo/<int:pk>',views.MovieAPI.as_view()),
]
