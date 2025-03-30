from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio', 'image']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

