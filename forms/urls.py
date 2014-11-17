from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import LoginView,RegisterView,IndexView,SuccessView

urlpatterns = patterns('',

    url(r'^$', IndexView.as_view(), name='inicio'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^info/$', 'app.views.FormularioView', name='datos_personales'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^success/$', SuccessView.as_view(), name='success'),
)