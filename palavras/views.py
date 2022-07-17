from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Palavra
from .forms import PalavraNovaForm



# Create your views here.
def home(request):
    if request.method == 'POST':
        form = PalavraNovaForm(request.POST)
        if form.is_valid():
            form.save()
            #  Se o formulário for válido, volta pra pagina index.html
            return HttpResponseRedirect(reverse('palavras:home'))
        else:
            palavras = Palavra.objects.all()
            return render(
                request, 
                'palavras/home.html', 
                {
                    'form': form,
                    'palavras': palavras,
                },status=400
            )
    
    palavras = Palavra.objects.all()
    return render(request, 'palavras/home.html', {'palavras': palavras})

