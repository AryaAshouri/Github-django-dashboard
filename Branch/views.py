from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import *
import requests
app_name = "Branch"
context = {}

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from .models import *
import requests
app_name = "Branch"
context = {}
last_theme = "light"
def home(request):
	global context
	global last_theme
	if request.method == "POST" and "button-input" in request.POST:
		try:
			user_name = request.POST.get("username-input")
			response = requests.get(f"https://api.github.com/users/{user_name}").json()
			all_followers = requests.get(f"https://api.github.com/users/{user_name}/followers").json()

			first_half_followers = {}
			for follower in all_followers[0:int(len(all_followers)/2)]:
				first_half_followers.update({follower["login"] : follower["avatar_url"]})

			second_half_followers = {}
			for follower in all_followers[int(len(all_followers)/2):]:
				second_half_followers.update({follower["login"] : follower["avatar_url"]})

			context = {
				"user_username" : response["login"],
				"user_name" : response["name"],
				"user_id" : response["id"],
				"user_profile" : response["avatar_url"],
				"user_type" : response["type"],
				"is_user_admin" : response["site_admin"],
				"user_company" : response["company"],
				"user_location" : response["location"],
				"is_user_hireable" : response["hireable"],
				"user_bio" : response["bio"],
				"user_created_at" : response["created_at"][0:10],
				"user_blog" : response["blog"],
				"user_twitter" : response["twitter_username"],
				"user_email" : response["email"],
				"user_followers" : response["followers"],
				"user_following" : response["following"],
				"current_theme" : "",
				"first_half_followers" : first_half_followers,
				"second_half_followers" : second_half_followers,
			}
			context.update({"current_theme" : last_theme })
			return HttpResponseRedirect("dashboard")
		except:
			print(first_half_followers)
			return HttpResponseRedirect("/")
	return render(request, "index.html", context)

def dashboard(request):
	global context
	global last_theme

	if (request.method == "POST" and "change-theme-button" in request.POST):
		if (context["current_theme"] == "dark"):
			context.update({"current_theme" : "light"})
			Theme.objects.all().delete()
			Theme.objects.create(theme="Light")
			last_theme = "light"
		elif (context["current_theme"] == "light"):
			context.update({"current_theme" : "dark"})
			Theme.objects.all().delete()
			Theme.objects.create(theme="Dark")
			last_theme = "dark"
	return render(request, "dashboard.html", context)
