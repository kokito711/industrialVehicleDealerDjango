from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('/<int:user_code>', views.selected_user, name='defined_user'),
    path('/auth', views.auth, name='user_auth')
]
