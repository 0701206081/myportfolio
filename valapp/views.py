from django.shortcuts import render,redirect
from valapp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        mycontacts=Contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        mycontacts.save()
        return redirect('/contact')
    else:
        return render(request,'contact.html')
