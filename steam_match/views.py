from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import resolve

from steam_match import services


def matcher(request):
    template_name = 'steam_match/matcher.html'

    if request.method == 'POST':
        print(request.POST.get("steamProfileID"))

        ID = request.POST.get("steamProfileID")

        return HttpResponseRedirect(ID)

    else:
        return render(request, template_name)


def friendSelector(request, steam_id):
    template_name = 'steam_match/friendSelector.html'
    print(steam_id)
    data = services.getFriendsInfoBySteamID(int(steam_id))
    print(data)
    if request.method == 'POST':
        IDs = request.POST.getlist("selectFriend")
        print(IDs)


    return render(request, template_name, {"playerInfos": data})


