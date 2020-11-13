from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	"""Class for forms to add posts"""
	
	class Meta:
		model = Post
		fields = ('title', 'text',)