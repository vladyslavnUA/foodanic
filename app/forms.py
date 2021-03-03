from django import forms
from .models import *
from durationwidget.widgets import TimeDurationWidget

class RecipeForm(forms.ModelForm):
    prep = forms.DurationField(widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False), required=False)
    cook = forms.DurationField(widget=TimeDurationWidget(show_days=False, show_hours=True, show_minutes=True, show_seconds=False), required=False)
    
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ('author',)
        