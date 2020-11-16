from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Post, Profile
from django.contrib.auth.models import User
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
    user = User.objects.filter(username=username)
    if user:
        user = user[0]
        profile = Profile.objects.get(user=user)
        bio = profile.bio
        conn = profile.connection
        user_img = profile.userImage
        
        data = {
            'user_obj':user,
            'bio':bio,
            'conn':conn,
            'userImg':user_img,
            'posts':post,
        }
    else: return HttpResponse("NO SUCH USER")

    return render(request, 'userpage/userProfile.html', data)


def delPost(request, postId):
    post_ = Post.objects.filter(pk=postId)
    # print(post_)
    image_path = post_[0].image.url
    post_.delete()
    messages.info(request, "Post Deleted")
    return redirect('/userpage')