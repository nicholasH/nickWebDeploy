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
    status = True
    selectedFriends = None

    if request.method == 'POST':
        IDs = request.POST.getlist("selectFriend")
        gamesAndstatus = services.getCommonGamesInfo(steam_id,IDs)
        games = gamesAndstatus[0]
        status = gamesAndstatus[1]
        selectedFriends = services.getFriendsInfo(IDs)
        print(selectedFriends)
        print("status was "+ str(status))

        return render(request, template_name, {"playerInfos": data,
                                               "selectedFriends":selectedFriends,
                                               "commonGames": games,
                                               "status":status})
    else:
        return render(request, template_name, {"playerInfos": data,
                                               "status":status,
                                               "selectedFriends": selectedFriends})





