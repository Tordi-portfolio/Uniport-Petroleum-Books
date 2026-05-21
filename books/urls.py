from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('book_list', views.book_list, name='book_list'),
    path('register/', views.register_view, name='register'),
    # ✅ ADD THIS LINE
    path('mybooks/', views.mybooks, name='mybooks'),
    # 🔐 CUSTOM ADMIN PANEL
    path('admin-unlock/', views.admin_unlock_page, name='admin_unlock'),
    path("book/<int:book_id>/", views.book_detail, name="book_detail"),
    # 🔁 TOGGLE ACCESS (LOCK/UNLOCK)
    path('toggle-access/<int:user_id>/<int:book_id>/',
         views.toggle_book_access,
         name='toggle_access'),


    
    # RESET PASSWORD
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]