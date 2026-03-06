from django.core.management.base import BaseCommand
from restaurants.models import Restaurant
import qrcode
from pathlib import Path
from django.conf import settings


class Command(BaseCommand):
    help = 'Generate QR code for Hotel Subedar menu'

    def handle(self, *args, **kwargs):
        # Get Hotel Subedar restaurant
        try:
            restaurant = Restaurant.objects.get(name='Hotel Subedar')
        except Restaurant.DoesNotExist:
            self.stdout.write(self.style.ERROR('Hotel Subedar restaurant not found!'))
            return

        # Generate the menu URL (you need to replace with your actual domain)
        menu_url = f'http://127.0.0.1:8000/menu/{restaurant.slug}/'
        
        self.stdout.write(self.style.SUCCESS(f'Generating QR code for: {menu_url}'))

        # Create QR code with high error correction
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% damage tolerance
            box_size=12,
            border=4,
        )
        qr.add_data(menu_url)
        qr.make(fit=True)
        
        # Generate image with restaurant theme colors
        img = qr.make_image(fill_color="#064E3B", back_color="#FFFFFF")
        
        # Ensure directories exist
        qr_dir = Path(settings.MEDIA_ROOT) / 'qr_codes'
        qr_dir.mkdir(parents=True, exist_ok=True)
        
        static_qr_dir = Path('static/qr_codes')
        static_qr_dir.mkdir(parents=True, exist_ok=True)
        
        # Save QR code in both media and static folders
        media_qr_path = qr_dir / f'{restaurant.slug}.png'
        static_qr_path = static_qr_dir / f'{restaurant.slug}.png'
        
        img.save(str(media_qr_path))
        img.save(str(static_qr_path))
        
        self.stdout.write(self.style.SUCCESS(f'\n✓ QR Code generated successfully!'))
        self.stdout.write(self.style.SUCCESS(f'\nSaved to:'))
        self.stdout.write(self.style.SUCCESS(f'  1. {media_qr_path}'))
        self.stdout.write(self.style.SUCCESS(f'  2. {static_qr_path}'))
        self.stdout.write(self.style.SUCCESS(f'\nMenu URL: {menu_url}'))
        self.stdout.write(self.style.SUCCESS(f'Restaurant Slug: {restaurant.slug}'))
        
        # Print additional info
        self.stdout.write(self.style.SUCCESS(f'\n📱 How to use:'))
        self.stdout.write(self.style.SUCCESS(f'  • Print the QR code and place it on tables'))
        self.stdout.write(self.style.SUCCESS(f'  • Customers can scan with any camera app'))
        self.stdout.write(self.style.SUCCESS(f'  • No app download required'))
