from django.conf.urls import include, url

from index_page.views import IndexView, change, change_profil, VorotaView, DoorView, RoletuView, GalleryView, send, \
    show_image

from . import views


urlpatterns = [
    url(r'^change/(?P<element_id>\d+)/$', change, name='product_details'),
    url(r'^change/profil/(?P<element_id>\d+)/$', change_profil, name='details'),
    url(r'^$', IndexView.as_view(), name="home_page"),
    url(r'^vorota/$', VorotaView.as_view(), name="vorota"),
    url(r'^door/$', DoorView.as_view(), name="door"),
    url(r'^roletu/$', RoletuView.as_view(), name="roletu"),
    url(r'^gallery/$', GalleryView.as_view(), name="gallery"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^about-us/$', views.about, name="about_us"),
    url(r'send_mail/', send, name="send_mail"),
    url(r'gallery/(?P<element_id>\d+)/$', show_image, name="gallery_id"),


]