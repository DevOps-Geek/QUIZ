from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Index View
@login_required(login_url="login/")
def index(request):
    return render(request,'index.html')

