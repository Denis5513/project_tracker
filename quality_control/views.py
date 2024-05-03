from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm

#Function-Based Views

def index(request):
    return render(request, 'quality_control/index.html')

def bug_list(request):
    bug_list = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'object_list': bug_list})

def feature_list(request):
    feature_list = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'object_list': feature_list})

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug, 'project': bug.project, 'task': bug.task})

def feature_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_detail.html', {'feature': feature, 'project': feature.project, 'task': feature.task})

def create_bug_report(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('quality_control:bug_list')

    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

def create_feature_request(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('quality_control:feature_list')

    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

def update_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
        return redirect('quality_control:bug_detail', {'bug_id': bug_id})

    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_update.html', {'form': form, 'bug': bug})

def update_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    if request.method == 'POST':
        form = FeatureRequest(request.POST, instance=feature)
        if form.is_valid():
            form.save()
        return redirect('quality_control:feature_detail', {'feature_id': feature_id})

    else:
        form = BugReportForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})

def delete_bug_report(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')

def delete_feature_request(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    feature.delete()
    return redirect('quality_control:feature_list')


#Class-Based Views

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

class BugListView(ListView):
    model = BugReport
    template_name = 'quality_control/bug_list.html'

class FeatureListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/feature_list.html'

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'
    context_object_name = 'bug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bug = self.get_object()
        context['project'] = bug.project
        context['task'] = bug.task
        return context

class  FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'
    context_object_name = 'feature'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feature = self.get_object()
        context['project'] = feature.project
        context['task'] = feature.task
        return context

class BugCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('quality_control:feature_list')

class BugUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_update.html'
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    from_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    success_url = reverse_lazy('quality_control:feature_list')

class BugDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_confirm_delete.html'
    context_object_name = 'bug'
    success_url = reverse_lazy('quality_control:bug_list')

class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_confirm_delete.html'
    context_object_name = 'feature'
    success_url = reverse_lazy('quality_control:feature_list')


