from django.shortcuts import render, reverse, redirect
from . models import Video, Comment, Category
from . forms import VideoForm, CommentForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from datetime import datetime
from django.db.models import Q

# Create your views here.

def index(request):
    videos = Video.objects.all()

    context = {
        "videos": videos
    }
    return render(request, 'videos/index.html', context)



def detail_video(request, pk):
    video = Video.objects.get(id=pk)

    form = CommentForm(request.POST)

    if form.is_valid():
        comment = Comment(
            user = request.user,
            video = video,
            comment = form.cleaned_data['comment']
        )
        comment.save()


    comments = Comment.objects.filter(video=video).order_by('-created_on')
    categories = Video.objects.filter(category=video.category)[:15]
    
    context = {
        "video": video,
        "comments": comments,
        "categories": categories,
        "form": form
    }

    return render(request, 'videos/detail_video.html', context)



def create_video(request):
    form = VideoForm()

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.uploader = request.user
            form.save()
            return redirect('index')
    else:
        form = VideoForm()        

    context = {
        "form": form
    }
    return render(request, 'videos/create_video.html', context)



def update_video(request, pk):
    video = Video.objects.get(id=pk)

    form = VideoForm(instance=Video)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('index')
 
    context = {
        "form": form
    }

    return render(request, 'videos/update_video.html', context)





class DeleteVideo(DeleteView):
    model = Video
    template_name = 'videos/delete_video.html'

    def get_success_url(self):
        return reverse('index')        


def video_category_list(request,pk):
    category = Category.objects.get(id=pk)
    videos = Video.objects.filter(category=category).order_by('-date_posted')

    context = {
        'category': category,
        'videos': videos
    }
    return render(request, 'videos/video_category.html', context)



def search_video(request):
    query = request.GET.get('query');

    query_list = Video.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query) |
        Q(uploader__username__icontains=query) 
    )

    context = {
        'query_list': query_list
    }

    return render(request, 'videos/search.html', context)