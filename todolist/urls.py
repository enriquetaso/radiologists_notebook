from django.urls import path, include
from todolist import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"task", views.TaskViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
