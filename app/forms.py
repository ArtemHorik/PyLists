from django import forms
from app.models import Item

EMPTY_ITEM_ERROR = "You can't have an empty list item"


class ItemForm(forms.models.ModelForm):
    """Form for list item"""

    class Meta:
        model = Item
        fields = ('text',)
        widgets = {
            'text': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a to-do item',
                'class': 'form-control-lg w-50 border-info'
            })
        }
        error_messages = {
            'text': {'required': EMPTY_ITEM_ERROR}
        }
