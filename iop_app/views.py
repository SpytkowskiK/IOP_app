from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import xlwt
import datetime
from datetime import datetime


from .models import ParcelMachine, Worker
from .forms import ParcelMachineForm, WorkerForm


@login_required
def index(request):
    """Strona główna aplikacji IOP"""
    return render(request, 'iop_app/index.html')


@login_required
def parcel_machines(request):
    """Wyświetlenie listy paczkomatów z obecnego dnia"""
    parcel_machines = ParcelMachine.objects.filter(
            date_added__year=datetime.now().year,
            date_added__month=datetime.now().month,
            date_added__day=datetime.now().day)

    context = {'parcel_machines': parcel_machines}
    return render(request, 'iop_app/parcel_machines.html', context)


@login_required
def parcel_machines_all(request):
    """Wyświetlnie historii paczkomatów"""

    parcel_machines = ParcelMachine.objects.all()

    context = {'parcel_machines': parcel_machines}

    return render(request, 'iop_app/parcel_machines_all.html', context)

@login_required
def parcel_machine_details(request, parcel_machine_id):
    """Wyświetlenie szczegółów paczkomatu"""

    parcel_machine = ParcelMachine.objects.get(id=parcel_machine_id)
    workers = parcel_machine.worker_set.order_by('qc')
    error_instances = Worker.objects.filter(
            parcel_machine__id=parcel_machine_id)
    error_list_all = []
    error_values_not_null = []
    sum_of_errors = 0

    for error_instance in error_instances:
        error_list_all.append(error_instance.brak_ceownika)
        error_list_all.append(error_instance.brak_elementow_zlacznych)
        error_list_all.append(error_instance.brak_markera)
        error_list_all.append(error_instance.brak_nagran_z_kamer)
        error_list_all.append(error_instance.brak_naklejek_zs)
        error_list_all.append(error_instance.brak_nitow)
        error_list_all.append(error_instance.brak_obrazu)
        error_list_all.append(error_instance.brak_odbojnikow)
        error_list_all.append(error_instance.brak_pieczatki_qc)
        error_list_all.append(error_instance.brak_przepustu_kablowego)
        error_list_all.append(error_instance.brak_segerow)
        error_list_all.append(error_instance.brak_uchwytu_przewodow)
        error_list_all.append(error_instance.brak_uszczelki)
        error_list_all.append(error_instance.brak_zaslepki_dachowej)
        error_list_all.append(error_instance.brak_zlacza_gpd)
        error_list_all.append(error_instance.drzwiczki_do_regulacji)
        error_list_all.append(error_instance.niedokrecona_krancowka)
        error_list_all.append(error_instance.niedokrecona_nakretka_drzwiczek)
        error_list_all.append(error_instance.niedokrecona_sruba)
        error_list_all.append(error_instance.niedokrecone_uziemienie)
        error_list_all.append(error_instance.niedokrecony_przewod)
        error_list_all.append(error_instance.niedokrecony_zawias_drzwiczek)
        error_list_all.append(error_instance.niedzialajac_dvr)
        error_list_all.append(error_instance.niedzialajaca_kamera)
        error_list_all.append(error_instance.niepoprawne_podlaczenie_przewodow)
        error_list_all.append(error_instance.niezabezpieczony_przewod)
        error_list_all.append(error_instance.opilki_w_skrytkach)
        error_list_all.append(error_instance.pozostawione_el_zlaczne)
        error_list_all.append(error_instance.uszkodzenia_pow_lakierniczej)
        error_list_all.append(error_instance.uszkodzona_polka)
        error_list_all.append(error_instance.uszkodzone_drzwiczki)
        error_list_all.append(error_instance.uszkodzony_felc)
        error_list_all.append(error_instance.uszkodzony_przewod)
        error_list_all.append(error_instance.wadliwa_sciana_modulu)
        error_list_all.append(error_instance.wystajace_nity)
    for error in error_list_all:
        if error != None:
            error_values_not_null.append(error)

    for error in error_values_not_null:
        sum_of_errors += error

    parcel_machine.sum_of_errors = sum_of_errors
    parcel_machine.save()

    context = {'parcel_machine': parcel_machine, 'workers': workers,
               'sum_of_errors': sum_of_errors}
    return render(request, 'iop_app/parcel_machine_details.html', context)


