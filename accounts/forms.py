from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import User
from restaurants.models import Restaurant


class RegisterForm(UserCreationForm):
    """Restaurant registration form"""
    
    restaurant_name = forms.CharField(
        max_length=255,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your restaurant name',
            'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
        })
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
        })
    )
    
    phone = forms.CharField(
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '+1234567890',
            'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
        })
    )
    
    address = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'placeholder': 'Full restaurant address',
            'rows': 2,
            'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all resize-none'
        })
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Minimum 8 characters',
            'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
        })
    )
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm password',
            'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
        })
    )
    
    class Meta:
        model = User
        fields = ['email', 'phone', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Use email as username
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.role = User.ROLE_RESTAURANT_ADMIN
        
        if commit:
            user.save()
            # Create restaurant profile
            Restaurant.objects.create(
                owner=user,
                name=self.cleaned_data['restaurant_name'],
                email=self.cleaned_data['email'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address']
            )
        
        return user


class LoginForm(forms.Form):
    """User login form"""
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
        })
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your password',
            'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        if email and password:
            # Try to get user by email
            try:
                user = User.objects.get(email=email)
                # Authenticate using username (which is email)
                self.user = authenticate(username=user.username, password=password)
                if self.user is None:
                    raise forms.ValidationError('Invalid email or password.')
            except User.DoesNotExist:
                raise forms.ValidationError('Invalid email or password.')
        
        return cleaned_data
    
    def get_user(self):
        return getattr(self, 'user', None)
