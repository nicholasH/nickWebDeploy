import requests
import json
from operator import itemgetter


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
    url = 'https://store.steampowered.com/api/appdetails?'
    gameList = []
    for game in games:
        params = {'appids': game}
        r = requests.get(url, params=params)
        gameInfo = r.json()
        x = gameInfo[str(game)].get("data")
        if x is not None:
            gameList.append(x)

    return  gameList



def getCommonGamesInfo(user,IDs):
    return getGamesInfo(getCommonGames(user, IDs))



vaas = "76561198053222544"
tecvdsf = getFriendsInfo(getFriends(vaas))

#getFriendsInfoBySteamID("76561197993827038")
t = "76561197993827038"
test = ['76561198067123311', '76561198071982180', '76561197999136248', '76561198053222544']
