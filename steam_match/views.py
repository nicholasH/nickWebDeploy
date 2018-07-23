from django.shortcuts import render

from steam_match import services


def matcher(request):
    template_name = 'steam_match/matcher.html'

    if request.method == 'POST':
        print(request.POST.get("steamProfileID"))

        ID = request.POST.get("steamProfileID")
        data = services.getFriends(ID)
        print(data)


    return render(request,template_name)

