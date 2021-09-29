from django.forms import ModelForm
from .models import Bathroom

class BathroomForm(ModelForm):

    class Meta:
        model = Bathroom
        fields = ['owner', 'user', 'address', 'featured_image', 'demo_link','source_link', 'reviews', 'tags']