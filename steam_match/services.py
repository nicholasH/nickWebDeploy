import time

import requests
import json
from operator import itemgetter

from requests.exceptions import ConnectionError

from nickWebDeploy import settings


def getFriends(id):
    url = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?'
    params = {'key': settings.STEAM_KEY, 'steamid': id,"relationship":"friend"}
    r = requests.get(url, params=params)
    friendsListJson = r.json()
    friendIDlist=[]


    if len(friendsListJson) == 0:
        return friendIDlist

    friendslist = friendsListJson["friendslist"]["friends"]

    for friend in friendslist:
        friendIDlist.append(friend["steamid"])

    return friendIDlist

#todo make it so if a user has more then 100 friends this method get all of them
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

#todo make sure thing dont chrash when no one is selected
def getUserGames(id):
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?'
    params = {'key': settings.STEAM_KEY, 'steamid': id}
    r = requests.get(url, params=params)
    gamesList = r.json()
    games = gamesList["response"]["games"]
    turnList = []
    for game in games:
        turnList.append(game["appid"])
    return turnList


def getCommonGames(user,IDs):
    url = 'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?'

    userList = set(getUserGames(user))

    for id in IDs:
        glist = []
        params = {'key': settings.STEAM_KEY, 'steamid': id}
        r = requests.get(url, params=params)
        gamesList = r.json()
        games = gamesList["response"].get("games")

        if games is not None:
            for game in games:
                glist.append(game["appid"])

        userList = userList.intersection(glist)

    return userList



def getGamesInfo(games):
    url = 'https://store.steampowered.com/api/appdetails/basic?'
    gameList = []
    ok = True

    for game in games:
        params = {'key': settings.STEAM_KEY,'appids': game}
        try:
            r = requests.get(url, params=params)
        except ConnectionError as e:
            print(e)
            ok = False
            continue
        print(r)
        if r.status_code == 200:
            gameInfo = r.json()
            x = gameInfo[str(game)].get("data")

            if x is not None:
                gameList.append(x)
        elif r.status_code == 403:
            ok = False
            return [gameList,ok]
        else:
            ok = False


    return  [gameList,ok]



def getCommonGamesInfo(user,IDs):
    return getGamesInfo(getCommonGames(user, IDs))

def getSteamByURl(vanityURL):
    url = 'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?'
    params = {'key': settings.STEAM_KEY, 'vanityurl': vanityURL}
    r = requests.get(url, params=params)
    steamID = r.json()["response"].get("steamid")

    if steamID is not None:
        return steamID
    else:
        return ""

def getUserExists(id):
    url = 'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?'
    params = {'key': settings.STEAM_KEY, 'steamids': id}
    r = requests.get(url, params=params)
    players = r.json()["response"].get("players")

    if len(players) > 0:
        return True
    else:
        return False




what = "76561197993827038"
vaas = "76561198053222544"

ac = "AnAngelCried"

#test = getSteamByURl(ac)
#print(getCommonGamesInfo(what,[]))



#getFriendsInfoBySteamID("76561197993827038")
t = "76561197993827038"
test = ['76561198067123311', '76561198071982180', '76561197999136248', '76561198053222544']
