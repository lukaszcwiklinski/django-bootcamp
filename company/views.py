from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, FormView, UpdateView

from company.form import EditForm
from company.models import Company


class List(ListView):
    model = Company
    template_name = 'list.html'
    queryset = Company.objects.filter(is_active=True)


class Details(DetailView):
    model = Company
    template_name = 'details.html'


class Delete(DeleteView):
    model = Company
    success_url = reverse_lazy('company:list')
    template_name = 'delete.html'

    # def delete(self, request, *args, **kwargs):
    #     company = self.get_object()
    #     company.is_active = False
    #     company.save(update_fields=['is_active'])
    #
    #     return redirect('company:list')


class Edit(UpdateView):
    model = Company
    template_name = 'edit.html'
    success_url = reverse_lazy('company:list')
    fields = ['name', 'owner', 'category']
