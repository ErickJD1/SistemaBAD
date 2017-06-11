from django.conf.urls import url, include
from .views import IndexView

urlpatterns = [

    url(r'^vista$', IndexView.as_view(), name='vista'),
   
]
