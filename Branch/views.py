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
			foll = requests.get(f"https://api.github.com/users/{user_name}/followers").json()
			followers1 = [follower["login"] for follower in foll[0:int(len(foll)/2)]]
			followers2 = [follower["login"] for follower in foll[int(len(foll)/2):]]
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
				"followers_part1" : followers1,
				"followers_part2" : followers2,
			}
			context.update({"current_theme" : last_theme })
			return HttpResponseRedirect("dashboard")
		except:
			return HttpResponseRedirect("/")
	return render(request, "index.html", context)

def dashboard(request):
	global context
	global last_theme

	if (request.method == "POST" and "change-theme-button" in request.POST):
		print("*****************************", context["current_theme"])
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
