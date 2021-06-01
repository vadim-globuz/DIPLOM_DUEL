from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .forms import PostForm
from .models import Post


def index(request):
    template = loader.get_template('pages/index.html')
    context = {
        'latest_question_list': 'Hello',
    }
    return HttpResponse(template.render(context, request))


@login_required()
def profile(request):
    template = loader.get_template('pages/profile.html')
    model = Post.objects.all()
    context = {
        'posts_count': model.filter(key=request.user.id)
    }
    return HttpResponse(template.render(context, request))


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.key = request.user

            post.save()
            return redirect('main:profile')
    else:
        form = PostForm()
    return render(request, 'pages/post.html', {'form': form})


@login_required()
def album_view(request):
    template = loader.get_template('pages/album.html')
    model = Post.objects.all()
    context = {
        'images': model.filter(key=request.user.id)
    }
    return HttpResponse(template.render(context, request))
