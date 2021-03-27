from django.urls import path
from sub_api import views

urlpatterns = [
    path('category/', views.CategoryApiView.as_view()),
    path('sub_category/', views.subCategoryApiView.as_view()),
]
