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

    if request.method == 'POST':
        IDs = request.POST.getlist("selectFriend")
        games = services.getCommonGamesInfo(steam_id,IDs)

        selectedFriends = services.getFriendsInfo(IDs)

        print(IDs)
        print(data)
        return render(request, template_name, {"playerInfos": data,"selectedFriends":selectedFriends, "commonGames": games})
    else:
        return render(request, template_name, {"playerInfos": data})





