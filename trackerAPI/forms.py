from django import forms
from .models import Book, Category
from datetime import date

class BookForm(forms.ModelForm):
    subtitle = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Enter subtitle'}))

    class Meta:
        model = Book
        fields = ['title', 'subtitle', 'authors', 'published_date', 'publisher', 'category', 'distribution_expense']

        widgets = { 'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
                    'published_date': forms.DateInput(attrs={'type': 'date'}),
                    'distribution_expense': forms.NumberInput(attrs={'class': 'input', 'step': '0.5'})
        }
        
    def __init__(self, *args, **kwargs): 
        super(BookForm, self).__init__(*args, **kwargs) 
        self.fields['published_date'].initial = date.today()
    
    def clean_distribution_expense(self):
        expense = self.cleaned_data['distribution_expense']
        if expense <= 0:
            raise forms.ValidationError('Expense must be greater than zero')