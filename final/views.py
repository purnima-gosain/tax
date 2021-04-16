from django.shortcuts import render
from django.http import HttpResponse    

# Create your views here.
def home(request):
    if request.method == 'POST':
        sal = request.POST['salary']
        bon = request.POST['Bonus']
        allo = request.POST['allowance']
        oth = request.POST['others']
        salary = int(sal)
        bonus = int(bon)
        allow = int(allo)
        other = int(oth)
        total_salary = salary + bonus + allow + other
        print("total_salary",total_salary)
        print("allow",allow)

        if total_salary <=400000:
            total_tax= total_salary*(0.01)
            print("total_tax",total_tax)
        elif total_salary > 400000 and total_salary <=500000:
            total_tax = total_salary*(0.1)
            print("total_tax",total_tax)
        elif total_salary > 500000 and total_salary <=700000:
            total_tax = total_salary*(0.2)
            print("total_tax",total_tax)
        elif total_salary > 700000 and total_salary <=2000000:
            total_tax = total_salary*(0.3)
            print("total_tax",total_tax)
        else:
            total_tax= total_salary*(0.36)
            print("total_tax",total_tax)
    return render(request, 'index.html')
        # {'tax':total_tax}

   

