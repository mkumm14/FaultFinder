from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from bug.models import Bug

# Create your views here.


@login_required()
def home(request):
    user=request.user

    num_open_bugs = Bug.objects.filter(assigned_to=user, status='new').count(
    ) + Bug.objects.filter(assigned_to=user, status='in_progress').count()


# Count the number of closed bugs
    num_closed_bugs = Bug.objects.filter(assigned_to=user, status='fixed').count(
    ) + Bug.objects.filter(assigned_to=user, status='closed').count()

    return render(request, 'main/home.html', {'open_bugs':num_open_bugs, 'closed_bugs':num_closed_bugs})
