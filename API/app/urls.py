from django.urls import path, include

from rest_framework.routers import  DefaultRouter

from app import views

router = DefaultRouter()
router.register('profile', views.UserProfileviewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view())
]
