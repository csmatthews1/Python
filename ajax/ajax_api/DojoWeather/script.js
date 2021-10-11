var tempMode = 0;  // 0 is deg C, 1 is deg F
var sanjose = "https://api.openweathermap.org/data/2.5/onecall?lat=37.3382&lon=-121.88&exclude=current,minutely,hourly,alerts&appid=90ea172a7bd00c8f43235b277faddc84&units=";
var burbank = "https://api.openweathermap.org/data/2.5/onecall?lat=34.1808&lon=-118.3090&exclude=current,minutely,hourly,alerts&appid=90ea172a7bd00c8f43235b277faddc84&units=";
var chicago = "https://api.openweathermap.org/data/2.5/onecall?lat=41.8781&lon=-87.6298&exclude=current,minutely,hourly,alerts&appid=90ea172a7bd00c8f43235b277faddc84&units=";
var dallas = "https://api.openweathermap.org/data/2.5/onecall?lat=32.7767&lon=-96.7970&exclude=current,minutely,hourly,alerts&appid=90ea172a7bd00c8f43235b277faddc84&units=";
var days = {
    0: "Sunday",
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday"
}

function initialize() {
    today = new Date();
    
    third = today.getDay()+2;
    if (third > 6) {
        third -= 7;
    }
    fourth = today.getDay()+3;
    if (fourth > 6) {
        fourth -= 7;
    }
    document.getElementById('third_day').innerText = days[third];
    document.getElementById('fourth_day').innerText = days[fourth];
    
    address = sanjose + 'metric';
    getWeather(address);

}
initialize();

function changeCity(id) {

    console.log(id)
    if(id == 'sanjose') {
        address = sanjose;
        document.getElementById('city').innerText = "San Jose";
    }
    else if (id == 'burbank'){
        address = burbank;
        document.getElementById('city').innerText = "Burbank";
    }
    else if (id == 'chicago'){
        address = chicago;
        document.getElementById('city').innerText = "Chicago";
    }
    else {
        address = dallas;
        document.getElementById('city').innerText = "Dallas";
    }
    tempUnits = 'metric'
    console.log(tempMode)
    if(tempMode == 1) {
        tempUnits = 'imperial'
    }
    address += tempUnits;
    getWeather(address);
}

function changeTemp(element) {
    var tempF = 0;
    var tempC = 0;

    if(element.value == "°C" && tempMode == 1) {
        tempMode = 0;
        console.log("Change to deg C");
        //Loop through the high temps and convert to deg C
        var highs = document.getElementsByClassName("high")
        for (var i=0; i < highs.length; i++) {
            tempF = parseInt(highs[i].innerText);
            tempC = Math.round((tempF - 32) * 5 / 9);
            highs[i].innerText = tempC + "°";
        }

        //Loop through the low temps and convert to deg F
        var lows = document.getElementsByClassName("low")
        for (var i=0; i < lows.length; i++) {
            tempF = parseInt(lows[i].innerText);
            tempC = Math.round((tempF - 32) * 5 / 9);
            lows[i].innerText = tempC + "°";
        }
    }
    if(element.value == "°F" && tempMode == 0) {
        tempMode = 1;
        console.log("Change to deg F");
        //Loop through the high temps and convert to deg F
        var highs = document.getElementsByClassName("high")
        console.log(highs);
        for (var i=0; i < highs.length; i++) {
            tempC = parseInt(highs[i].innerText)
            tempF = Math.round(tempC * 9 / 5 + 32);
            highs[i].innerText = tempF + "°";
        }

        //Loop through the low temps and convert to deg F
        var lows = document.getElementsByClassName("low")
        console.log(highs);
        for (var i=0; i < lows.length; i++) {
            tempC = parseInt(lows[i].innerText)
            tempF = Math.round(tempC * 9 / 5 + 32);
            lows[i].innerText = tempF + "°";
        }

    }
}
function accept() {
    document.getElementById("modal-dialog").remove();
}

async function getWeather(address) {
     // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch(address);

    // We then need to convert the data into JSON format.
    var weatherData = await response.json();

    imgs = document.getElementsByClassName('weather_img');
    descriptions = document.getElementsByClassName('description');
    highs = document.getElementsByClassName('high');
    lows = document.getElementsByClassName('low');

    for (i=0; i < 4; i++) {
        descriptions[i].innerText = weatherData.daily[i].weather[0].description;
        highs[i].innerText = Math.round(weatherData.daily[i].temp.max) + "°"
        lows[i].innerText = Math.round(weatherData.daily[i].temp.min) + "°"
        if(weatherData.daily[i].weather[0].main == "Clouds") {
            imgs[i].src = "assets/some_clouds.png"
        }
        else if (weatherData.daily[i].weather[0].main == "Clear") {
            imgs[i].src = "assets/some_sun.png"
        }
        else {
            imgs[i].src = "assets/some_rain.png"
        }
    }
    return weatherData;
}
