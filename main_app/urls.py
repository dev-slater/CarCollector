from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
path('', views.Home.as_view(), name="home"),
path('about/', views.About.as_view(), name="about"),
path('index/', views.Index.as_view(), name="index"),
path('cars/', views.CarList.as_view(), name="car_list"),
path('cars/new/',views.CarCreate.as_view(), name="car_create"),
path('colors/new/',views.ColorCreate.as_view(), name="color_create"),
path('colors/list/<int:pk>',views.ColorList.as_view(), name="color_list"),
path('cars/<int:pk>/', views.CarDetail.as_view(), name="car_detail"),
path('cars/<int:pk>/update', views.CarUpdate.as_view(), name="car_update"),
path('cars/<int:pk>/delete', views.CarDelete.as_view(), name="car_delete"),

]