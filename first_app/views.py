from django.shortcuts import render
from first_app.models import User, AccessRecord

from .forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'first_app/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user_list':user_list}
    # my_dict = {'insert_me':"yoooooo test"}
    return render(request,'first_app/users.html',context=user_dict)

def usersform(request):

    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVAILD')

    return render(request,'first_app/usersform.html',{'form':form})
