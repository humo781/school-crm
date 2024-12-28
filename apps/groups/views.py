from django.shortcuts import render, redirect, get_object_or_404
from .models import Group
from ..students.models import Student
from ..teachers.models import Teacher


def home(request):
    return render(request, 'index.html')

def group_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group': group}
    return render(request, 'groups/group-detail.html', ctx)


def group_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher_id = request.POST.get('teacher')
        student_ids = request.POST.getlist('student')
        if name and teacher_id and student_ids:
            teacher = get_object_or_404(Teacher, pk=teacher_id)
            group = Group.objects.create(
                name=name,
                teacher=teacher
            )
            group.student.set(Student.objects.filter(pk__in=student_ids))
            group.save()
            return redirect('groups:list')
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    ctx = {'teachers': teachers, 'students': students}
    return render(request, 'groups/form.html', ctx)

def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        teacher = request.POST.get('teacher')
        student = request.POST.getlist('student')
        if name and teacher and student:
            group.name = name
            group.teacher = Teacher.objects.get(pk=teacher)
            group.student.set(Student.objects.filter(pk__in=student))
            group.save()
            return redirect('groups:list')
    ctx = {
           'group': group,
           'students': students,
           'teachers': teachers
    }
    return render(request, 'groups/form.html', ctx)

def group_del_confirm(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return redirect('groups:list')
    ctx = {'group': group}
    return render(request, 'groups/del-confirm.html', ctx)
