from django.shortcuts import render,  render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from Verwalter.forms import UserForm , UserProfileForm 
from django.contrib.auth import authenticate, login, logout 
from Verwalter.models import UserProfile
from django.contrib.auth.decorators import login_required


def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/Verwalter/')


def index(request):
	context = RequestContext(request)
	#The sending method must be a POST method so data can't be visible 
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		#authenticate function return an user object if the username 
		# and password combination or none if no Match is found
		if user:
			if user.is_active:
				login(request,user)
				obj = UserProfile.objects.get(user_id=user.id)
				if obj.user_level == "Admin": 
					return HttpResponseRedirect('/Verwalter/register/')
				elif obj.user_level == "MAG":
					return HttpResponseRedirect('/Verwalter/magtab/')
				else:
					return HttpResponseRedirect('/Verwalter/usertab/')
			else:
				return HttpResponse("Your account is disabled")
		else:
			print "Invalid login details: {0}, {1}".format(username,password)
			return HttpResponse("Invalid login details supplied")

	else:
		return render_to_response('Verwalter/index.html',{},context)
	#context_dict = {'boldmessage': "hallo ich bin da"}
	#return render_to_response('Verwalter/index.html', context_dict, context)


def register(request):
	context = RequestContext(request)
	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user=user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			if 'job_title' in request.FILES:
				profile.job_title = request.FILES['job_title']
			if 'user_level' in request.FILES:
				profile.user_level = request.FILES['user_level']
			profile.save()
			registered = True;
			context_dict = {'message':user.username}
		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render_to_response(
			'Verwalter/register.html',
			{'user_form':user_form, 'profile_form': profile_form, 'registered':registered},
			context)

def magtab(request):
	context = RequestContext(request)
	return render_to_response('Verwalter/magtab.html',{},context)

def usertab(request):
	context = RequestContext(request)
	return render_to_response('Verwalter/usertab.html',{},context)

