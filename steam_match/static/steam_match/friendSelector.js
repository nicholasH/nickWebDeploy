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

        games[i].classList.remove("hidden");
        games[i].classList.add("show");
     }


}


function showCoOp(){
    var header = document.getElementById("commonGamesDiv");
    var games = header.getElementsByClassName("game");

    for(var i = 0; i < games.length; i++){
        var isCoOp = false

        var meta = games[i].getElementsByClassName("GameMeta")
        var ids = meta[0].getElementsByClassName("catID")

            for(var x =  0;x < ids.length; x++){
                id = ids[x]

                //if not in list
                if ('38' === id.textContent) {
                    isCoOp = true

                }
            }


        if(!isCoOp){
            games[i].classList.remove("show");
            games[i].classList.add("hidden");
        }
        else{

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
        if(games[i].classList.contains("show")){


            shownGames.push(games[i])

        }
     }
     while (randomDiv.firstChild) {
        randomDiv.removeChild(randomDiv.firstChild);
     }
     var gameDiv = shownGames[Math.floor(Math.random() * shownGames.length)]
     randomDiv.appendChild(gameDiv.cloneNode(true))
}





