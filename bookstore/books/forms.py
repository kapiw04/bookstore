from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label='Search',
                             max_length=100,
                             required=False,
                             widget=forms.TextInput(
                                 attrs={'class': 'col search'})
                             )
    sortby = forms.ChoiceField(label="Sort by",
                               choices=[('title', 'Title'), ('author',
                                                             'Author'), ('price', 'Price'), ('sales_in_millions', 'Popularity')],
                               required=False,
                               initial='title',
                               widget=forms.Select(
                                   attrs={'class': 'col choice'})
                               )
    order = forms.ChoiceField(label='Order',
                              choices=[(
                                  'asc', 'Ascending'), ('desc', 'Descending')],
                              required=False,
                              initial='asc',
                              widget=forms.Select(
                                  attrs={'class': 'col choice'})
                              )
