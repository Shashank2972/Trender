from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Post
# Create your views here.


def userHome(request):
    posts = Post.objects.all().order_by('-pk')
    data = {'posts':posts}
    return render(request,"userpage/postfeed.html",data)

def post(request):
    if request.method=="POST":
        image_= request.FILES['image']
        captions_ =request.POST.get('captions','')
        user_ = request.user
        post_obj = Post(user=user_, captions=captions_, image=image_)
        post_obj.save()
        messages.success(request, "Sucessfully Posted")
        return redirect('/userpage')
    else:
        messages.error(request,"Something went Wrong : (")
        return redirect('/userpage')

def userProfile(request, username):
    return render(request, 'userpage/userProfile.html')