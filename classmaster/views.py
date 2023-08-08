from django.shortcuts import render
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
        
    return render(request,'tt_1.html',number_of_faculty)
def tt_2(request):
    a=[]
    # for i in range(0,number_of_faculty):
    #     a.append(0)
    # re={
    #     'res':a
    # }
    return render(request,'tt-2.html',re)