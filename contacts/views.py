from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.


def contact(request):
  if request.method == 'POST':
    house_id = request.POST['house_id']
    house = request.POST['house']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    salesPerson_email = request.POST['salesPerson_email']

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(house_id=house_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this house')
        return redirect('/houses/'+house_id)

    contact = Contact(house=house, house_id=house_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    # send_mail(
    #   'Property house Inquiry',
    #   'There has been an inquiry for ' + house + '. Sign into the admin panel for more info',
    #   'aketchoyugi.brad@gmail.com',
    #   [salesPerson_email, 'godfreyoyugi@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/houses/'+house_id)

