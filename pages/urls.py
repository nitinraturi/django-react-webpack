from django.urls import path
from .views import index1, index2

app_name = 'pages'

urlpatterns = [
    path('', index1, name='index1'),
    path('index2', index2, name='index2')
]
