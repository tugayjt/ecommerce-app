from django.contrib import admin
from django.urls import path, include
from store import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('store.urls')),
    path('', views.product_list, name='product_list')]
