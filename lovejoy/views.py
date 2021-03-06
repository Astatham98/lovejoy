from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from lovejoy.forms import SignUpForm
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from lovejoy.forms import SignUpForm, EvaluationsForm, CaptchForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from lovejoy.tokens import account_activation_token
from .models import Evaluation
from django.core.mail import EmailMessage


@login_required
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            email_id = request.POST['email']
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Lovejoy Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            email = EmailMessage(subject, message, to=[email_id])
            print('got here')
            email.send(fail_silently=False)
            print('you also got here')
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            pass
    return render(request, 'login.html')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html')

@login_required
def evaulation_view(request):
    if request.method == 'POST':
        form = EvaluationsForm(request.POST, request.FILES)
        if form.is_valid():
            form.user = request.user.username
            print(form.user)
            form.save()

            form = EvaluationsForm()
            return render(request, 'evaluation.html', {'form': form})
    else:
        form = EvaluationsForm()
    return render(request, 'evaluation.html', {'form': form})

@login_required
def staff_view(request):
    evaluation_list = Evaluation.objects.all()
    return render(request, 'staff_view.html',{
        'evaluation_list': evaluation_list
    })