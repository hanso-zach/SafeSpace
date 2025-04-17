from django.urls import path
from main import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.landing_page, name="landing_page"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('journal/', views.journal, name='journal'),
    path('mood_tracking/', views.mood_tracking, name='mood_tracking'),
    path('hotlines/', views.hotlines, name='hotlines'),
    path('community/', views.community, name='community'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('shared-journals/', views.shared_journals, name='shared_journals'),
]
