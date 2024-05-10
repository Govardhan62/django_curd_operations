from django.shortcuts import render,redirect
from newapp.models import Member

# Create your views here.
def sample(request):
    mem =Member.objects.all()
    return render(request,'sample.html',{'mem':mem})


def add(request):
    return render(request,'add.html')

def addrec(request):
         if request.method == 'POST':
                
           firstname = request.POST['firstname']
           lastname = request.POST['lastname']
           country = request.POST['country']

           query =Member(firstname=firstname,lastname=lastname,country=country)
           query.save()
           return redirect("/")

def update(request,id):
        if request.method=="POST":
          firstname = request.POST['firstname']
          lastname = request.POST['lastname']
          country = request.POST['country']

          edit =Member.objects.get(id=id)
          edit.firstname = firstname
          edit.lastname = lastname
          edit.country = country
          edit.save()
          return redirect("/")


        d =Member.objects.get(id=id)
        context={'d':d}
        return render(request,"update.html",context)  

def delete(request,id):
    d=Member.objects.get(id=id)
    d.delete()
    return redirect("/")