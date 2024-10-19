from django.shortcuts import render , HttpResponse,loader
from .models import Post,Comment
from .forms import CommentForm,LoginForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
def check_login(request):
    context = {'Flag' : 'False'}
    if request.user.is_authenticated:
        user = User.objects.get(username=request.user.username)
        context = {'user' : user.username,'Flag' : 'True'}
    return context
# Create your views here.
def post_list(request):
    context= check_login(request)
    posts = Post.objects.all()
    context.update({'posts' : posts}) 
    return render(request,'posts/post_list.html',context=context)


def post_details(request,post_id):
    context= check_login(request)
    form = CommentForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            c = form.save(commit=False)
            c.post_id = post_id
            c.save()
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post_id)
    context.update({'post' : post,'comments' : comments ,'form': form})
    return render(request,'posts/post_info.html',context=context)
def index(request):
    context= check_login(request)
    return render(request,'home/index.html',context=context)

def user_login(request):
    form = LoginForm(request.POST)
    context = {'form' : form}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username,password=password)
        login(request=request,user=user)
    return render(request,'auth/login.html',context)
def user_logout(request):
    logout(request)
    context= check_login(request)
    return render(request,'home/index.html',context=context)