from django.urls import path
from cowsay import views

urlpatterns = [
    path('', views.singlecowsay,name='homepage'),
    path('history/', views.topcowsay)
]