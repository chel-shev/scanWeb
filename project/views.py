from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from project.models import PC, Data
from django.http import Http404


# Create your views here.
def show(request):
    users = PC.objects.all()
    ctx = {'users': users}
    return render(request, 'myView.html', ctx)


def toInt(inValue):
    if inValue != '':
        return int(float(inValue))
    else:
        return 0


def deleteItem():
    for i in range(22, 23):
        pc = PC.objects.get(id=i)
        print pc
        pc.delete()


def addData(request):
    data_pc = Data(
        id_pc=PC.objects.get(id=int(request.GET.get('id_pc'))),
        used_memory=toInt(request.GET.get('used_memory')),
        ram=toInt(request.GET.get('ram')),
        cpu_0=toInt(request.GET.get('cpu_0')),
        cpu_1=toInt(request.GET.get('cpu_1')),
        cpu_2=toInt(request.GET.get('cpu_2')),
        cpu_3=toInt(request.GET.get('cpu_3')),
        temp_0=toInt(request.GET.get('temp_0')),
        temp_1=toInt(request.GET.get('temp_1')),
        temp_2=toInt(request.GET.get('temp_2')),
        temp_3=toInt(request.GET.get('temp_3')),
    )
    data_pc.save()
    return HttpResponse('200')


def addPC(request):
    PC.objects.get(id=23).delete()
    PC.objects.get(id=24).delete()
    # try:
    #     pc = PC.objects.get(pc=request.GET.get('pc'))
    # except PC.DoesNotExist:
    #     pc = PC(pc=request.GET.get('pc'),
    #             os=request.GET.get('os'),
    #             distro=request.GET.get('distro'),
    #             isa=request.GET.get('isa'),
    #             kernel=request.GET.get('kernel'),
    #             cpu=request.GET.get('cpu'),
    #             memory=float(request.GET.get('memory')),
    #             ram=float(request.GET.get('ram')),
    #             swap=float(request.GET.get('swap')),
    #             high=float(request.GET.get('high')),
    #             crit=float(request.GET.get('crit')),
    #             limit=int(request.GET.get('crit')))
    #     pc.save()
    # return HttpResponse(pc.id)
    return HttpResponse(0)

