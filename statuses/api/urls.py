
from django.conf.urls import url
from .views import StatusListSearchAPIView, StatusCreateAPIView

urlpatterns = [

    url(r'', StatusListSearchAPIView.as_view()),
    url(r'^create/$', StatusCreateAPIView.as_view()),
    
]
