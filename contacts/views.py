from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.

# The import statements include necessary modules and classes for the code to work.


def contact(request):
  """
    A view function that handles the contact form submission.

    Arguments:
    - request: The HTTP request object.

    Returns:
    - If the request method is POST:
        - If the user has already made an inquiry for the house, redirects to the house details page with an error message.
        - If the user has not made a previous inquiry, saves the contact information, displays a success message, and redirects to the house details page.
    - If the request method is not POST, renders the contact form template.
    """
  if request.method == 'POST':

    # If the request method is POST, indicating a form submission.

    # Extract form data from the request object.
    house_id = request.POST['house_id']
    house = request.POST['house']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    salesPerson_email = request.POST['salesPerson_email']

    
    if request.user.is_authenticated:
      # If the user is authenticated (logged in).

      # Check if the user has already made an inquiry for the house.

      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(house_id=house_id, user_id=user_id)
      if has_contacted:

      # If the user has already made an inquiry, display an error message and redirect to the house details page.

        messages.error(request, 'You have already made an inquiry for this house')
        return redirect('/houses/'+house_id)

      # Create a new Contact object with the extracted form data.
    contact = Contact(house=house, house_id=house_id, name=name, email=email, phone=phone, message=message, user_id=user_id )
      # Save the contact information to the database.
    contact.save()

    # Send email
    # send_mail(
    #   'Property house Inquiry',
    #   'There has been an inquiry for ' + house + '. Sign into the admin panel for more info',
    #   'aketchoyugi@gmail.com',
    #   [salesPerson_email, 'godfreyoyugi@gmail.com'],
    #   fail_silently=False
    # )

    messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')
    return redirect('/houses/'+house_id)

