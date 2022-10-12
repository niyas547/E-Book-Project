from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views
router=DefaultRouter()
router.register("signup",views.UsersView,basename="user")
router.register("genres",views.GenreView,basename="genre")
router.register("books",views.BookView,basename="books")
urlpatterns=[

]+router.urls