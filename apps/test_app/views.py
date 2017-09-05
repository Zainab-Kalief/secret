from django.shortcuts import render, redirect
from .models import User, Post, Like
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'test_app/index.html')

def dataTest(request):
    request.session.flush()
    entry = User.objects.register(request.POST)
    if not type(entry) is dict:
        return redirect('/result/{}'.format(entry.id))
    else:
        if 'name' in entry:
            messages.add_message(request, messages.INFO, entry['name'])
        if 'email' in entry:
            messages.add_message(request, messages.INFO, entry['email'])
        if 'password' in entry:
            messages.add_message(request, messages.INFO, entry['password'])
        if 'confirm_password' in entry:
            messages.add_message(request, messages.INFO, entry['confirm_password'])
        if 'email_exist' in entry:
            messages.add_message(request, messages.INFO, entry['email_exist'])
        return redirect('/')

def loginTest(request):
    request.session.flush()
    entry = User.objects.log_in(request.POST) #user loging in
    if entry == False:
        messages.add_message(request, messages.INFO, 'This user doesnt exist')
        return redirect('/')
    else:
        print entry.id, entry.name
        request.session['user_id'] = entry.id
        return redirect('/result/{}'.format(entry.id))

def result(request, id):
    entry = User.objects.get(id=id) #the whole user object gotten by the id from loginTest func redirection
    request.session['user_name'] = entry.name
    context = {'messages': Post.objects.all().order_by('-created_at'), 'user_id': entry.id,}
    return render(request, 'test_app/result.html', context)

def post_message(request, id): #this id is from the user id when he logs in
    user = User.objects.get(id=id)
    post = Post.objects.add_post(post=request.POST['post'], user_id=user) #user's post
    return redirect('/result/{}'.format(user.id)) #this is the same route as our loginTest so they share one url


def like_post(request, user_id, post_id):
    post = Post.objects.get(id=post_id)
    user = User.objects.get(id=user_id)
    like = Like.objects.add_like(user, post)
    return redirect('/result/{}'.format(request.session['user_id']))


def view_likes(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'likes': Like.objects.filter(post_id= post), 'post': post.post}
    return render(request, 'test_app/likes.html', context)

def delete_post(request, post_id):
    remove_post = Post.objects.get(id=post_id)
    remove_post.delete()
    return redirect('/result/{}'.format(request.session['user_id']))

def popular_secrets(request):
    return render(request, 'test_app/popular_secrets.html')
