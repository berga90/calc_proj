from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'allcad_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'Verwalter/',include('Verwalter.urls')),	
    #url(r'^admin/', include(admin.site.urls)),
)