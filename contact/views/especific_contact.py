from django.shortcuts import render, get_object_or_404
from contact.models import Contact

# Create your views here.
def select_contact(request,contact_id):

    contact = Contact.objects.filter(pk=contact_id).filter(show=True).first()

    clicked_contact = get_object_or_404(
        Contact,
        pk=contact_id,
        show=True

    )

    contact_name = f'{clicked_contact.first_name} {clicked_contact.last_name} - '


    context = {

        'contact': contact,
        'page_context': contact_name
    }

    return render(

        request,
        'contact/contact.html',
        context
        
    )