from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"Whatsapp/home.html")

def SendData(request):
    if request.method == 'POST':
        Num = request.POST['Phone']
        Msg = request.POST['Message']
        print(Num,Msg)
        info = "Message has successfully sent.."
        return render(request,"Whatsapp/home.html",{'info':info})
    else:
        return HttpResponse("<h1>404 - Not Found :(</h1>")