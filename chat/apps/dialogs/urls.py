from django.urls import path

from . import views

app_name = 'dialogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:arg>/', views.det, name='det'),
    path('<int:dialog_id>/nm/', views.nmess, name='nm'),
]
