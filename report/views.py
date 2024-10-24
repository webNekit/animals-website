from django.shortcuts import render
from .models import Report

# Create your views here.

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report/page-index.html', {
        'reports': reports
    })

def report_detail(request, pk):
    report = Report.objects.get(pk=pk)
    return render(request, 'report/page-detail.html', {
        'report': report
    })