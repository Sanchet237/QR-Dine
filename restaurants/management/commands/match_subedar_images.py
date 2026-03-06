from django.core.management.base import BaseCommand
from django.core.files import File
from restaurants.models import Restaurant, MenuItem
import os
import shutil
from pathlib import Path
from difflib import SequenceMatcher


class Command(BaseCommand):
    help = 'Match images from static/Subedar Menu to Hotel Subedar menu items'

    def similarity(self, a, b):
        """Calculate similarity ratio between two strings"""
        return SequenceMatcher(None, a.lower(), b.lower()).ratio()

    def handle(self, *args, **kwargs):
        # Get Hotel Subedar restaurant
        try:
            restaurant = Restaurant.objects.get(name='Hotel Subedar')
        except Restaurant.DoesNotExist:
            self.stdout.write(self.style.ERROR('Hotel Subedar restaurant not found!'))
            return

        # Path to images
        static_folder = Path('static/Subedar Menu')
        media_folder = Path('media/menu_items')
        
        # Create media folder if it doesn't exist
        media_folder.mkdir(parents=True, exist_ok=True)

        # Get all image files
        image_files = {}
        for ext in ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']:
            for img_path in static_folder.glob(ext):
                # Store with normalized name as key
                name = img_path.stem.lower().replace('_', ' ').replace('-', ' ')
                image_files[name] = img_path

        self.stdout.write(self.style.SUCCESS(f'Found {len(image_files)} images in static folder'))

        # Get all menu items
        menu_items = MenuItem.objects.filter(restaurant=restaurant)
        matched = 0
        unmatched = []

        for item in menu_items:
            # Normalize item name for matching
            item_name_normalized = item.name.lower().replace('-', ' ')
            
            # Try exact match first
            best_match = None
            best_ratio = 0
            
            for img_name, img_path in image_files.items():
                ratio = self.similarity(item_name_normalized, img_name)
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_match = img_path

            # If similarity is good enough (>0.6), use it
            if best_ratio > 0.6 and best_match:
                # Copy image to media folder
                new_filename = f"{restaurant.slug}_{item.id}_{best_match.name}"
                destination = media_folder / new_filename
                
                try:
                    shutil.copy2(best_match, destination)
                    
                    # Update menu item with relative path for Django's FileField
                    item.image = f'menu_items/{new_filename}'
                    item.save()
                    
                    matched += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✓ {item.name} → {best_match.name} (similarity: {best_ratio:.2f})'
                        )
                    )
                except Exception as e:
                    self.stdout.write(
                        self.style.ERROR(f'✗ Error copying {best_match.name}: {str(e)}')
                    )
            else:
                unmatched.append(item.name)
                self.stdout.write(
                    self.style.WARNING(
                        f'⚠ No good match for: {item.name} (best: {best_ratio:.2f})'
                    )
                )

        self.stdout.write(self.style.SUCCESS(f'\n📊 Summary:'))
        self.stdout.write(self.style.SUCCESS(f'  ✓ Matched: {matched}/{menu_items.count()}'))
        if unmatched:
            self.stdout.write(self.style.WARNING(f'  ⚠ Unmatched: {len(unmatched)}'))
            for name in unmatched:
                self.stdout.write(self.style.WARNING(f'    - {name}'))
