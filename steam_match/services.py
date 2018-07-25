import requests
import json
from operator import itemgetter


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

    turnlist = sorted(infoList, key=itemgetter('personaname'))

    return turnlist

def getFriendsInfoBySteamID(id):
    return getFriendsInfo(getFriends(id))

def getUserGames(ID):
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?'
    params = {'key': settings.STEAM_KEY, 'steamid': id}
    r = requests.get(url, params=params)
    gamesList = r.json()
    games = gamesList["response"]["games"]


def getCommonGames(IDs):
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?'
    gamelist = []
    for id in IDs:

        params = {'key': settings.STEAM_KEY, 'steamid': id}
        r = requests.get(url, params=params)
        gamesList = r.json()
        games = gamesList["response"]["games"]

        for game in games:

            gamelist.append(game["appid"])



    pass


#getFriendsInfoBySteamID("76561197993827038")

test = ['76561198053222544','76561197993827038']
getCommonGames(test)
