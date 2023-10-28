from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label='Search', max_length=100)
    sortby = forms.ChoiceField(label='Sort by', choices=[('title', 'Title'), ('author', 'Author'), ('price', 'Price')], required=False)
    order = forms.ChoiceField(label='Order', choices=[('asc', 'Ascending'), ('desc', 'Descending')], required=False)