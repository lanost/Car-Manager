from django.conf.urls import include, url
from django.contrib import admin

from home.views import Home

urlpatterns = [
    # Examples:
    # url(r'^$', 'CarManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Home.as_view(),name='index')
]
