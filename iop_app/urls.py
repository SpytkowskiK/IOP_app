from django.urls import path

from . import views

app_name = 'iop_app'
urlpatterns = [
        path('', views.index, name='index'),
        path('parcel_machines/', views.parcel_machines, name='parcel_machines'),
        path('parcel_machine/(<int:parcel_machine_id>)/',
             views.parcel_machine_details,
             name='parcel_machine_details'),
        path('parcel_machine/create_parcel_machine/',
             views.create_parcel_machine, name='create_parcel_machine'),
        path('parcel_machine/create_worker/', views.create_worker, name='create_worker'),
        path('parcel_machine/worker/<int:worker_id>', views.worker_details, name='worker_details'),
        ]
