from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, DeleteView, DetailView, UpdateView

from bboard.forms import BbForm
from bboard.models import Bb


class BbIndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Bb.objects.all()
        return context


def about_page(request):
    return render(request, 'about.html')


def contacts_page(request):
    return render(request, 'contacts.html')

class BbCreateView(CreateView):
    template_name = 'add.html'
    form_class = BbForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BbDeleteView(DeleteView):
    model = Bb
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context