from django.shortcuts import render
from app_ticket.models import Person
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from .forms import PersonForm
from .models import Person
# Create your views here.

@csrf_protect
def homepage(request):
    if request.method == 'GET':
        return render(request, "homepage.html")
    else:
        p = Person()
        print(request.POST)
        body_dec = request.POST
        p.email_address = body_dec.get('email_address')
        p.first_name = body_dec.get('first_name')
        p.message = body_dec.get('message')
        p.checkbox = body_dec.get(' checkbox')
        p.save()
        return HttpResponse('')

def person_create_view(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request,"response.html", context)


    