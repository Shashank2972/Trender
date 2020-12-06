from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import Post, Profile, Like, Following
from django.contrib.auth.models import User
# Create your views here.
import os, json
from django.views.generic import ListView
from django.core.paginator import Paginator
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
        post = getPosts(user)
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

def getPosts(user):
    post_obj = Post.objects.filter(user=user)
    img_List = [post_obj[i:i+3] for i in range(0,len(post_obj),3)]
    return img_List

def delPost(request, postId):
    post_ = Post.objects.filter(pk=postId)
    # print(post_)
    # print(post_[0].image.url, post_[0].image.path)
    image_path = post_[0].image.url
    os.remove(post_[0].image.path)
    post_.delete()
    messages.info(request, "Post Deleted")
    return redirect('/userpage')

def likePost(request):
    post_id = request.GET.get("likeId", "")
    post = Post.objects.get(pk=post_id)
    user = request.user
    like = Like.objects.filter(post = post, user=user)
    liked = False

    if like:
        Like.dislike(post, user)
    else:
        liked = True
        Like.like(post, user)

    resp = {
        'liked':liked
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type = "application/json")

def follow(request, username):
    main_user = request.user
    to_follow = User.objects.get(username= username)

    following = Following.objects.filter(user = main_user, followed= to_follow)
    is_following= True if following else False

    if is_following:
        Following.unfollow(main_user, to_follow)
        is_following =False
    else:
        Following.follow(main_user, to_follow)
        is_following = True

    resp = {
        "following" : is_following,
    }
    response = json.dumps(resp)
    return HttpResponse(response, content_type="application/json")

class Search_User(ListView):
    model = User
    template_name = "userpage/searchUser.html"
    paginate_by = 1
    def get_queryset(self):
        username = self.request.GET.get("username","")
        print(username)
        queryset = User.objects.filter(username__icontains=username)
        print(queryset)
        return queryset
