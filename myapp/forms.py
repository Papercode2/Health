from django import forms
from .models import ContactFormSubmission,AppointmentFormSubmission
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Payment


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ['name', 'email', 'message']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model= AppointmentFormSubmission
        fields=['full_name','email','phone','department','appointment_date','appointment_time']



class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text="Required. Enter a valid email address.")
    phone = forms.CharField(max_length=15, required=False, help_text="Optional. Enter your phone number.")

    class Meta:
        model = User
        fields = ('username', 'email', 'phone', 'password1', 'password2')



class LoginForm(AuthenticationForm):
    class Meta:
        model = User

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['phone_number', 'amount']