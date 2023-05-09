from django import forms
from .models import KnowledgeData

class Contact_Form(forms.ModelForm):
    class Meta():
        model = KnowledgeData
        fields=('title', 'content','member')
        labels={'title':"タイトル", 'content':"コンテンツ", 'member':"メンバー"}
