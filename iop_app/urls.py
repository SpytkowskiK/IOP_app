from django.urls import path

from . import views

app_name = 'iop_app'
urlpatterns = [
        path('', views.index, name='index'),
        path('parcel_machines/', views.parcel_machines, name='parcel_machines'),
        path('parcel_machines/(<int:parcel_machine_id>)/',
             views.parcel_machine_details,
             name='parcel_machine_details'),
        path('parcel_machines/history/', views.parcel_machines_all,
             name='parcel_machines_all'),
        path('parcel_machines/create_parcel_machine/',
             views.create_parcel_machine, name='create_parcel_machine'),
        path('parcel_machines/create_worker/(<int:parcel_machine_id>)/',
             views.create_worker,
             name='create_worker'),
        path('parcel_machines/worker/<int:worker_id>/', views.worker_details,
             name='worker_details'),
        path('parcel_machines/worker/edit_worker/<int:worker_id>/',
             views.edit_worker, name='edit_worker'),
        path('parcel_machines/worker/delete_worker/<int:worker_id>/',
             views.delete_worker, name='delete_worker'),
        path('parcel_machines/delete_parcel_machine/<int:parcel_machine_id>/',
             views.delete_parcel_machine, name='delete_parcel_machine'),
        path('parcel_machines/history/delete_history/', views.delete_history,
             name='delete_history'),
        path('parcel_machines/download_xmls/', views.download_xlsx,
             name="download_xlsx")
        ]
