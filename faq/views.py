from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Faqs
# Create your views here.

def faqs(request):
    if (request.method == 'POST'):
        email = request.POST['email']
        query = request.POST['query']
        k = Faqs(email=email, query=query + '?')
        k.save()
        if request.user.is_staff: return redirect('faqs2')
        elif request.user.is_active: return redirect('faqs1')
        else : return redirect('faqs')
    elif request.user.is_staff:
        l = Faqs.objects.all()
        return render(request, 'faqs2.html', {'Q': l})
    elif request.user.is_active:
        l = Faqs.objects.all()
        return render(request, 'faqs.html', {'Q': l})
    else:
        l = Faqs.objects.all()
        return render(request, 'faqs1.html', {'Q': l})


