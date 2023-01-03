from django import forms

from .models import ParcelMachine, Worker


class ParcelMachineForm(forms.ModelForm):
    class Meta:
        model = ParcelMachine
        fields = ['serial_number', 'description']
        labels = {'serial_number': 'Numer seryjny',
                  'description': 'Dodatkowy opis'}


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
        labels = {'qc': 'QC'}