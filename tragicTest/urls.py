from django.conf.urls import url
from tragicTest import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registration/$', views.registration, name='registration'),
    url(r'^login/$', views.login, name='login'),
    url(r'profile/$', views.profile, name='profile'),
    url(r'profile/uploads/$', views.profile_uploads, name='uploads'),
    url(r'profile/reviews/$', views.profile_reviews, name='reviews'),
    url(r'category/$', views.category, name='category'),
    url(r'article/$', views.article, name='article'),
]
