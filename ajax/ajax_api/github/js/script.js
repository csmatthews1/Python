var url = "";

async function getInfo() {
    
    url = "https://api.github.com/users/"
    url += document.getElementById("user").value

    var response = await fetch(url);
    // We then need to convert the data into JSON format
    var coderData = await response.json();

    if (coderData.message == "Not Found") {
        document.getElementById("userinfo").style.display = "block"; // TypeError: failed to fetch
        document.getElementById("avatar").style.visibility = "hidden";
        document.getElementById("userinfo").innerText = "Could not find Github User"; // TypeError: failed to fetch
        return 0;
    }
    
    document.getElementById("userinfo").innerText = coderData.name + " has " + coderData.followers + " followers."
    document.getElementById("avatar").src = coderData.avatar_url;
    document.getElementById("userinfo").style.display = "block"; // TypeError: failed to fetch
    document.getElementById("avatar").style.visibility = "visible"; 
    return coderData;
}

