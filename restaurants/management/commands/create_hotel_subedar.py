from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from restaurants.models import Restaurant, Category, MenuItem

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates Hotel Subedar restaurant with full menu'

    def handle(self, *args, **kwargs):
        # Create user/owner for the restaurant
        email = 'hotelsubedar@example.com'
        
        # Check if user already exists
        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'User {email} already exists. Using existing user.'))
            user = User.objects.get(email=email)
        else:
            user = User.objects.create_user(
                username='hotelsubedar',
                email=email,
                password='subedar@123',
                role='restaurant_admin',
                phone='+919876543210'
            )
            self.stdout.write(self.style.SUCCESS(f'Created user: {email}'))

        # Check if restaurant already exists
        if Restaurant.objects.filter(owner=user).exists():
            self.stdout.write(self.style.WARNING('Restaurant already exists for this user. Deleting and recreating...'))
            Restaurant.objects.filter(owner=user).delete()

        # Create restaurant
        restaurant = Restaurant.objects.create(
            owner=user,
            name='Hotel Subedar',
            email='contact@hotelsubedar.com',
            phone='+919876543210',
            address='Shivaji Nagar, Pune, Maharashtra 411005',
            description='Authentic Maharashtrian and North Indian cuisine',
            is_active=True
        )
        self.stdout.write(self.style.SUCCESS(f'Created restaurant: {restaurant.name}'))

        # Menu data
        menu_data = {
            'Starters (Veg)': [
                {'name': 'Paneer Tikka', 'price': 240, 'description': 'Paneer cubes marinated in yogurt and spices grilled in tandoor', 'is_vegetarian': True},
                {'name': 'Hara Bhara Kebab', 'price': 210, 'description': 'Spinach and peas patties served with mint chutney', 'is_vegetarian': True},
                {'name': 'Crispy Corn', 'price': 180, 'description': 'Deep fried sweet corn tossed with spices', 'is_vegetarian': True},
                {'name': 'Veg Manchurian Dry', 'price': 200, 'description': 'Vegetable balls tossed in spicy Indo-Chinese sauce', 'is_vegetarian': True},
                {'name': 'Cheese Corn Balls', 'price': 220, 'description': 'Crispy cheese stuffed corn balls', 'is_vegetarian': True},
                {'name': 'Chilli Paneer', 'price': 240, 'description': 'Paneer cubes tossed with capsicum and chilli sauce', 'is_vegetarian': True},
                {'name': 'Veg Spring Rolls', 'price': 190, 'description': 'Crispy rolls stuffed with vegetables', 'is_vegetarian': True},
            ],
            'Non-Veg Starters': [
                {'name': 'Chicken Tikka', 'price': 320, 'description': 'Boneless chicken marinated in yogurt and spices', 'is_vegetarian': False},
                {'name': 'Tandoori Chicken (Half)', 'price': 340, 'description': 'Classic tandoor roasted chicken', 'is_vegetarian': False},
                {'name': 'Tandoori Chicken (Full)', 'price': 580, 'description': 'Full roasted chicken in tandoor', 'is_vegetarian': False},
                {'name': 'Chicken 65', 'price': 280, 'description': 'Spicy deep fried chicken bites', 'is_vegetarian': False},
                {'name': 'Chicken Lollipop', 'price': 300, 'description': 'Crispy fried chicken wings', 'is_vegetarian': False},
                {'name': 'Fish Fry', 'price': 320, 'description': 'Spiced shallow fried fish', 'is_vegetarian': False},
                {'name': 'Prawns Fry', 'price': 360, 'description': 'Prawns tossed with spices', 'is_vegetarian': False},
            ],
            'Maharashtrian Specials': [
                {'name': 'Misal Pav', 'price': 130, 'description': 'Spicy sprout curry served with pav', 'is_vegetarian': True},
                {'name': 'Vada Pav', 'price': 50, 'description': 'Deep fried potato fritter in pav', 'is_vegetarian': True},
                {'name': 'Sabudana Khichdi', 'price': 160, 'description': 'Tapioca pearls cooked with peanuts', 'is_vegetarian': True},
                {'name': 'Kanda Bhaji', 'price': 120, 'description': 'Onion fritters', 'is_vegetarian': True},
                {'name': 'Zunka Bhakar', 'price': 180, 'description': 'Traditional gram flour curry with bhakri', 'is_vegetarian': True},
                {'name': 'Pithla Bhakri', 'price': 190, 'description': 'Gram flour curry served with jowar bhakri', 'is_vegetarian': True},
                {'name': 'Thalipeeth', 'price': 160, 'description': 'Multigrain savory pancake', 'is_vegetarian': True},
            ],
            'Main Course (Veg)': [
                {'name': 'Paneer Butter Masala', 'price': 280, 'description': 'Creamy tomato based paneer curry', 'is_vegetarian': True},
                {'name': 'Paneer Lababdar', 'price': 290, 'description': 'Rich paneer gravy with butter', 'is_vegetarian': True},
                {'name': 'Palak Paneer', 'price': 270, 'description': 'Paneer cubes cooked in spinach gravy', 'is_vegetarian': True},
                {'name': 'Veg Kolhapuri', 'price': 250, 'description': 'Spicy vegetable curry with Kolhapuri masala', 'is_vegetarian': True},
                {'name': 'Kaju Curry', 'price': 300, 'description': 'Rich cashew nut curry', 'is_vegetarian': True},
                {'name': 'Mix Veg', 'price': 230, 'description': 'Mixed vegetables in rich gravy', 'is_vegetarian': True},
                {'name': 'Dal Tadka', 'price': 190, 'description': 'Yellow lentils tempered with spices', 'is_vegetarian': True},
                {'name': 'Dal Fry', 'price': 180, 'description': 'Lentils cooked with butter and garlic', 'is_vegetarian': True},
            ],
            'Main Course (Non-Veg)': [
                {'name': 'Butter Chicken', 'price': 340, 'description': 'Creamy tomato based chicken curry', 'is_vegetarian': False},
                {'name': 'Chicken Curry', 'price': 280, 'description': 'Traditional Indian chicken curry', 'is_vegetarian': False},
                {'name': 'Chicken Kolhapuri', 'price': 320, 'description': 'Spicy Kolhapuri style chicken', 'is_vegetarian': False},
                {'name': 'Chicken Handi', 'price': 330, 'description': 'Rich chicken gravy cooked in handi', 'is_vegetarian': False},
                {'name': 'Mutton Curry', 'price': 360, 'description': 'Slow cooked mutton in spicy gravy', 'is_vegetarian': False},
                {'name': 'Mutton Kolhapuri', 'price': 380, 'description': 'Authentic spicy Kolhapuri mutton', 'is_vegetarian': False},
                {'name': 'Fish Curry', 'price': 320, 'description': 'Coastal style fish curry', 'is_vegetarian': False},
                {'name': 'Prawns Masala', 'price': 360, 'description': 'Prawns cooked in rich spicy gravy', 'is_vegetarian': False},
            ],
            'Indian Breads': [
                {'name': 'Butter Naan', 'price': 60, 'description': 'Soft naan brushed with butter', 'is_vegetarian': True},
                {'name': 'Garlic Naan', 'price': 70, 'description': 'Naan topped with garlic', 'is_vegetarian': True},
                {'name': 'Tandoori Roti', 'price': 40, 'description': 'Whole wheat bread cooked in tandoor', 'is_vegetarian': True},
                {'name': 'Butter Roti', 'price': 45, 'description': 'Soft roti with butter', 'is_vegetarian': True},
                {'name': 'Lachha Paratha', 'price': 80, 'description': 'Layered crispy paratha', 'is_vegetarian': True},
                {'name': 'Missi Roti', 'price': 70, 'description': 'Gram flour flavored roti', 'is_vegetarian': True},
            ],
            'Rice & Biryani': [
                {'name': 'Veg Biryani', 'price': 240, 'description': 'Aromatic rice cooked with vegetables', 'is_vegetarian': True},
                {'name': 'Paneer Biryani', 'price': 270, 'description': 'Biryani with paneer cubes', 'is_vegetarian': True},
                {'name': 'Chicken Biryani', 'price': 320, 'description': 'Fragrant basmati rice with chicken', 'is_vegetarian': False},
                {'name': 'Mutton Biryani', 'price': 360, 'description': 'Rich mutton biryani', 'is_vegetarian': False},
                {'name': 'Veg Pulao', 'price': 200, 'description': 'Mild rice cooked with vegetables', 'is_vegetarian': True},
                {'name': 'Jeera Rice', 'price': 140, 'description': 'Basmati rice flavored with cumin', 'is_vegetarian': True},
                {'name': 'Steamed Rice', 'price': 120, 'description': 'Plain basmati rice', 'is_vegetarian': True},
            ],
            'Beverages': [
                {'name': 'Masala Chaas', 'price': 70, 'description': 'Spiced buttermilk', 'is_vegetarian': True},
                {'name': 'Sweet Lassi', 'price': 110, 'description': 'Sweet yogurt drink', 'is_vegetarian': True},
                {'name': 'Mango Lassi', 'price': 130, 'description': 'Yogurt blended with mango', 'is_vegetarian': True},
                {'name': 'Fresh Lime Soda', 'price': 90, 'description': 'Lemon soda', 'is_vegetarian': True},
                {'name': 'Cold Coffee', 'price': 150, 'description': 'Chilled coffee with ice cream', 'is_vegetarian': True},
                {'name': 'Fresh Orange Juice', 'price': 140, 'description': 'Fresh orange juice', 'is_vegetarian': True},
                {'name': 'Mineral Water', 'price': 20, 'description': 'Packaged drinking water', 'is_vegetarian': True},
            ],
            'Desserts': [
                {'name': 'Gulab Jamun', 'price': 100, 'description': 'Milk dumplings soaked in sugar syrup', 'is_vegetarian': True},
                {'name': 'Shrikhand', 'price': 130, 'description': 'Sweet yogurt dessert', 'is_vegetarian': True},
                {'name': 'Rabdi', 'price': 160, 'description': 'Thick sweet milk dessert', 'is_vegetarian': True},
                {'name': 'Chocolate Brownie', 'price': 160, 'description': 'Warm chocolate brownie', 'is_vegetarian': True},
                {'name': 'Vanilla Ice Cream', 'price': 90, 'description': 'Classic vanilla scoop', 'is_vegetarian': True},
                {'name': 'Chocolate Ice Cream', 'price': 100, 'description': 'Chocolate ice cream scoop', 'is_vegetarian': True},
            ],
        }

        # Create categories and menu items
        total_items = 0
        for order, (category_name, items) in enumerate(menu_data.items(), start=1):
            category = Category.objects.create(
                restaurant=restaurant,
                name=category_name,
                order=order
            )
            self.stdout.write(self.style.SUCCESS(f'  Created category: {category_name}'))

            for item_data in items:
                MenuItem.objects.create(
                    restaurant=restaurant,
                    category=category,
                    **item_data
                )
                total_items += 1

            self.stdout.write(self.style.SUCCESS(f'    Added {len(items)} items'))

        self.stdout.write(self.style.SUCCESS(f'\n✓ Successfully created Hotel Subedar with {total_items} menu items!'))
        self.stdout.write(self.style.SUCCESS(f'\nLogin credentials:'))
        self.stdout.write(self.style.SUCCESS(f'  Email: {email}'))
        self.stdout.write(self.style.SUCCESS(f'  Password: subedar@123'))
        self.stdout.write(self.style.SUCCESS(f'\nMenu URL: /menu/{restaurant.slug}/'))
