from django.urls import path
from .views import productlist,product_detail,SearchProductsView,productlistbycategory,products_categories_partial
urlpatterns = [

    path('products', productlist.as_view()),
    path('products/<productId>/<product_name>', product_detail),
    path('products/search', SearchProductsView.as_view()),
    path('products/<category_name>', productlistbycategory.as_view()),
    path('products_categories_partial', products_categories_partial,name='products_categories_partial'),


]
