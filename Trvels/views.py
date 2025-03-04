from django.shortcuts import render,redirect,get_object_or_404
from .forms import ContactForm
from .models import Location,Inquiry
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection


def get_data(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM your_table")
        rows = cursor.fetchall()
    
    # Return the data as JSON response
    return JsonResponse({'data': rows})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

        
            subject = contact.subject
            message = f"Name: {contact.name}\nEmail: {contact.email}\nMessage: {contact.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.CONTACT_EMAIL]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)

            return redirect('contact')  # Use the name of the URL pattern
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def home(request):
    locations = Location.objects.all()  # Fetch all locations
    return render(request, 'index.html', {'locations': locations})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def career(request):
    return render(request, 'career.html')

def location(request, id):
  location = Location.objects.get(id=id)  # Fetch the specific location by ID
  return render(request, 'loc.html', {'location': location})

def inquiry_form(request):
    return render(request, 'inquiry.html')

def submit_inquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_no = request.POST.get('contact_no')
        place = request.POST.get('place')
        persons = request.POST.get('persons')
        departure_date = request.POST.get('departure_date')
        return_date = request.POST.get('return_date')
        transportation = request.POST.get('transportation')


        inquiry = Inquiry(
            name=name,
            email=email,
            contact_number=contact_no,
            place=place,
            number_of_persons=persons,
            departure_date=departure_date,
            return_date=return_date,
            transportation_method=transportation
        )
        inquiry.save() 

        recipient_email = 'gohilpratishtha57@gmail.com'  

        # Send email
        send_mail(
            subject=f'New Inquiry from {name}',
            message=(
                "Hello,\n\n"
                "You have received a new inquiry. Here are the details:\n\n"
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Contact No: {contact_no}\n'
                f'Place: {place}\n'
                f'Number of Persons: {persons}\n'
                f'Departure Date: {departure_date}\n'
                f'Return Date: {return_date}\n'
                f'Transportation: {transportation}\n\n'
                "Please reach out to the customer as soon as possible to confirm the inquiry and provide further details.\n\n"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            fail_silently=False,
        )

        # Render a success page or show a success message
        return render(request, 'submit_inquiry.html')

    else:
        return redirect('inquiry_form')

def plantrip(request):
    return render(request, 'plantrip.html')

def adventure(request):
    return render(request, 'explore/adventure.html')

def spiritual(request):
    return render(request, 'explore/spiritual.html')

def mountains(request):
    return render(request, 'explore/mountains.html')

def heritage(request):
    return render(request, 'explore/heritage.html')

def honeymoon(request):
    return render(request, 'explore/honeymoon.html')

def weekend(request):
    return render(request, 'explore/weekend.html')

def romantic(request):
    return render(request, 'explore/romantic.html')

def pilgrimage(request):
    return render(request, 'explore/pilgrimage.html')

def foodie(request):
    return render(request, 'explore/foodie.html')

def trekking(request):
    return render(request, 'explore/trekking.html')

def relax(request):
    return render(request, 'explore/relax.html')

def international(request):
    return render(request, 'explore/international.html')

def login_view(request):
    return render(request, "login.html")