from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("register", views.register, name="register"),
    path("prediction/<str:id>/", views.predictionPage, name="prediction"),
    path("create", views.create_prediction_event, name="create"),
    path("comment/<str:id>/", views.comment, name="comment"),
    path("save/<str:id>/", views.save, name="save"),
    path("delete/<str:id>/", views.delete, name="delete"),
    #path("wishlist", views.wishlist, name="wishlist"),
    #path("predict/<str:name>/", views.predict, name="predict"),
    #path("categories", views.categories, name="categories"),
    #path('category/<str:cat>/', views.index, name='category'),'''
]