from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path('form-example-class/', views.form_example_class, name="form_example_class"),
    path('form-django-template/', views.form_example_template, name="form_example_template"),
    path("order-form-example/", views.order_form_example, name="order_form_example"),
]
