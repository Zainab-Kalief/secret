from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^sign_up$', views.dataTest),
    url(r'^log_in$', views.loginTest),
    url(r'^result/(?P<id>\d+)$', views.result),
    url(r'^message/(?P<id>\d+)$', views.post_message),
    url(r'^like/(?P<post_id>\d+)/(?P<user_id>\d+)$', views.like_post),
    url(r'^log_out$', views.index),
    url(r'^result$', views.result), #i dont think this is working
    url(r'^view_likes/(?P<post_id>\d+)$', views.view_likes),
    url(r'^delete/(?P<post_id>\d+)$', views.delete_post),
    url(r'^secrets$', views.popular_secrets),

]
