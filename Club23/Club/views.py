from django.shortcuts import render, redirect
from .forms import Bookclub_from
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from .models import News

# Create your views here.
def Home(request):
    temp ="index.html"
    return render(request, temp)

@login_required
def Bookclub_view(request):
    temp = "BookClub.html"
    if request.method == 'POST':
        print("In post")
        form = Bookclub_from(request.POST or None)

        print(request.POST.get('email'))
        if form.is_valid():
            email = request.POST.get('email')
            print("Form valid")
            venu = request.POST.get('Venu')
            print(venu)
            occasion = request.POST.get('Occasion')
            person = request.POST.get('PERSON')
            price = request.POST.get('PRICE')
            booking_form = form.save(commit=False)
            booking_form.email = email
            booking_form.Occasion = occasion
            booking_form.Price = price
            booking_form.person = person
            p = booking_form.Venu.split("|")
            subject = "Club23"
            message = "Hello, " + request.user.username + ". Welcome To Club23. Your booking date" + request.POST.get(
                'Date_from') + " on " + request.POST.get('Time_from') + " at club23 " + p[
                          0] + " . Your venu price for one day is " + price + "rs."
            email_from = settings.EMAIL_HOST_USER
            email_to = [email, ]
            send_mail(subject, message, email_from, email_to)

            v = p[0],

            request.session["v"] = v
            request.session["p"] = price

            booking_form.save()
            return redirect('Club:checkout')  # need to complete
    else:
        form = Bookclub_from()
    return render(request,temp, {'BookClub_from':form})

def Gallery(request):
    temp = "gallery.html"
    return render(request, temp)

def Person_grid(request):
    temp = "person_grid.html"
    return render(request, temp)

def Contact_us(request):
    temp = "contact_us.html"
    return render(request,temp)

def checkout(request, **kwargs):
    return render(request, 'checkout.html')

def faq(request):
    return render(request, 'faq.html')

def birthdate(request):
    return render(request, 'birthdate.html')

def marriage(request):
    return render(request, 'marriage.html')

def farewell(request):
    return render(request, 'farewell.html')

def reception(request):
    return render(request, 'reception.html')

def party(request):
    return render(request, 'party.html')

def wedding(request):
    return render(request, 'wedding.html')

def all_news(request):
    data = News.objects.all()
    return render(request, 'all_news.html', {'data':data})
