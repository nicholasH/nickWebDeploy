import requests
import json

from nickWebDeploy import settings


def getFriends(id):
    url = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?'
    params = {'key': settings.STEAM_KEY, 'steamid': id,"relationship":"friend"}
    r = requests.get(url, params=params)
    friendsListJson = r.json()

    friendslist = friendsListJson["friendslist"]["friends"]

    friendIDlist=[]
    for friend in friendslist:
        friendIDlist.append(friend["steamid"])

    return friendIDlist


def getFriendsInfo(ids):
    idsStn = ",".join(ids)
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?'
    params = {'key': settings.STEAM_KEY, 'steamids': idsStn}
    r = requests.get(url, params=params)
    friendsInfoListJson = r.json()
    infoList = friendsInfoListJson["response"]["players"]
    return infoList

def getFriendsInfoBySteamID(id):
    return getFriendsInfo(getFriends(id))

def getUserGames(ID):
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?'
    params = {'key': settings.STEAM_KEY, 'steamid': id}
    r = requests.get(url, params=params)
    gamesList = r.json()




