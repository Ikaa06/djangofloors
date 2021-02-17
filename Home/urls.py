from django.urls import path

from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('about', views.about.as_view(), name='about'),
    path('floor/<slug:slug>/', views.concrete_floors.as_view(), name='concrete_floors'),
    path('polymer-floors', views.polymer.as_view(), name='polymer'),
    path('contacts', views.contacts.as_view(), name='contacts'),
    path('vacancies', views.vacancies.as_view(), name='vacancies'),
    path('vacancy/<slug:slug>', views.vacancy.as_view(), name='vacancy'),
    path('solutions', views.ready_solutions.as_view(), name='ready_solutions'),
    path('solution/<slug:slug>', views.ready_solution.as_view(), name='ready_solution'),
    path('objects', views.ready_objects.as_view(), name='ready_objects'),
    path('object/<slug:slug>', views.ready_object.as_view(), name='ready_object'),
    path('add_application', views.AdviseFreeView.as_view(), name='application'),
    path('add_resume', views.ResumeFreeView.as_view(), name='add_resume'),
    path('add_order', views.OrderPaymentView.as_view(), name='add_order'),
    path('add_order_object', views.OrderPaymentObjectView.as_view(), name='add_order_object')

]
