
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:year>/<int:month>',views.index,name='index'),
]