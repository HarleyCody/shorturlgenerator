from django.conf.urls import url
from django.contrib import admin
from shortner.views import HomeView, URLRedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r'b/(?P<shorturl>[\w-]+)/$', URLRedirectView.as_view(), name='surl'),
]
