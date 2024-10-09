from django import forms 
from .models import Product 
 

class SearchForm(forms.Form):
    query = forms.CharField(label='検索キーワード', required=False, widget=forms.TextInput(attrs={'placeholder': '映画のタイトルを入力'}))

class ProductForm(forms.ModelForm): 
    class Meta: 
        model = Product 
        fields = ['name', 'description', 'price', 'category'] 
        labels = {
            'name': '商品名',
            'description': '商品説明',
            'price': '価格',
            'category': 'カテゴリ',
        }