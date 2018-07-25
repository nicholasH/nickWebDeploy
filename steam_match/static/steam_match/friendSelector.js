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