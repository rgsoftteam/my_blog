from django import forms
from .models import Topic, BlogPost

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['text']
		labels = {'text': 'BlogPost'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}