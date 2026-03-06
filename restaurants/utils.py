import qrcode
from io import BytesIO
from pathlib import Path
from django.conf import settings
import os


def generate_qr_code(restaurant, request):
    """
    Generate a QR code for a restaurant's menu.
    Returns the relative path to the saved QR code image.
    """
    # Build the absolute URL for the menu
    menu_url = request.build_absolute_uri(f'/menu/{restaurant.slug}/')
    
    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # 30% damage tolerance
        box_size=12,
        border=4,
    )
    qr.add_data(menu_url)
    qr.make(fit=True)
    
    # Generate image with custom colors
    img = qr.make_image(fill_color="#064E3B", back_color="#FAFAF7")
    
    # Ensure media directory exists
    qr_dir = Path(settings.MEDIA_ROOT) / 'qr_codes'
    qr_dir.mkdir(parents=True, exist_ok=True)
    
    # Save QR code
    qr_path = qr_dir / f'{restaurant.slug}.png'
    img.save(str(qr_path))
    
    # Return relative path for media URL
    return f'qr_codes/{restaurant.slug}.png'
