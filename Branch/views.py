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
			foll = requests.get(f"https://api.github.com/users/{user_name}/followers").json()
			half = int(len(foll)/2)
			print(half)
			followers1 = [follower["login"] for follower in foll[0:half]]
			followers2 = [follower["login"] for follower in foll[half:]]
			response = requests.get(f"https://api.github.com/users/{user_name}").json()
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
				"user_created_at" : response["created_at"],
				"user_blog" : response["blog"],
				"user_twitter" : response["twitter_username"],
				"user_email" : response["email"],
				"theme_right_now" : "",
				"followers_part1" : followers1,
				"followers_part2" : followers2,
			}
			context.update({"theme_right_now" : last_theme })
			return HttpResponseRedirect("dashboard")
		except:
			return HttpResponseRedirect("/")
	return render(request, "index.html", context)

def dashboard(request):
	global context
	global last_theme

	if (request.method == "POST" and "theme-option-button-dark" in request.POST):
		if (context["theme_right_now"] == "dark"):
			context.update({"theme_right_now" : "light"})
			Theme.objects.all().delete()
			Theme.objects.create(theme="Light")
			last_theme = "light"
		elif (context["theme_right_now"] == "light"):
			context.update({"theme_right_now" : "dark"})
			Theme.objects.all().delete()
			Theme.objects.create(theme="Dark")
			last_theme = "dark"
	return render(request, "dashboard.html", context)
