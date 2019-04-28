from django.shortcuts import render
from django import forms
from django.contrib.auth import get_user_model
from django.http import JsonResponse,HttpResponse
from .models import Query
from .forms import ContactForm
User = get_user_model()



# Create your views here.
def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact",
        "content":" Welcome to the contact page.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        c=Query()
        c.content=contact_form.cleaned_data['content']
        c.email=contact_form.cleaned_data['email']
        c.fullname=contact_form.cleaned_data['fullname']
        c.save()

        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)

