from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import LoginView,RegisterView

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^info/$', 'app.views.FormularioView', name='datos_personales'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
)