from django.shortcuts import render
from AnonymousBin.models import msg

# Create your views here.

def create(request):
	if request.method != 'POST':
		return render(request,'create.html')
	m = msg.objects.filter(status=0).order_by("id")
	if m :
		m = m[0]
	else:
		m = msg()
	m.text = request.POST['text']
	m.status = 1
	m.save()
	return render(request,'select.html',locals())

def select(request,id_num):
	m = msg.objects.get(id=id_num)
	m.status = 0
	m.save()
	return render(request,'select.html',locals())
