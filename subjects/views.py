from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject

def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subjects-list.html', ctx)

def subject_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Subject.objects.create(
                name=name,
            )
            return redirect('subjects:list')
    return render(request, 'subjects/form.html')

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    name = request.POST.get('firstName')
    if name:
        subject.name = name
        subject.save()
        return redirect(subject.get_detail_url())
    return render(request, 'subjects/form.html', {'subject': subject})

def subject_del_conf(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subjects:list')
    return render(request, 'subjects/del_conf.html', {'subject': subject})
