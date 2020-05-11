from django.shortcuts import render, reverse, HttpResponseRedirect
from subprocess import check_output
from cowsay.form import AddCowsay
from cowsay.models import Cowsay

# Create your views here.
def singlecowsay(request):
    html = 'index.html'
    if request.method == 'POST':
        form = AddCowsay(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            viewCowsay = check_output(
                ['cowsay', str(data['text'])]
            )
            viewCowsay = viewCowsay.decode('utf-8')
            newCowsay = Cowsay.objects.create(
                text=data['text'],
                cowsay=viewCowsay
            )
            return render(request, html, {'form':form, 'newCowsay': newCowsay})
    form = AddCowsay()
    return render(request, html, {'form': form})

def topcowsay(request):
    html = 'history.html'
    data = Cowsay.objects.order_by('-id')[:10]
    return render(request,html,{'data' : data})