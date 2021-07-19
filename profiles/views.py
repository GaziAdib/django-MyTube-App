from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import View
from . models import Profile
from videos.models import Video
from .forms import ProfileForm

# Create your views here.

class ProfileView(View):
    def get(self, request, pk, *args, **kwargs):
        profile = get_object_or_404(Profile, pk=pk)
        videos = Video.objects.all().filter(uploader=profile.id).order_by('-date_posted')

        context = {
            "profile": profile,
            "videos": videos
        }

        return render(request, 'profiles/profile.html', context)


def add_profile(request):
    form = ProfileForm()

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('index')
    else:
        form = ProfileForm()

    context = {
        'form' : form
    }

    return render(request, 'profiles/add_profile.html', context)            


def update_profile(request, pk):
    profile = Profile.objects.get(id=pk)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.instance.user = profile.user
            form.save()
            return redirect('index')
    
    context = {
        "form": form
    }

    return render(request, 'profiles/update_profile.html', context)       











