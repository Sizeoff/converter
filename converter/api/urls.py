from django.urls import path

from .views import convert, database

urlpatterns = [
    path('convert', convert),
    path('database', database),

]
