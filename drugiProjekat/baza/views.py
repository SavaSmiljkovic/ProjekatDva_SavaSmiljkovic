from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Car
from .forms import CarForm, SignUpForm, About


def index(req):
    if not req.user.is_authenticated:
        return render(req, 'index.html', {'page_title': 'Aplikacija'})
    else:
        return redirect('baza:cars')


@login_required
def cars(req):
    tmp = Car.objects.all()
    return render(req, 'cars.html', {'cars': tmp})


@login_required
def car(req, id):
    tmp = get_object_or_404(Car, id=id)
    return render(req, 'car.html', {'car': tmp, 'page_title': tmp.title})


@permission_required('baza.change_car')
def edit(req, id):
    if req.method == 'POST':
        form = CarForm(req.POST)

        if form.is_valid():
            a = Car.objects.get(id=id)
            a.title = form.cleaned_data['title']
            a.content = form.cleaned_data['content']
            a.save()
            return redirect('baza:cars')
        else:
            return render(req, 'edit.html', {'form': form, 'id': id})
    else:
        a = Car.objects.get(id=id)
        form = CarForm(instance=a)
        return render(req, 'edit.html', {'form': form, 'id': id})

@permission_required('baza.change_car')
def delete(req, id):
    # if req.method == 'POST':
        form = CarForm(req.POST)

        if form.is_valid():
            a = Car.objects.get(id=id)
            a.delete()
            return redirect('baza:cars')
        else:
            a = Car.objects.get(id=id)
            a.delete()
            return redirect('baza:cars')
            # return render(req, 'edit.html', {'form': form, 'id': id})
    # else:
    #     a = Car.objects.get(id=id)
    #     form = CarForm(instance=a)
    #     return render(req, 'edit.html', {'form': form, 'id': id})


@permission_required('baza.add_car')
def new(req):
    if req.method == 'POST':
        form = CarForm(req.POST)

        if form.is_valid():
            #a = Car(title=form.cleaned_data['title'], content=form.cleaned_data['content'], owner=req.user)
            a = Car(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            a.save()
            return redirect('baza:cars')
        else:
            return render(req, 'new.html', {'form': form})
    else:
        form = CarForm()
        return render(req, 'new.html', {'form': form})


def signUp(req):
    if req.method == 'POST':
        form = SignUpForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            firstName = form.cleaned_data.get('first_name')
            lastName = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User(first_name=firstName, last_name=lastName, username=username, email=email, password=password)
            # user = authenticate(username=username, password=password)
            # login(req, user)
            # user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(req, 'signup.html', {'form': form})


def about(req):
    if req.method == 'POST':
        #  form = About(req.POST)
        # if form.is_valid():
        #     form.save()
        username = User.get_username()
        firstName = User.get_short_name()
        lastName = User.get_last_name()
        email = User.get_email()
        return redirect('baza:cars')
    # else:
    #      form = About()
    return render(req, 'about.html')
