from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('post/', views.CreateInventoryView.as_view(), name='post'),

    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),

    path('inventorys/<int:category>', views.CategoryView.as_view(), name='inventorys_cat'),

    path('user-list/<int:user>', views.UserView.as_view(), name='user_list'),

    path('inventory-detail/<int:pk>', views.DetailView.as_view(), name='inventory_detail'),

    path('mypage/', views.MypageView.as_view(), name='mypage'),

    path('inventory/<int:pk>/delete/', views.InventoryDeleteView.as_view(), name='inventory_delete'),

    path('contact/', views.ContactView.as_view(), name = 'contact'),
]