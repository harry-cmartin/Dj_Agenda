from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from contact.models import Contact

def search(request: HttpRequest) -> HttpResponse:

    search_value: str = request.GET.get('q','').strip()

    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.filter(show=True).order_by('-id')

    context = {
        'contacts': contacts,
        'page_context': 'search - '
    }

    return render(
        request,
        'contact/index.html',
        context

    )