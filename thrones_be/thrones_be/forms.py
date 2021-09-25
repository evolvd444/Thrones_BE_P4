from django.forms import ModelForm
from .models import Bathroom

class BathroomForm(ModelForm):

    class Meta:
        model = Bathroom
        fields = ['owner', 'address', 'image', 'reviews', 'tags']