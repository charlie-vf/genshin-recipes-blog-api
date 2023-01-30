from django.urls import path
from made import views

urlpatterns = [
    path('made/', views.MadeList.as_view()),
    path('made/<int:pk>', views.MadeDetail.as_view()),
]
