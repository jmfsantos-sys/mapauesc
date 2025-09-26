from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm
from .models import Portfolio  # importa o modelo Portfolio

def index(request):
    return render(request, 'core/index.html')

def portfolio_details(request):
    return render(request, 'core/portfolio-details.html')


def starter(request):
    return render(request, 'core/starter-page.html')

def service_details(request):
    return render(request, 'core/service-details.html')

def portfolio_details(request, id):
    # Exemplo basico de portifolio
    return render(request, 'core/portfolio-details.html', {'id': id})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            full_message = f"De: {name} <{email}>\n\n{message}"
            
            try:
                send_mail(
                    subject=subject,
                    message=full_message,
                    from_email=email,
                    recipient_list=['seuemail@dominio.com'],
                )
            except BadHeaderError:
                return HttpResponse('Erro no cabecalho do email.')
            
            return redirect('contact_success')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'core/contact-success.html')
