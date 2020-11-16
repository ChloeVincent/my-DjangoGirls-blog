from django import forms
from .models import Post, Species

class PostForm(forms.ModelForm):
	"""Class for forms to add posts"""
	
	class Meta:
		model = Post
		fields = ('title', 'text',)


class SearchForm(forms.ModelForm):
	"""Class for forms to search for species"""

	class Meta:
		model = Species
		fields = ('query',)