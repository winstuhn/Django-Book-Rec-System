from django import forms
 
# creating a form
class BookForm(forms.Form):
    search_book = forms.CharField(label="Input a book here:", max_length = 100)
     