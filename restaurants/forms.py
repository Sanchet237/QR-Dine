from django import forms
from .models import Restaurant, Category, MenuItem


class RestaurantProfileForm(forms.ModelForm):
    """Form for editing restaurant profile"""

    ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/webp', 'image/gif']
    MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB

    class Meta:
        model = Restaurant
        fields = ['name', 'email', 'phone', 'address', 'description', 'logo']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
            }),
            'address': forms.Textarea(attrs={
                'rows': 2,
                'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all resize-none'
            }),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Brief description of your restaurant, cuisine, ambiance…',
                'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all resize-none'
            }),
        }

    def clean_logo(self):
        logo = self.cleaned_data.get('logo')
        if logo and hasattr(logo, 'size'):
            if logo.size > self.MAX_IMAGE_SIZE:
                raise forms.ValidationError('Logo must be under 5 MB.')
            if hasattr(logo, 'content_type') and logo.content_type not in self.ALLOWED_IMAGE_TYPES:
                raise forms.ValidationError('Logo must be a JPEG, PNG, WebP, or GIF image.')
        return logo


class CategoryForm(forms.ModelForm):
    """Form for adding/editing categories"""
    
    class Meta:
        model = Category
        fields = ['name', 'order']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Starters, Main Course, Drinks',
                'class': 'w-full px-4 py-2.5 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
            }),
            'order': forms.NumberInput(attrs={
                'min': '0',
                'value': '0',
                'class': 'w-full px-4 py-2.5 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
            }),
        }


class MenuItemForm(forms.ModelForm):
    """Form for adding/editing menu items"""

    ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/webp', 'image/gif']
    MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5 MB

    def __init__(self, restaurant, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter categories by restaurant
        self.fields['category'].queryset = Category.objects.filter(restaurant=restaurant)
        self.fields['category'].required = False

    class Meta:
        model = MenuItem
        fields = ['name', 'category', 'description', 'price', 'image', 'is_available', 'is_vegetarian']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Paneer Tikka, Margherita Pizza',
                'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
            }),
            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Briefly describe the dish — ingredients, taste, dietary notes…',
                'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all resize-none'
            }),
            'price': forms.NumberInput(attrs={
                'step': '0.01',
                'min': '0',
                'placeholder': '0.00',
                'class': 'w-full px-4 py-3 border border-[#E7E7E0] rounded-xl text-sm focus:border-[#059669] focus:ring-2 focus:ring-[#D1FAE5] outline-none transition-all'
            }),
        }

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and hasattr(image, 'size'):
            if image.size > self.MAX_IMAGE_SIZE:
                raise forms.ValidationError('Image must be under 5 MB.')
            if hasattr(image, 'content_type') and image.content_type not in self.ALLOWED_IMAGE_TYPES:
                raise forms.ValidationError('Image must be a JPEG, PNG, WebP, or GIF file.')
        return image
