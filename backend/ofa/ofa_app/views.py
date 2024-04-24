#from django.shortcuts import render, HttpResponse
#from .models import Opportunity
#from .filters import OpportunityFilter
#from django.views import View
#from django.views.generic import ListView, DetailView
# Create your views here.


#def home(request):
#    items = Opportunity.objects.all()
#    opportunity_filter = OpportunityFilter(request.GET, queryset=Opportunity.objects.all())


#    return render(request, "home.html", {"opportunities" : items, "filter": opportunity_filter})


#class OpportunityListView(ListView):
#    model = Opportunity
#    template_name = "templates/home.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['filter'] = SnippetFilter(self.request.GET, queryset=self.get_queryset())
#        return context


from django.shortcuts import render
from django.views.generic import ListView
from .models import Opportunity
from .filters import OpportunityFilter

def home(request):
    opportunity_filter = OpportunityFilter(request.GET, queryset=Opportunity.objects.all())

    # Apply the filter to the queryset
    opportunities = opportunity_filter.qs

    return render(request, "home.html", {"opportunities": opportunities, "filter": opportunity_filter})

class OpportunityListView(ListView):
    model = Opportunity
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pass the filter object to the context
        context['filter'] = OpportunityFilter(self.request.GET, queryset=self.get_queryset())
        return context

