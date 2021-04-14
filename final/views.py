from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def home(request):
    return render(request, 'index.html')
def post(request):
    sal= request.GET['salary'] 
    bon=request.GET['Bonus']
    allow=request.GET['allowance']
    oth=request.GET['others']
    total_salary= sal+bon+allow+oth
# logic to calculate tax according to annual income.
    if total_salary<=400000:
        total_tax= total_salary*(0.01)
    elif total_salary > 400000 and total_salary <=500000:
        total_tax = total_salary*(0.1)
    elif total_salary > 500000 and total_salary <=700000:
        total_tax = total_salary*(0.2)
    elif total_salary > 700000 and total_salary <=2000000:
        total_tax = total_salary*(0.3)
    else:
        total_tax= total_salary*(0.36)
 
    return render(request,'tax.html',{'tax':total_tax})