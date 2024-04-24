#import django_filters
#from .models import Opportunity

#class OpportunityFilter(django_filters.FilterSet):

#    CHOICES = (
#        ('ascending', "Ascending"),
#        ('descending', "Descending"),
#        ('Domestic', "Domestic")
#    )

#    ordering = django_filters.ChoiceFilter(label="Category", choices=CHOICES, method="filter_by_order")

#    class Meta: 
#        model = Opportunity
#        fields = {
        
#        "program_name" : ['icontains'],
#        'category' : ['icontains']
#        }

#    def filter_by_order(self, queryset, name, value):
#        expression = 'program_name' if value == 'ascending' else '-created'
#        return queryset.order_by(expression)


import django_filters
from django import forms  # Importing forms module

from .models import Opportunity


class OpportunityFilter(django_filters.FilterSet):

    
    # Define the choices for the dropdown filter
    CHOICES = (
        ('', 'All'),  # Default choice for no selection
        ('Domestic', 'Domestic'),
        ('Abroad', 'Abroad'),
        ('postgrad', 'postgrad'),
        ('law', 'law')
        # Add more choices as needed
    )

    program_name = django_filters.CharFilter(label="Program Name", field_name="program_name", lookup_expr='icontains',
    widget=forms.TextInput(attrs={'placeholder': 'Enter program name...'}))
    category = django_filters.ChoiceFilter(label="Category", choices=CHOICES, empty_label=None)


    class Meta: 
        model = Opportunity
        fields = {
            #'program_name': ['icontains'],
        }