@login_required
def create_parcel_machine(request):
    """Utworzenie nowego paczkomatu w bazie danych"""

    if 'add' in request.POST:
        form = ParcelMachineForm(data=request.POST)
        if form.is_valid():
            paczkomat = form.save(commit=False)
            paczkomat.user = request.user
            paczkomat.save()
        return redirect('iop_app:parcel_machines')
    else:
        form = ParcelMachineForm()

    context = {'form': form}
    return render(request, 'iop_app/create_parcel_machine.html', context)


@login_required
def create_worker(request, parcel_machine_id):
    """Utworzenie workera w bazie danych"""
    parcel_machine = ParcelMachine.objects.get(id=parcel_machine_id)

    if 'add' in request.POST:
        form = WorkerForm(data=request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.parcel_machine = parcel_machine
            worker.user = request.user
            worker.save()
            return redirect('iop_app:parcel_machine_details',
                            parcel_machine_id=parcel_machine_id)
    else:
        form = WorkerForm()

    context = {'form': form, 'parcel_machine': parcel_machine}
    return render(request, 'iop_app/create_worker.html', context)


@login_required
def worker_details(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    error_instances = Worker.objects.values().filter(id=worker_id)
    parcel_machine = worker.parcel_machine
    error_list_names = []
    error_list_values = []

    error_values_not_null = []
    sum_of_errors = 0

    names = Worker._meta.fields
    for name in names[4:]:
        error_list_names.append(name.verbose_name)

    for error_instance in error_instances:
        for error_value in error_instance.values():
            error_list_values.append(error_value)

    error_list_number = error_list_values[4:]
    errors = zip(error_list_names, error_list_number)

    for error in error_list_number:
        if error != None:
            error_values_not_null.append(error)

    for error in error_values_not_null:
        sum_of_errors += error

    context = {'worker': worker, 'error_list_names': error_list_names,
               'sum_of_errors': sum_of_errors, 'error_list_number':
                   error_list_number, 'errors': errors, 'parcel_machine':
                   parcel_machine}
    return render(request, 'iop_app/worker_details.html', context)


@login_required
def edit_worker(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    parcel_machine = worker.parcel_machine

    if 'add' in request.POST:
        form = WorkerForm(instance=worker, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('iop_app:worker_details',
                            worker_id=worker.id)
    else:
        form = WorkerForm(instance=worker)

    context = {'worker': worker, 'parcel_machine': parcel_machine, 'form': form}
    return render(request, 'iop_app/edit_worker.html', context)


@login_required
def delete_worker(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    parcel_machine = worker.parcel_machine

    if "delete" in request.POST:
        parcel_machine_id = parcel_machine.id
        worker.delete()
        return redirect('/parcel_machines/')

    context = {'worker': worker, 'parcel_machine': parcel_machine}
    return render(request, "iop_app/delete_worker.html", context)


@login_required
def delete_parcel_machine(request, parcel_machine_id):
    parcel_machine = ParcelMachine.objects.get(id=parcel_machine_id)

    if "delete" in request.POST:
        parcel_machine.delete()
        return redirect('/parcel_machines/')

    context = {'parcel_machine': parcel_machine}
    return render(request, "iop_app/delete_parcel_machine.html", context)


@login_required
def delete_history(request):
    parcel_machine = ParcelMachine.objects.all()

    if 'delete' in request.POST:
        parcel_machine.delete()
        return redirect('/parcel_machines/')

    context = {'parcel_machine': parcel_machine}
    return render(request, "iop_app/delete_history.html", context)


@login_required
def download_xlsx(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=Raport'  \
                                      f'{datetime.today()}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet(
            'Raport KJ')  # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Data dodania', 'Dodał', 'Numer Seryjny', 'Suma błędów',
               'Notatka']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num],
                 font_style)  # at 0 row 0 column

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()


    parcel_machine = ParcelMachine.objects.filter(
         date_added__year=datetime.now().year,
         date_added__month=datetime.now().month,
         date_added__day=datetime.now().day).order_by('date_added')

    print(parcel_machine)

    values_list_all = []

    for value in parcel_machine:
        list_items = [value.date_added.strftime('%x %X'), value.user.username,
                      value.serial_number, value.sum_of_errors, value.description]

        values_list_all.append(list_items)

    for row in values_list_all:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response
