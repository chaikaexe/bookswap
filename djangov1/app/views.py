from django.shortcuts import render, redirect
from .models import BookSwap
from .forms import BookSwapForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import RegisterForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from app.forms import RegisterForm
from .forms import UserProfileForm


def index(request):
    swaps = BookSwap.objects.order_by('-id')
    return render(request, 'app/index.html', {'title': 'Страница обмена - BookSwap', 'swaps': swaps})



def about(request):
    return render(request, 'app/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = BookSwapForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:home')
        else:
            error = 'Заявка неверна'

    form = BookSwapForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'app/create.html', context)

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'app/profile.html', {'form': form})

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("app:profile")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)