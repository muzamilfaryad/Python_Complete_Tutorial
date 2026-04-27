from django.urls import include, path
from rest_framework.routers import DefaultRouter

from home.views import PersonAPIView, PeopleViewSet, index, login, person, RegisterAPIView, LoginAPIView


router = DefaultRouter()
router.register('people', PeopleViewSet, basename='people')


urlpatterns = [
    path('', include(router.urls)),
    path("index/", index),
    path('person/', person),
    path('persons/', PersonAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view())
]
