var header = document.getElementById("friendDiv");
var btns = header.getElementsByClassName("btn");



for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    if(this.classList.contains("active")){
        this.classList.remove("active")
    }
    else{
        this.className += " active"

    }



  });
}