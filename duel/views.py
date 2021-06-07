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
    template = loader.get_template('pages/dashboard.html')
    models = Post.objects.all().filter(key=request.user.id)
    counter = models.count()
    context = {
        'works': models,
        'count': counter,
    }
    return HttpResponse(template.render(context, request))


@login_required()
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
    model = Post.objects.filter(key=request.user.id)
    context = {
        'images': model
    }
    return HttpResponse(template.render(context, request))

@login_required()
def duel_get_works(request):
    template = loader.get_template('pages/duel_main.html')
    model = Post.objects.exclude(key=request.user.id)
    context= {
        'deuce': model
    }
    if request.method == "POST":
        selected_choice = model.get(pk=request.POST['work_id'])
        selected_choice.rate += 1
        selected_choice.save()
    return HttpResponse(template.render(context, request))