
from django.conf.urls import url, include
from django.contrib import admin
from updates.views import(
json_example_view,
SerializeDetailView,
SerializeListView) 
urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^api/status/', include('statuses.api.urls')),
   
]
