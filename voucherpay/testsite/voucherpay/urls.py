from django.urls import path

from . import views

urlpatterns = [
    path('documents/<application_name>/<form_name>/<id>', views.reliance_documents, name='documents'),
]