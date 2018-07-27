var header = document.getElementById("friendDiv");
var btns = header.getElementsByClassName("btn");

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    if(this.classList.contains("active")){
        this.classList.remove("active")
        var checks = this.getElementsByTagName("input")
        checks[0].checked = false
        console.log(checks)



    }
    else{
        this.className += " active"
        var checks = this.getElementsByTagName("input")
        checks[0].checked = true
        console.log(checks)

    }



  });
}


function showAll(){
    var header = document.getElementById("commonGamesDiv");
    var games = header.getElementsByClassName("game");

    for(var i = 0; i < games.length; i++){

        games[i].style = "display: inline-block;"

     }


}


function showCoOp(){
    var header = document.getElementById("commonGamesDiv");
    var games = header.getElementsByClassName("game");

    for(var i = 0; i < games.length; i++){
        var isMulti = false

        var meta = games[i].getElementsByClassName("GameMeta")
        var ids = meta[0].getElementsByClassName("catID")

            for(var x =  0;x < ids.length; x++){
                id = ids[x]

                //if not in list
                if ('38' === id.textContent) {
                    isMulti = true

                }
            }


        if(!isMulti){
            console.log(games[i])
            games[i].style = "display: none;"
        }
        else{
            games[i].style = "display: inline-block;"
        }

     }

}




function getMuti() {
    var header = document.getElementById("commonGamesDiv");
    var games = header.getElementsByClassName("game");

    for(var i = 0; i < games.length; i++){
        var isMulti = false

        var meta = games[i].getElementsByClassName("GameMeta")
        var ids = meta[0].getElementsByClassName("catID")

            for(var x =  0;x < ids.length; x++){
                id = ids[x]

                //if not in list
                if (['1', '20', '27','36','38'].indexOf(id.textContent) >= 0) {
                    isMulti = true

                }

            }


        if(!isMulti){
            games[i].classList.remove("show");
            games[i].classList.add("hidden");
        }
        else{
            games[i].classList.remove("hidden");
            games[i].classList.add("show");
        }

     }
}

function getRandom(){
    var header = document.getElementById("commonGamesDiv");
    var games = header.getElementsByClassName("game");
    var randomDiv = document.getElementById("randomGame");


    var shownGames =[]
    for(var i = 0; i < games.length; i++){
         console.log(games[i].style)
        if(games[i].classList.contains("show")){


            shownGames.push(games[i])

        }


     }
     while (randomDiv.firstChild) {
        randomDiv.removeChild(randomDiv.firstChild);
     }

     randomDiv.appendChild(shownGames[Math.floor(Math.random() * shownGames.length +1)])
}

//todo make it so I just need to sent the page the appID and the page get the page info later.

var header = document.getElementById("commonGamesDiv");
var games = header.getElementsByClassName("game");
var steamURL = 'https://store.steampowered.com/api/appdetails?appids='

for(var i = 0; i < games.length; i++){
    var game, obj, dbParam, xmlhttp, myObj, x, gib, txt = ""

    game = games[i]
    steamId = game.id
    console.log(steamId)

    steamURL = 'https://store.steampowered.com/api/appdetails?appids=' + steamId
    gib = 'https://ghibliapi.herokuapp.com/films'
    test = "https://steam.cmandersen.com/categories"

    var request = new XMLHttpRequest();
    //request.open('GET', gib, true);
    request.open('GET', test, true);

    request.onload = function () {

  // Begin accessing JSON data here
  var data = JSON.parse(this.response);
  if (request.status >= 200 && request.status < 400) {
      console.log(data)
  } else {
    console.log("Not working")
  }
}

request.send();



}



