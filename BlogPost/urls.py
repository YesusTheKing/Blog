from . import views
from django.urls import path
app_name = "BlogPost"

urlpatterns = [
    path("",views.index,name="index"),
    path("blogdetail/<blog_id>/",views.detail,name="detail")
]
