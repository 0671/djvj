from django.urls import path

from .views import (
    ListCreateMydata,
    Login,
    RetrieveUpdateDestroyMydata
)

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('list-create-mydata/',ListCreateMydata.as_view(),name='list-create-mydata'),
    path('retrieve-update-destroy-mydata/<int:pk>/',RetrieveUpdateDestroyMydata.as_view(),name='retrieve-update-destroy-mydata'),
]