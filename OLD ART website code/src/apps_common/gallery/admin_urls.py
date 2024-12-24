from django.contrib import admin
from django.conf.urls import url
from . import admin_views


app_name = 'admin_gallery'
urlpatterns = [
    url(r'^create/$', admin.site.admin_view(admin_views.GalleryCreate.as_view()), name='create'),
    url(r'^delete/$', admin.site.admin_view(admin_views.GalleryDelete.as_view()), name='delete'),
    url(r'^upload/$', admin.site.admin_view(admin_views.UploadImage.as_view()), name='upload'),
    url(r'^upload_video/$', admin.site.admin_view(admin_views.UploadVideoImage.as_view()), name='upload_video'),
    url(r'^delete_item/$', admin.site.admin_view(admin_views.DeleteItem.as_view()), name='delete_item'),
    url(r'^rotate_item/$', admin.site.admin_view(admin_views.RotateItem.as_view()), name='rotate_item'),
    url(r'^crop_item/$', admin.site.admin_view(admin_views.CropItem.as_view()), name='crop_item'),
    url(r'^item_form/$', admin.site.admin_view(admin_views.EditItem.as_view()), name='edit_item'),
    url(r'^sort/$', admin.site.admin_view(admin_views.SortItems.as_view()), name='sort'),
]
