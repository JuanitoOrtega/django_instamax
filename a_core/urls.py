from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

# Sitemaps
from django.contrib.sitemaps.views import sitemap
from a_posts.sitemaps import StaticSitemap, CategorySitemap, PostpageSitemap

sitemaps = {
    'static': StaticSitemap,
    'categories': CategorySitemap,
    'postpages': PostpageSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('theboss/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('inbox/', include('a_inbox.urls')),
    path('', include('a_posts.urls')),
    path('_/', include('a_landingpages.urls')),
    path('', include('a_users.urls')),
]

# Only used when DEBUG=True, whitenoise can serve files when DEBUG=False
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)