from django.shortcuts import render, redirect
from .models import JournalEntry, MoodLog, CommunityPost
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
def landing_page(request):
    return render(request, 'main/landing.html')
@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')
@login_required
def journal(request):
    if request.method == "POST":
        entry_text = request.POST.get('entry')
        if entry_text:
            JournalEntry.objects.create(user=request.user, entry=entry_text)
            return redirect('journal') 
    entries = JournalEntry.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/journal.html', {'entries': entries})
@login_required
def mood_tracking(request):
    moods = MoodLog.objects.filter(user=request.user).order_by('-date')
    if request.method == 'POST':
        date = request.POST.get('date')
        mood = request.POST.get('mood')
        notes = request.POST.get('notes', '')
        if date and mood:
            MoodLog.objects.create(
                user=request.user,
                date=date,
                mood=mood,
                notes=notes
            )
        return redirect('mood_tracking') 
    return render(request, 'main/mood_tracking.html', {'moods': moods})
@login_required
def shared_journals(request):
    entries = JournalEntry.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'main/shared_journals.html', {'entries': entries})
def community(request):
    posts = CommunityPost.objects.all()
    return render(request, 'main/community.html', {'posts': posts})
def hotlines(request):
    hotlines_list = [
        {"country": "United States", "hotline": "1-800-273-8255 (National Suicide Prevention Lifeline)"},
        {"country": "United Kingdom", "hotline": "116 123 (Samaritans)"},
        {"country": "Canada", "hotline": "1-833-456-4566 (Talk Suicide Canada)"},
    ]
    return render(request, 'main/hotlines.html', {'hotlines': hotlines_list})
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login') 