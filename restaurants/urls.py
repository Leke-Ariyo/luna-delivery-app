from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/restaurant/(?P<pk>[0-9]+)$',
        views.get_delete_update_restaurant,
        name='get_delete_update_restaurant'
    ),
    url(
        r'^api/v1/restaurant/$',
        views.get_post_restaurant,
        name='get_post_restaurant'
    )
]
