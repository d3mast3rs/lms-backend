from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),

    # user endpoints
    path('user-list/', views.userList, name='user-list'),
    path('user-create/', views.userCreate, name='user-create'),
    path('user-detail/<int:pk>/', views.userDetail, name='user-detail'),
    path('user-update/<int:pk>/', views.userUpdate, name='user-update'),
    path('user-delete/<int:pk>/', views.userDelete, name='user-delete'),

    # book endpoints
    path('book-list/', views.bookList, name='book-list'),
    path('book-create/', views.bookCreate, name='book-create'),
    path('book-detail/<int:pk>/', views.bookDetail, name='book-detail'),
    path('book-update/<int:pk>/', views.bookUpdate, name='book-update'),
    path('book-delete/<int:pk>/', views.bookDelete, name='book-delete'),
]