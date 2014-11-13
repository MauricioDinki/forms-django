from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import LoginView

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'app.views.FormularioView', name='Formulario'),
    url(r'^login/$', LoginView.as_view(), name='login'),
)