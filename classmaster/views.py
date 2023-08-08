from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def seating(request):
    res={}
    if request.method == "POST":
        exam=request.POST['exam']
        no_of_class=int(request.POST['no_of_class'])
        capacity=int(request.POST['capacity'])
        startin_roll=int(request.POST['start_roll'])
        ending_roll=int(request.POST['ending_roll'])
        classes = [[] for _ in range(no_of_class)]

        current_roll = startin_roll
        for i in range(no_of_class):
            for _ in range(capacity):
                if current_roll <= ending_roll:
                 classes[i].append(current_roll)
                current_roll += 1
        
        res={
            'exam':exam,
            'classes': enumerate(classes, 1),
            'noofclass':no_of_class
        }
    return render(request,'seating.html',res)
def tt_1(request):
    if request.method == "POST":
        number_of_faculty=int(request.POST['number_of_faculty'])
    return render(request,'tt_1.html')

def tt_2(request):
    if request.method == "POST":
        # Get the data from the submitted form
        number_of_faculty = len(request.POST.getlist('faculty_name'))
        faculty_names = request.POST.getlist('faculty_name')
        class_names = request.POST.getlist('class_name[]')
        subject_names = request.POST.getlist('subject_name[]')
        subject_durations = request.POST.getlist('subject_duration[]')
        practical_lectures = request.POST.getlist('practical_lectures[]')
        practical_batches = request.POST.getlist('practical_batches[]')

        # Your processing logic for the form data goes here...
        # For example, you can pass the extracted data to the template for display.

        context = {
            'number_of_faculty': number_of_faculty,
            'faculty_names': faculty_names,
            'class_names': class_names,
            'subject_names': subject_names,
            'subject_durations': subject_durations,
            'practical_lectures': practical_lectures,
            'practical_batches': practical_batches,
        }

        # return render(request, context)

    return render(request, 'tt-2.html')  # Render the initial form if it's not a POST request

