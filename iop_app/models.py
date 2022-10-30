from pyexpat import model
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Lista błędów
ERROR_LIST=(
        ('brak_ceownika', 'Brak ceownika'),
        ('brak_elementów_zlacznych', 'Brak elementów złącznych'),
        ('brak_markera', 'Brak markera'),
        ('brak_nagran_z_kamer', 'Brak nagrań z kamer'),
        ('brak_naklejek_zs', 'Brak naklejek ZS'),
        ('brak_nitow', 'Brak nitów'),
        ('brak_obrazu', 'Brak obrazu'),
        ('brak_odbojnikow', 'Brak odbojników'),
        ('brak_pieczatki_qc', 'Brak pieczątki QC'),
        ('brak_przepustu_kablowego', 'Brak przepustu kablowego'),
        ('brak_segerów', 'Brak segerow'),
        ('brak_uchwytu_przewodow', 'Brak uchwytu przewodów'),
        ('brak_uszczelki', 'Brak uszczelki'),
        ('brak_zaslepki_dachowej', 'Brak zaślepki dachowej'),
        ('brak_zlacza_qpd', 'Brak złącza QPD'),
        ('drzwiczki_do_regulacji', 'Drzwiczki do regulacji'),
        ('niedokrecona_krancowka', 'Niedokręcona krańcówka'),
        ('niedokrecona_nakretka_drzwiczek', 'Niedokręcona nakrętka drzwiczek'),
        ('niedokrecona_sruba','Niedokręcona śruba'),
        ('niedokrecony_przewod','Niedokręcony przewód'),
        ('niedokrecone_uziemienie', 'Niedokręcone uziemienie'),
        ('niedokrecony_zawias_drzwiczek','Niedokręcony zawias drzwiczek'),
        ('niedzialajaca_kamera', 'Niedziałająca kamera'),
        ('niedzialajac_dvr', 'Niedziałający DVR'),
        ('niepoprawne_podlaczenie_przewodow' ,'Niepoprawne podłączenie '
                                            'przewodów'),
        ('niezabezpieczony_przewod', 'Niezabezpieczony przewód'),
        ('opilki_w_skrytkach', 'Opiłki w skrytkach'),
        ('pozostawione_el_zlaczne', 'Pozostawione elementy złączne'),
        ('uszkodzenia_pow_lakierniczej', 'Uszkodzenia powierzchni '
                                         'lakierniczej'),
        ('uszkodzona_polka', 'Uszkodzona półka'),
        ('uszkodzone_drzwiczki', 'Uszkodzone drzwiczki'),
        ('uszkodzony_felc', 'Uszkodzony felc'),
        ('uszkodzony_przewod', 'Uszkodzony przewód'),
        ('wadliwa_sciana_modulu', 'Wadliwa ściana modułu'),
        ('wystajace_nity', 'Wystające nity'),
)


# Numer ID paczkomatu
class ParcelMachine(models.Model):
    serial_number = models.CharField(max_length=12)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    #status - czy paczkomat zostal sprawdzony

    class Meta:
        verbose_name_plural = 'Paczkomat'

    def __str__(self):
        return self.serial_number


# Numer ID pracownika
class Worker(models.Model):
    parcel_machine = models.ForeignKey(ParcelMachine,
                                       on_delete=models.CASCADE)
    qc = models.CharField(max_length=3) #indywidualny kod pracowanika
    error_list = MultiSelectField(choices=ERROR_LIST)
    other_error = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name_plural = 'Pracownik'

    def __str__(self):
        return f'QC{self.qc}'

