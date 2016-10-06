from django.shortcuts import render


# Index View
def index(request):
    return render(request,'index.html')

