import django.shortcuts
from .models import student as student_records

def student_list(request):
	return django.shortcuts.render(
		request,
		"main/home.html",
		{"students": student_records},
	)
