from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^register/', views.Register, name='register'),
    url(r'^login/', views.Login, name='login')
]