
import os
import django
from django.core.files import File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from store.models import Gemstone

# Map category names to the image filenames we just created
image_map = {
    'Ruby': 'gemstones/ruby.png',
    'Sapphire': 'gemstones/sapphire.png',
    'Emerald': 'gemstones/emerald.png',
    'Diamond': 'gemstones/diamond.png',
    'Amethyst': 'gemstones/amethyst.png',
}

# Also handle "Other" or unspecified by assigning a random one or specific one
default_image = 'gemstones/diamond.png'

def assign_images():
    count = 0
    for gemstone in Gemstone.objects.all():
        # Check if we have a specific image for this category
        if gemstone.category in image_map:
            img_path = image_map[gemstone.category]
        else:
            img_path = default_image
        
        # We assign the RELATIVE path from MEDIA_ROOT. 
        # Since we manually copied files to media/gemstones/, 
        # saving the string path to the ImageField is sufficient in many cases,
        # but to be safe and "Django-like", we can just set the field to the string relative path.
        # Django ImageFields store the path relative to MEDIA_ROOT.
        
        print(f"Assigning {img_path} to {gemstone.name} ({gemstone.category})")
        gemstone.image = img_path
        gemstone.save()
        count += 1
        
    print(f"Updated {count} gemstones with new images.")

if __name__ == '__main__':
    assign_images()
