from django.conf.urls import url
from . import views

app_name = 'blog_main'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name = 'post_list'),
    url(r'^about/$', views.AboutView.as_view(), name = 'about_me'),
    url(r'^posts/(?P<pk>\d+)$', views.PostDetailView.as_view(), name = 'post_detail'),
    url(r'^posts/new/', views.PostCreateView.as_view(), name = 'post_create'),
    url(r'^posts/(?P<pk>\d+)/update/$', views.PostUpdateView.as_view(), name = 'post_update'),
    url(r'^posts/(?P<pk>\d+)/delete/$', views.PostDeleteView.as_view(), name = 'post_delete'),
    url(r'^posts/drafts/$', views.PostDraftListView.as_view(), name = 'post_drafts'),
    url(r'^posts/(?P<pk>\d+)/add_comment/$', views.add_comment_to_post, name = 'post_add_comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.aprove_comment, name = 'aprove_comment'),
    url(r'^comment/(?P<pk>\d+)/delete/$', views.delete_comment, name = 'delete_comment'),
    url(r'^posts/(?P<pk>\d+)/publish/$', views.publish_post, name = 'post_publish'),

]
