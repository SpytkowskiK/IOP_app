from django.contrib import admin
from .models import Worker, ParcelMachine


class WorkerInline(admin.StackedInline):
    model = Worker


@admin.register(ParcelMachine)
class ParcelMachineAdmin(admin.ModelAdmin):
    list_display = ['serial_number', 'user']
    inlines = [
            WorkerInline
            ]


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['parcel_machine', 'qc']
    list_filter = ['parcel_machine']