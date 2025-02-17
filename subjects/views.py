from django.shortcuts import render, redirect, get_object_or_404
from teachers.models import Teacher
from .models import Subject

def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subjects-list.html', ctx)

def subject_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            subject = Subject.objects.create(
                name=name,
            )
            teacher_ids = [int(teacher_id) for teacher_id in request.POST.getlist('teachers') if teacher_id.isdigit()]
            teachers = Teacher.objects.filter(id__in=teacher_ids)
            subject.teachers.set(teachers)

            return redirect('subjects:list')
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'subjects/form.html', ctx)

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    teacher = Teacher.objects.all()
    ctx = {'subject': subject, 'teacher': teacher}
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)

    if request.method == 'POST':

        name = request.POST.get('name')
        if name:
            subject.name = name

            teacher_ids = [int(teacher_id) for teacher_id in request.POST.getlist('teachers') if teacher_id.isdigit()]
            teachers = Teacher.objects.filter(id__in=teacher_ids)

            subject.teachers.set(teachers)
            subject.save()

            return redirect(subject.get_detail_url())

    teachers = Teacher.objects.all()
    ctx = {'subject': subject, 'teachers': teachers}
    return render(request, 'subjects/form.html', ctx)

def subject_del_conf(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subjects:list')

    teacher = Teacher.objects.all()
    ctx = {'subject': subject, 'teacher': teacher}
    return render(request, 'subjects/del_conf.html', ctx)
