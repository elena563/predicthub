from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    #path("register", views.register, name="register"),
    path("prediction/<str:name>/", views.predictionPage, name="prediction"),
    path("create", views.create_prediction_event, name="create"),
    #path("comment/<str:name>/", views.comment, name="comment"),
    '''path("save/<str:name>/", views.save, name="save"),
    path("cancel/<str:name>/", views.cancel, name="cancel"),
    path("wishlist", views.wishlist, name="wishlist"),
    path("predict/<str:name>/", views.predict, name="predict"),
    path("categories", views.categories, name="categories"),
    path('category/<str:cat>/', views.index, name='category'),'''
]