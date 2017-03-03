from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('library.urls', namespace='library')),
    # url(r'^store', include('store.urls', namespace='store')),
    # url(r'^profile', include('users.urls', namespace='users')),
]
