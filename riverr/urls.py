
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from riverrapp import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gigs/(?P<id>[0-9]+)$', views.gig_detail, name='gig_detail'),
    url(r'^create_gig/$', views.create_gig, name='create_gig'),
    url(r'^profile/(?P<username>\w+)/$', views.profile, name='profile'),
    url(r'^category/(?P<link>[\w|-]+)/$', views.category, name='category'),
    url(r'^my_gigs/$', views.my_gigs, name='my_gigs'),
    url(r'^edit_gig/(?P<id>[0-9]+)$', views.edit_gig, name='edit_gig'),
    url(r'^login/$', views.login, {'template_name': 'templates/login.html'}, name='login'),
    url(r'^logout/$', views.logout,{'template_name': 'templates/logout.html'}, name='logout'),
    url(r'^my_sellings/$', views.my_sellings, name='my_sellings'),
    url(r'^my_buyings/$', views.my_buyings, name='my_buyings'),
    url(r'^search/$', views.search, name='search'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^checkout$', views.checkout, name="checkout_page"),
    url(r'^$', views.payment_form, name="payment_page"),
    url(r'^thank-you$', views.thank_you, name="thank_you.html"),
    url(r'^admin/', admin.site.urls),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
