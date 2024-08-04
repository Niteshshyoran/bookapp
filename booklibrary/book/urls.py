from django.urls import path,include
from .views import RegisterView,loginView,AuthorRegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(),name= 'register'),
    path('login/', loginView.as_view(),name= 'login'),
    path('author/', AuthorRegisterView.as_view(),name= 'author'),
    path('author/<int:pk>/update/', AuthorRegisterView.as_view(),name= 'authorupdate'),
    path('book/', AuthorRegisterView.as_view(),name= 'book'),
    path('book/<int:pk>/update/', AuthorRegisterView.as_view(),name= 'bookupdate'),
    path('country/', AuthorRegisterView.as_view(),name= 'country'),
]
