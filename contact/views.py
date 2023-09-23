from django.shortcuts import render
from .models import Contact
from .forms import ContactForm



def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'contact/thank_you.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact_page.html', {'form': form})
