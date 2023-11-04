from django.urls import path
from django.contrib import include, path

from . import views

urlpatterns = [
    path("polls/",include("polls.url")),
    path("admin/",admin.site.urls),
    # path("polls/",views.index,name="index"),
]