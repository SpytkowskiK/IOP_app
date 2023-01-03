import datetime
from pyexpat import model
from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


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
    date_added = models.DateTimeField(auto_now_add=True)
    parcel_machine = models.ForeignKey(ParcelMachine,
                                       on_delete=models.CASCADE)
    qc = models.CharField(max_length=3) #indywidualny kod pracowanika
    brak_ceownika = models.IntegerField(null=True, blank=True, default=None)
    brak_elementow_zlacznych = models.IntegerField(null=True, blank=True, default=None)
    brak_markera = models.IntegerField(null=True, blank=True, default=None)
    brak_nagran_z_kamer = models.IntegerField(null=True, blank=True, default=None)
    brak_naklejek_zs = models.IntegerField(null=True, blank=True, default=None)
    brak_nitow = models.IntegerField(null=True, blank=True, default=None)
    brak_obrazu = models.IntegerField(null=True, blank=True, default=None)
    brak_odbojnikow = models.IntegerField(null=True, blank=True, default=None)
    brak_pieczatki_qc = models.IntegerField(null=True, blank=True, default=None)
    brak_przepustu_kablowego = models.IntegerField(null=True, blank=True, default=None)
    brak_segerow = models.IntegerField(null=True, blank=True, default=None)
    brak_uchwytu_przewodow = models.IntegerField(null=True, blank=True, default=None)
    brak_uszczelki = models.IntegerField(null=True, blank=True, default=None)
    brak_zaslepki_dachowej = models.IntegerField(null=True, blank=True, default=None)
    brak_zlacza_gpd = models.IntegerField(null=True, blank=True, default=None)
    drzwiczki_do_regulacji = models.IntegerField(null=True, blank=True, default=None)
    niedokrecona_krancowka = models.IntegerField(null=True, blank=True, default=None)
    niedokrecona_nakretka_drzwiczek = models.IntegerField(null=True, blank=True, default=None)
    niedokrecona_sruba = models.IntegerField(null=True, blank=True, default=None)
    niedokrecony_przewod = models.IntegerField(null=True, blank=True, default=None)
    niedokrecone_uziemienie = models.IntegerField(null=True, blank=True, default=None)
    niedokrecony_zawias_drzwiczek = models.IntegerField(null=True, blank=True, default=None)
    niedzialajaca_kamera = models.IntegerField(null=True, blank=True, default=None)
    niedzialajac_dvr = models.IntegerField(null=True, blank=True, default=None)
    niepoprawne_podlaczenie_przewodow = models.IntegerField(null=True, blank=True, default=None)
    niezabezpieczony_przewod = models.IntegerField(null=True, blank=True, default=None)
    opilki_w_skrytkach = models.IntegerField(null=True, blank=True, default=None)
    pozostawione_el_zlaczne = models.IntegerField(null=True, blank=True, default=None)
    uszkodzenia_pow_lakierniczej = models.IntegerField(null=True, blank=True, default=None)
    uszkodzona_polka = models.IntegerField(null=True, blank=True, default=None)
    uszkodzone_drzwiczki = models.IntegerField(null=True, blank=True, default=None)
    uszkodzony_felc = models.IntegerField(null=True, blank=True, default=None)
    uszkodzony_przewod = models.IntegerField(null=True, blank=True, default=None)
    wadliwa_sciana_modulu = models.IntegerField(null=True, blank=True, default=None)
    wystajace_nity = models.IntegerField(null=True, blank=True, default=None)
    other_error = models.CharField(null=True, blank=True, max_length=50)

    class Meta:
        verbose_name_plural = 'Pracownik'

    def __str__(self):
        return f'QC{self.qc}'

    def get_fields(self):
        values = []
        for field in Worker._meta.fields:
            if field.value_to_string(self):
                values.append(str(field.name) + ": " + field.value_to_string(self))
        return values
