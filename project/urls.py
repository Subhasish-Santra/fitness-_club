from django.urls import path
from.import views


urlpatterns = [
    
    path('',views.index),
    path('registration',views.registration),
    path('reg',views.reg),
    path('Contact',views.Contact),
    path('signin',views.signin),
    path('sign',views.sign),
    path('success',views.success),
    path('del/<int:id>',views.delete),
    path('editdata/<int:id>',views.editdata),
    path('edit/<int:id>',views.edit),
    path('logout', views.logout),
    path('register/', views.register, name='register'),
    path('success/', views.success_view, name='success_url'),
    path('index', views.index),
    path('index_2', views.index_2),
    path('success', views.success),
    path('subscription', views.subscription),
    path('payment', views.payment),
    path('explore', views.explore, name='explore'),
    path('registration', views.registration, name='registration'),
    path('save_registration', views.save_registration, name='save_registration'),
    # Add other URL patterns here
]
