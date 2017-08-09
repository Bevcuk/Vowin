from django.conf.urls import url

from blog.views import PostList, DetailsList
from . import views


urlpatterns = [
    url(r'^$', PostList.as_view(), name='post_list'),
    url(r'^details/(?P<post_id>\d+)/$', DetailsList.as_view(), name='post_list'),
]