from django.shortcuts import render

# Create your views here.
def imagem(request):
    return render(request, 'gallery/index.html')
def index(request):
    return render(request, 'gallery/imagem.html')

