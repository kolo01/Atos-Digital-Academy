from django.shortcuts import render

from student.forms import StudentForm, StudentsForm


# Create your views here.

def index(request):
    
    context={
        'nom': "Mon nom pour l'application ",
        'prenom': "Mon prenom ",
    }
    return render(request, "student/index.html")

def edit(request):
    form = StudentForm()
    context = {'form': form}
    return render(request, "student/edit.html",context)

def add(request):
    form = StudentForm()
    context = {'form': form}
    return render(request, "student/add.html",context)
    
def fold(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = form = StudentsForm()
    context = {'form': form}
    return render(request, "student/fold.html",context)
    


