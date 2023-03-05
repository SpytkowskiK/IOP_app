from django import forms

from .models import ParcelMachine, Worker

from crispy_forms.helper import FormHelper


class ParcelMachineForm(forms.ModelForm):
    class Meta:
        model = ParcelMachine
        fields = ['serial_number', 'description']
        labels = {'serial_number': '', 'description': ''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        data_serial_number = {
                'class': 'form__input',
                'placeholder': 'Numer Seryjny',
                }
        self.fields['serial_number'].widget.attrs.update(data_serial_number)

        data_description = {
                'class': 'form__input',
                'placeholder': 'Dodatkowa notatka',
                'rows': '5',
                }
        self.fields['description'].widget.attrs.update(data_description)


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = '__all__'
        exclude = ('parcel_machine',)
        labels = {'qc': 'QC', 'parcel_machine': 'Paczkomat'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({
                'class': 'form__input-worker',
                'placeholder': Worker._meta.get_field(
                        f'{field}').verbose_name,
                'size': '30'
                })