from django.conf.urls import url
from .views import do_search
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from products.views import all_products
from accounts import urls as urls_accounts
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from django.views import static
import os
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


urlpatterns = [
    url(r'^$', do_search, name='search'),
url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
]