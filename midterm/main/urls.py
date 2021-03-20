from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main import views
from main.views import BookViewSet, JournalViewSet
from rest_framework import routers

router = DefaultRouter()
router.register(r'books', viewset=views.BookViewSet, basename='books')
router.register(r'journals', viewset=views.JournalViewSet, basename='journals')

urlpatterns = [
    path('', include(router.urls))
]