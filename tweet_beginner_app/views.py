from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from rest_framework import viewsets
from .serializers import TweetSerializer
from .utils import get_weather

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            
            # Get weather data for the specified city or default to London
            city = form.cleaned_data.get('city') or 'London'
            weather_data = get_weather(city)
            if weather_data:
                tweet.temperature = weather_data['temperature']
                tweet.weather_description = weather_data['description']
                tweet.city = weather_data['city']
            else:
                print("Weather data could not be fetched.")  # Debug print
                # Optionally, set default values or handle the error

            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class TweetViewSet(viewsets.ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


