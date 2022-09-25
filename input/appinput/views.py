from django.shortcuts import render
from django.views.generic import ListView
from .models import Input


def home(request):
    data = Input.objects.all()
    context = {'len_objects': len(data), 'title': 'main'}
    if request.method == "POST":
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        data_object = Input(input_data=data)
        data_object.save()
    return render(request, 'input/index.html', context)


class Data(ListView):
    model = Input
    template_name = 'input/data.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'data'
        query = Input.objects.all().values('input_data')
        context['data'] = list(query)
        return context
