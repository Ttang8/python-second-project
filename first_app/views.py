from django.shortcuts import render
from first_app.models import User, AccessRecord
# Create your views here.

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user_list':user_list}
    # my_dict = {'insert_me':"yoooooo test"}
    return render(request,'first_app/index.html',context=user_dict)
