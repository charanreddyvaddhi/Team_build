from django.shortcuts import render, get_object_or_404
from django.views import generic
from Resources.models import People, Technology


# Create your views here.

def page1(request):
    candidates = People.objects.all().count()
    techs = Technology.objects.all().count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'candidates': candidates,
               'techs':techs,
               'num_visits': num_visits, }
    return render(request, 'index.html', context=context)


class MembersListView(generic.ListView):
    model = People
    context_object_name = 'my_resource_list'
    queryset = People.objects.all()
    template_name = 'resources_list.html'


class MembersDetailView(generic.DetailView):
    model = People
    template_name = 'resources_detail.html'

    def member_detail_view(request, primary_key):
        member = get_object_or_404(People, pk=primary_key)
        return render(request, 'Resources/resources_detail.html', context={'member': member})


class TechnologiesListView(generic.ListView):
    model = Technology
    context_object_name = 'technologies_list'
    queryset = Technology.objects.all()
    template_name = 'technologies_list.html'
