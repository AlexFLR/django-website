from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):

	records = Record.objects.all()


	# Check to see if logging in
	if request.method =="POST":
		username = request.POST['username']
		password = request.POST['password']
		#Auth
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request,user)
			messages.success(request,"You have been logged in!")
			return redirect('home')
		else:
			messages.success(request,"Username or password inccorect. Try again!")
			return redirect('home')	
	else:
		return render(request,'home.html',{'records': records});	
	


def logout_user(request):
	logout(request)
	messages.success(request,"You have been logged out...")
	return redirect('home')



def register_user(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			#Authenticate user
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username,password=password)
			login(request,user)
			messages.success(request,"You have successfully register !")
			return redirect('home')
	else:
		form = SignUpForm()	
		return render(request,'register.html',{'form':form});
	return render(request,'register.html',{'form':form});


def user_record(request, pk):
	if request.user.is_authenticated:
		#Look up records
		user_record = Record.objects.get(id = pk)
		return render(request,'record.html',{'user_record': user_record});
	else:
		messages.success(request,"You must be logged in to view this page.")
		return redirect('home')


def delete_record (request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delete_it.delete()
		messages.success(request,'Record deleted successfully!')
		return redirect( 'home')
	else:
		messages.success(request,'U must be logged in to delete this record!')
		return redirect( 'home')


def add_record(request):
		form = AddRecordForm(request.POST or None)
		if request.user.is_authenticated:
			if request.method == "POST":
				if form.is_valid():
					add_record = form.save()
					messages.success(request,"Record Added")
					return redirect('home')	
			return render(request,'add_record.html',{'form':form});
		else:
			messages.success("U are not authenticated. U must be logged in! ")
			return redirect('home')		