from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('index/', views.IndexListView.as_view(), name='index'),
    path('about/', views.AboutListView.as_view(), name='about'),
    path('contact/', views.EmailListView.as_view(), name='contact'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('privacy/policy/', views.PrivacyPolicyDetailView.as_view(), name='privacy-policy'),
    path('terms/conditions/', views.PrivacyPolicyDetailView.as_view(), name='terms-conditions')
]
