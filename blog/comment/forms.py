from django import forms
from django.forms import fields
from comment.models import Comment

class CommentForm(forms.ModelForm):
     class Meta:
          model = Comment
          # fields = '__all__'
          exclude = ('created_date',)