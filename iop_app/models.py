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
    sum_of_errors = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        verbose_name_plural = 'Paczkomat'

    def __str__(self):
        return self.serial_number


# Numer ID pracownika
class Worker(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    parcel_machine = models.ForeignKey(ParcelMachine,
                                       on_delete=models.CASCADE)
    qc = models.CharField(max_length=3, verbose_name="QC") #indywidualny kod
    # pracowanika
    brak_ceownika = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Ceownika")
    brak_elementow_zlacznych = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Elementów Złącznych")
    brak_markera = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Markera")
    brak_nagran_z_kamer = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Nagrań Z Kamer")
    brak_naklejek_zs = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Nakelejek ZS")
    brak_nitow = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Nitów")
    brak_obrazu = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Obrazu")
    brak_odbojnikow = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Odbojników")
    brak_pieczatki_qc = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Pieczątki QC")
    brak_przepustu_kablowego = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Przepustu Kablowego")
    brak_segerow = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Segerów")
    brak_uchwytu_przewodow = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Uchwytu Przewodów")
    brak_uszczelki = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Uszczelki")
    brak_zaslepki_dachowej = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Zaślepki Dachowej")
    brak_zlacza_gpd = models.IntegerField(null=True, blank=True,
                                        verbose_name="Brak Złącza GPD")
    drzwiczki_do_regulacji = models.IntegerField(null=True, blank=True,
                                        verbose_name="Drzwiczki Do Regulacji")
    niedokrecona_krancowka = models.IntegerField(null=True, blank=True,
                                        verbose_name="Niedokręcona Krańcówka")
    niedokrecona_nakretka_drzwiczek = models.IntegerField(null=True,
                                                          blank=True,
                                        verbose_name="Niedokręcona Nakrętka "
                                                     "Drzwiczek")
    niedokrecona_sruba = models.IntegerField(null=True, blank=True,
                                        verbose_name="Niedokręcona Śruba")
    niedokrecony_przewod = models.IntegerField(null=True, blank=True,
                                        verbose_name="Niedokręcony Przewód")
    niedokrecone_uziemienie = models.IntegerField(null=True, blank=True,
                                        verbose_name="Niedokręcone Uziemienie")
    niedokrecony_zawias_drzwiczek = models.IntegerField(null=True,
                                                        blank=True,
                                        verbose_name="Niedokręcony Zawias "
                                                     "Drzwiczek")
    niedzialajaca_kamera = models.IntegerField(null=True, blank=True,
                                        verbose_name="Niedziałająca Kamer")
    niedzialajac_dvr = models.IntegerField(null=True, blank=True,
                                        verbose_name="Niedziałający DVR")
    niepoprawne_podlaczenie_przewodow = models.IntegerField(null=True,
                                                            blank=True,
                               verbose_name="Niepoprawne Podłączenie "
                                             "Przewodów")
    niezabezpieczony_przewod = models.IntegerField(null=True, blank=True,
                                        verbose_name="Niezabezpieczony Przewód")
    opilki_w_skrytkach = models.IntegerField(null=True, blank=True,
                                        verbose_name="Opiłki W Skrytkach")
    pozostawione_el_zlaczne = models.IntegerField(null=True, blank=True,
                                        verbose_name="Pozowstawione Elementy "
                                                     "Złączne")
    uszkodzenia_pow_lakierniczej = models.IntegerField(null=True, blank=True,
                                        verbose_name="Uszkodzenia Powłoki "
                                                     "Lakierniczej")
    uszkodzona_polka = models.IntegerField(null=True, blank=True,
                                        verbose_name="Uszkodzona Półka")
    uszkodzone_drzwiczki = models.IntegerField(null=True, blank=True,
                                        verbose_name="Uszkodzone Drzwiczki")
    uszkodzony_felc = models.IntegerField(null=True, blank=True,
                                        verbose_name="Uszkodzony Felc")
    uszkodzony_przewod = models.IntegerField(null=True, blank=True,
                                        verbose_name="Uszkodzony Przewód")
    wadliwa_sciana_modulu = models.IntegerField(null=True, blank=True,
                                        verbose_name="Wadliwa Ściana Modułu")
    wystajace_nity = models.IntegerField(null=True, blank=True,
                                        verbose_name="Wystające Nity")

    class Meta:
        verbose_name_plural = 'Pracownik'

    def __str__(self):
        return f'QC{self.qc}'

    def get_fields(self):
        values = []
        for field in Worker._meta.fields:
            if field.value_to_string(self):
                values.append(str(field.name) + ": " +
                              field.value_to_string(self))
        return values
