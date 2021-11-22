from django.urls import path
from . import views
from .views import TokenObtainPairViewSelf

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),

    # user endpoints
    path('user-list/', views.userList, name='user-list'),
    path('user-create/', views.userCreate, name='user-create'),
    path('user-login/', TokenObtainPairViewSelf.as_view(), name='token_obtain_pair'),
    path('user-detail/<int:pk>/', views.userDetail, name='user-detail'),
    path('user-update/<int:pk>/', views.userUpdate, name='user-update'),
    path('user-delete/<int:pk>/', views.userDelete, name='user-delete'),

    # library card endpoints
    path('library-card-list/', views.libraryCardList, name='library-card-list'),
    path('library-card-detail/<int:pk>/', views.libraryCardDetail, name='library-card-detail'),

    # book endpoints
    path('book-list/', views.bookList, name='book-list'),
    path('book-create/', views.bookCreate, name='book-create'),
    path('book-detail/<int:pk>/', views.bookDetail, name='book-detail'),
    path('book-update/<int:pk>/', views.bookUpdate, name='book-update'),
    path('book-delete/<int:pk>/', views.bookDelete, name='book-delete'),

    # author endpoints
    path('author-create/', views.authorCreate, name='author-create'),
    path('author-list/', views.authorList, name='author-list'),

    # genre endpoints
    path('genre-create/', views.genreCreate, name='genre-create'),
    path('genre-list/', views.genreList, name='genre-list'),

    # publisher endpoints
    path('publisher-create/', views.publisherCreate, name='publisher-create'),
    path('publisher-list/', views.publisherList, name='publisher-list'),
]