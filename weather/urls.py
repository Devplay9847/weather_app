from django import path
from . import views

urlpatterns = [
    path('view/<int:pk>',index,name='view')
    path('',views.index),
]