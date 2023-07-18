from django.shortcuts import render, redirect
from .models import DeliverMassage, EditInformation
from .forms import ContactUsForm
from django.views.generic import ListView, FormView, CreateView, View
from django.urls import reverse_lazy



def contact_us(request):
    """این یک فانکشن بیس ویو است که فقط جنبه آموزشی دارد"""
    if request.method == "POST":
        forms = ContactUsForm(request.POST)
        if forms.is_valid():
            forms.save()

    else:
        forms = ContactUsForm()

    edit_informations = EditInformation.objects.all()

    return render(request, "contact_app/contact.html", {'forms': forms, "informations": edit_informations})


class ContactUsView(FormView):
    template_name = 'contact_app/contact.html'
    form_class = ContactUsForm
    success_url = '/contact/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informations'] = EditInformation.objects.all()
        context['forms'] = self.form_class
        return context



























