from django.urls import path

from . import views
# from Titanic_Survial_Prediction_Web import views

urlpatterns = [
    path('', views.index, name='predictions_index'),
]
