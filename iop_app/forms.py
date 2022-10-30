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
        fields = ['qc', 'error_list']
        labels = {'qc': 'QC', 'error_list': 'Błędy do porawy'}