from django.urls import path
from sub_api import views

urlpatterns = [
path('subject/', views.SubjectApiView.as_view()),
]
