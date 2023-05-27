from django.shortcuts import render
from .models import *
import pandas as pd
from django.http import JsonResponse
from django.conf import settings

def home(request):
    context = {}
    return render(request, 'index.html',context)


def export_data(request):
    data = Emp.objects.all()
    items = []

    for obj in data:
        items.append({
            "name": obj.name,
            "phone": obj.phone,
            "email": obj.email ,
        })
    
    pd.DataFrame(items).to_excel('output.xlsx')
    return JsonResponse({
        'status': 200
    })


def importData(request):
    # take excel
    if request.method == "POST":
        file  = request.FILES['files']
        obj =  up_data.objects.create(
            file = file
        )
        # get path of data saved
        path = str(obj.file)
        print(f'{settings.BASE_DIR}/{path}')
        
        # read data from excel
        df = pd.read_excel(path)
        print(df)
        
        for d in df.values:
            print(d)
            
        # Emp.objects.create(
        #     name = name(),
        #     phone = phone_number(),
        #     email = email()
        # )
        
    return render(request, 'form.html')
