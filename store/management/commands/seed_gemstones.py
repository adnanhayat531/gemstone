from django.core.management.base import BaseCommand
from store.models import Gemstone
from django.core.files.base import ContentFile
import requests

class Command(BaseCommand):
    help = 'Seeds the database with sample gemstones'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        gemstones = [
            {
                'name': 'Royal Blue Sapphire',
                'category': 'Sapphire',
                'price': 4500.00,
                'description': 'A magnificent Royal Blue Sapphire from Sri Lanka, displaying exceptional clarity and brilliance.',
                'origin': 'Sri Lanka',
                'carat': 2.50,
                'treatment': 'Heat',
                'certification': 'GIA',
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1617058475267-28d8b4c023d7?auto=format&fit=crop&w=600&q=80' # Placeholder
            },
            {
                'name': 'Pigeon Blood Ruby',
                'category': 'Ruby',
                'price': 8500.00,
                'description': 'Rare Pigeon Blood Ruby with intense saturation. A true collector\'s piece.',
                'origin': 'Burma',
                'carat': 1.80,
                'treatment': 'None',
                'certification': 'GRS',
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1615655114865-4cc1bda5901e?auto=format&fit=crop&w=600&q=80' # Placeholder
            },
            {
                'name': 'Colombian Emerald',
                'category': 'Emerald',
                'price': 6200.00,
                'description': 'Vivid green Colombian Emerald with minor oil. Classic emerald cut.',
                'origin': 'Colombia',
                'carat': 3.10,
                'treatment': 'Minor Oil',
                'certification': 'GIA',
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1603957640244-635e98544c01?auto=format&fit=crop&w=600&q=80' # Placeholder
            },
            {
                'name': 'Amethyst Cushion',
                'category': 'Amethyst',
                'price': 450.00,
                'description': 'Deep purple Amethyst with a perfect cushion cut. Great value.',
                'origin': 'Brazil',
                'carat': 5.50,
                'treatment': 'None',
                'certification': 'Local',
                'featured': False,
                'image_url': 'https://images.unsplash.com/photo-1549488344-c7079f85aa59?auto=format&fit=crop&w=600&q=80' # Placeholder is gem-like
            },
            {
                'name': 'Brilliant Cut Diamond',
                'category': 'Diamond',
                'price': 12000.00,
                'description': 'VVS1 Clarity, E Color. The ultimate symbol of eternity.',
                'origin': 'Botswana',
                'carat': 1.05,
                'treatment': 'None',
                'certification': 'GIA',
                'featured': True,
                'image_url': 'https://images.unsplash.com/photo-1616867727376-74db498939c3?auto=format&fit=crop&w=600&q=80'
            }
        ]

        for gem_data in gemstones:
            if not Gemstone.objects.filter(name=gem_data['name']).exists():
                gem = Gemstone(
                    name=gem_data['name'],
                    category=gem_data['category'],
                    price=gem_data['price'],
                    description=gem_data['description'],
                    origin=gem_data['origin'],
                    carat=gem_data['carat'],
                    treatment=gem_data['treatment'],
                    certification=gem_data['certification'],
                    featured=gem_data['featured']
                )
                
                # Download and save image
                try:
                    response = requests.get(gem_data['image_url'])
                    if response.status_code == 200:
                        file_name = f"{gem_data['name'].lower().replace(' ', '_')}.jpg"
                        gem.image.save(file_name, ContentFile(response.content), save=False)
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"Could not download image for {gem_data['name']}: {e}"))

                gem.save()
                self.stdout.write(self.style.SUCCESS(f"Created gemstone: {gem.name}"))
            else:
                self.stdout.write(f"Gemstone {gem_data['name']} already exists.")

        self.stdout.write(self.style.SUCCESS('Data seeding completed!'))
