from django.shortcuts import render
# _*_coding:utf-8_*_
# Create your views here.




def getform(request):
    from .models import UsrInfo
    people = None
    people = UsrInfo.objects.filter(name="zhenge")
    if people :
        person = people[0]

    #
    # if request.method == "POST":
    #     items = UsrInfo.objects.filter(name="zhenge")
    #     for item in items :
    #         item.delete()
    #
    #     usr =  UsrInfo()
    #     usr.name = request.POST.get("name","")
    #     usr.email = request.POST.get("email","")
    #     usr.address = request.POST.get("address","")
    #     usr.message = request.POST.get("message","")
    #
    #     usr.save()

    # all_item = UsrInfo.objects.all()
    # for item in all_item:
    #     print item.name

    return render(request, 'mes_form.html', {
        "person": person
    })
