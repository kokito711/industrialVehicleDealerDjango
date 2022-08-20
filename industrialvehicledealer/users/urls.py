from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('/{user_code}', views.selected_user, name='defined_user')
]
