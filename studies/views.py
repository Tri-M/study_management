from django.shortcuts import render, redirect, get_object_or_404
from .models import Study
from .forms import StudyForm

from django.shortcuts import render


from django.shortcuts import render
from .models import Study

def study_list(request):
    studies = Study.objects.all()  
    return render(request, 'studies/study_list.html', {'studies': studies})


from django.shortcuts import render, get_object_or_404
from .models import Study

def view_study(request, id):
    study = get_object_or_404(Study, id=id)
    return render(request, 'studies/view_study.html', {'study': study})


def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudyForm()
    return render(request, 'studies/add_study.html', {'form': form})

from django.shortcuts import render, get_object_or_404
from .models import Study
from .forms import StudyForm

def edit_study(request, id):
    study = get_object_or_404(Study, id=id)  
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('study_list') 
    else:
        form = StudyForm(instance=study)
    
    return render(request, 'studies/edit_study.html', {'form': form, 'study': study})

from django.shortcuts import redirect, get_object_or_404
from .models import Study

from django.shortcuts import get_object_or_404, redirect
from .models import Study

def delete_study(request, id):
    if request.method == 'POST':
        study = get_object_or_404(Study, id=id)
        study.delete()
        return redirect('study_list')
    return redirect('study_list') 


