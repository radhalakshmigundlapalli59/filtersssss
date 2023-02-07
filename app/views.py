from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'hAI gOOD MorNIng TO all','dt':dt,'c':3}
    return render(request,'filters.html',d)