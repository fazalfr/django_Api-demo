
from django.conf.urls import url
from BookApp import views


urlpatterns=[
    url(r'^user$',views.userApi),
    url(r'^user/([0-9]+)$',views.userApi),

    url(r'^ebook$',views.ebookApi),
    url(r'^ebook/([0-9]+)$',views.ebookApi),
]