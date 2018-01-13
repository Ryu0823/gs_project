from django import forms
from .models import Post, Message
from django.utils.translation import gettext_lazy as _

class FormPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title',)

class FormMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('text','human')
        labels = {
            'human': _('右に表示する'),
        }
