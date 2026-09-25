const API_URL = "http://127.0.0.1:8000/";

function checkName(){
    if (localStorage.getItem("username")){
        document.getElementById("nameForm").classList.add("hidden");
        document.getElementById("main2").classList.remove("hidden");
    }
}

function confirmUsername(){
    let name = docuemnt.getElementById("nameInput").value.trim();
    if (name.length < 3) {
        document.getElementById("msg").innerHTML = "Name must be atleast 3 characters long";
        return;
    }
    
    if (name.length > 20) {
        document.getElementById("msg").innerHTML = "Name must be atmost 20 character long";
        return;
    }

    localStorage.setItem("username", name);
    checkName();
}