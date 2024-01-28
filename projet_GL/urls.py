from django.contrib import admin
from django.urls import path, include
from authentification.views import google_auth, google_auth_callback  # Make sure to adjust the import statement based on your project structure
from django.urls import path
from rendezvous.views import rendezvous_form
from authentification.views import avocat_list
from authentification.views import search_avocats

urlpatterns = [
     path('search/', search_avocats, name='search_avocats'), 
    path('admin/', admin.site.urls),
    # urls.py
    path('avocats/', avocat_list, name='avocat-list'),
    path('accounts/', include('allauth.urls')),
    # ...
    path('google-auth/', google_auth, name='google-auth'),
    path('google-auth-callback/', google_auth_callback, name='google-auth-callback'),
    # Other URLs for your application...
    path('rendezvous/', rendezvous_form, name='rendezvous_form'),
]
