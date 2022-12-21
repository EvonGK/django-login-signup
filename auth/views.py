from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages 
from django.shortcuts import redirect 
from django.contrib.auth import authenticate , login , logout

# Create your views here.
def home (request):
	return render(request,'index.html')


def signup (request):

	if request.method == 'POST' :
		username = request.POST['username']
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		myuser = User.objects.create_user(username,email,password1)
		myuser.first_name = firstname
		myuser.last_name = lastname

		myuser.save() 

		messages.success(request, "Your Account has been created successfully")

		# if password1 == password2:
		# 	if email.is_valid :
		# 		pass 
		
		# else:
		# 	return HttpResponse('passwords do not match')
		return redirect('signin')



	return render(request,'signup.html')

def signin (request):
	if request.method == 'POST':
		username = request.POST['username']
		password1 = request.POST['password1']

		user = authenticate( username = username, password=password1)
		if user is not None:
			login(request, user)
			firstname = user.first_name
			return render(request, 'index.html', {'firstname': firstname})
		
		else : 
			messages.error(request, 'Bad Creds')
			return redirect('home')

	
	return render(request,'signin.html')

def signout (request):
	logout(request)
	messages.success(request, "Logged Out Successfully!")
	return redirect('home')