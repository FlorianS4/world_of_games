from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq, name='faq'),
    path('edit/<int:faq_id>/', views.edit_faq, name='edit_faq'),
]
