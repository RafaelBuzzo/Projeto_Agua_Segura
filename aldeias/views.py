from django.shortcuts import render, redirect
from .models import Aldeia
from .forms import AldeiaForm


def lista_aldeias(request):

    aldeias = Aldeia.objects.all()

    return render(
        request,
        'aldeias/lista.html',
        {'aldeias': aldeias}
    )


def nova_aldeia(request):

    if request.method == 'POST':

        form = AldeiaForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('aldeias')

    else:

        form = AldeiaForm()

    return render(
        request,
        'aldeias/form.html',
        {'form': form}
    )