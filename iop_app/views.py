from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ParcelMachine, Worker
from .forms import ParcelMachineForm, WorkerForm


def index(request):
    """Strona główna aplikacji IOP"""
    return render(request, 'iop_app/index.html')


def parcel_machines(request):
    """Wyświetlenie listy paczkomatów"""
    parcel_machines = ParcelMachine.objects.all()
    context = {'parcel_machines': parcel_machines}
    return render(request, 'iop_app/parcel_machines.html', context)


def parcel_machine_details(request, parcel_machine_id):
    """Wyświetlenie szczegółów paczkomatu"""

    parcel_machine = ParcelMachine.objects.get(id=parcel_machine_id)
    workers = parcel_machine.worker_set.order_by('qc')

    context = {'parcel_machine': parcel_machine, 'workers': workers}
    return render(request, 'iop_app/parcel_machine_details.html', context)


def create_parcel_machine(request):
    """Utworzenie nowego paczkomatu w bazie danych"""
    if request.method == 'POST':
        form = ParcelMachineForm(data=request.POST)
        if form.is_valid():
            paczkomat = form.save(commit=False)
            paczkomat.user = request.user
            paczkomat.save()
        return redirect('/parcel_machines/')
    else:
        form = ParcelMachineForm()

    context = {'form': form}
    return render(request, 'iop_app/create_parcel_machine.html', context)


def create_worker(request):
    """Utworzenie workera w bazie danych"""
    if request.method == 'POST':
        form = WorkerForm(data=request.POST)
        if form.is_valid():
            worker = form.save(commit=False)
            worker.user = request.user
            worker.save()
        return redirect('/parcel_machines/')
    else:
        form = WorkerForm()

    context = {'form': form}
    return render(request, 'iop_app/create_worker.html', context)


def worker_details(request, worker_id):
    worker = Worker.objects.get(id=worker_id)

    context = {'worker': worker}
    return render(request, 'iop_app/worker_details.html', context)
