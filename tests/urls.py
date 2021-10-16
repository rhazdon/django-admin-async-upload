import django
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r"^admin_async_upload/", include("admin_async_upload.urls")),
    url(r"^admin/", include(admin.site.urls)),
]


if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        (
            r"^media/(?P<path>.*)$",
            django.views.static.serve,
            {"document_root": settings.MEDIA_ROOT},
        )
    ]
