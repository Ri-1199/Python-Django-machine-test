
from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'client-view-set', ClientViewSet, basename='client')

urlpatterns = [

    path('', myapp , name ="myapp"),
    path('get-client/', get_client, name = "get_client"),
    path('patch-client/', patch_client, name = "patch_client"),
    path('post-client/', post_client , name="post_client"),

    path('client/', ClientView.as_view()),

]

urlpatterns += router.urls