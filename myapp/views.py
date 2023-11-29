from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import ContactForm,AppointmentForm,CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.shortcuts import render
from django.contrib import messages
from .models import Payment
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django_daraja.mpesa.core import MpesaClient
from django_daraja.models import AccessToken
from django.contrib.auth.decorators import login_required




from myapp.models import AppointmentFormSubmission  # Replace your_app and YourModel with your actual app and model names











# Create your views here.
def index(request):
    return render(request, 'index.html')


def adminstrator(request):
    return render(request, 'adminstrator.html')
def doctors(request):
    user = "example@example.com" 
    return render(request, 'doctors.html', {'user': user})


from django.shortcuts import render
from .models import AppointmentFormSubmission

def bookings(request):
    submissions = AppointmentFormSubmission.objects.all()
    return render(request, 'bookings.html', {'submissions': submissions})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render
@login_required
def home(request):
    return render(request,'home.html')
    

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def settings(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If UserProfile doesn't exist, create a new one
        user_profile = UserProfile.objects.create(user=request.user)

    context = {'user_profile': user_profile}
    return render(request, 'settings.html', context)
def save_profile(request):
    # Your implementation to handle saving profile data goes here
    return render(request, 'settings.html')

def sessions(request):
    return render(request, "sessions.html")

def login(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
            
                return redirect('/admin/')
            else:
                return redirect('home')
        else:
            messages.info(request, 'username OR password is incorrect')
            
    context={}    
    return render(request, 'login.html',context)

def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account was created successfully for' + user)
            return redirect('login')
    context={'form':form}
    return render(request, 'register.html', context)




def home(request):
    user = request.user
    user_display_name = "Custom Display Name"  # Replace this with your logic to get or calculate the display name
    context = {'user': user, 'user_display_name': user_display_name}
    return render(request, 'home.html', context)

def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' successfully sent.')
            return redirect('home')
    else:
        form = AppointmentForm()
    return render(request, 'appointment.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ' successfully sent.')
        
            return redirect('home') 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def about(request):
    return render(request, "about.html")

def success(request):
    return render(request, 'success.html')

def pay(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        amount_str = request.POST.get('amount') 
        try:
            
            
            amount = int(amount_str)
        except ValueError:
            return HttpResponse("Invalid amount. Amount must be a valid integer.")

        account_reference = 'reference'
        transaction_desc = 'Description'  
        callback_url = 'https://your-callback-url.com'  
        cl = MpesaClient()

        try:
            access_tokens = AccessToken.objects.all()
            response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
            
            messages.success(request, 'Thank you !!! Payment made successfully.')
            return render(request, 'success.html', {'access_tokens': access_tokens})
        except Exception as e:
            return HttpResponse("Error: Check your internet connection")

    else:
        return render(request, "pay.html")
    
def download_receipt(request, access_token_id):
    try:
        access_token = AccessToken.objects.latest('id')
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="receipt_{access_token.id}.pdf"'
        p = canvas.Canvas(response, pagesize=letter)
        p.drawString(100, 750, f"Payment Token ID :{access_token.id}")
        p.drawString(100, 730, f"Payment Token Amount :{access_token.token}")
        p.drawString(100, 710, f"Payment Token Datetime :{access_token.created_at}")
        p.showPage()
        p.save()
        return response
    except Exception:
        return HttpResponse('Payment not found', status=404)


def stk_push_callback(request):
        data = request.body
        
        return HttpResponse("STK Push in Django👋")

def approval(request):
    return render(request, 'approval.html')

def logout(request):
    return render(request, "index.html")