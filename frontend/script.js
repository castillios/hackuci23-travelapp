var returnInfo = {}
var t = false;
var t1 = false;
var t2 = false;
var t3 = false;


function NumHours()
{


    let x = document.getElementById('userInputBox1').value;
    returnInfo['numHours'] = x;
    //document.getElementById('userInputBox1').value = "";
   
    document.getElementById('demo').innerHTML = "Would you like to eat?";
    clickme();
}
function clickme()
{
    if(t === false)
    {
    YesButton.classList.toggle("hide");
    NoButton.classList.toggle("hide");  
    console.log(25)
    t = true;
    }
}
function FoodYes()
{
    returnInfo['food'] = true;
   
    document.getElementById('shadow').innerHTML = "What type of food would you like?";
    if(t1 === false)
    {
        shadowUser.classList.toggle('shadowHide');
        infiniteButton.classList.toggle('shadowHide');
        t1 = true;
    }
   
}
function Shadow()
{


    returnInfo['typeFood'] = document.getElementById('shadow').value;
    if(t2 === false)
    {
        document.getElementById('demo2').innerHTML = "What type of places would you like to see?";
    userInputBox3.classList.toggle("hide2")
    sight.classList.toggle("hide2");
    t2 = true;
    }


}
function FoodNo()
{
    returnInfo['food'] = false;
     
    document.getElementById('demo2').innerHTML = "What type of places would you like to see?";
    if(t2 === false)
    {
    userInputBox3.classList.toggle("hide2")
    sight.classList.toggle("hide2");
    t2 = true;
    }
}


function SightSeeing()
{


    let sights = document.getElementById('userInputBox3').value;
    returnInfo['Sights'] = sights;
    if(t3 === false)
    {
        userInputBox4.classList.toggle("hide3");
        finisher.classList.toggle("hide3");
        document.getElementById('demo3').innerHTML = "How many miles away are you willing to travel?"
        t3 = true;
    }
}
function SendOff()
{
  returnInfo["numHrs"] = document.getElementById('userInputBox4').value;
  //give it to mlsa and mlha
  let serverUrl= "https://26a1-169-234-111-136.ngrok.io?numActivites=" + returnInfo['numHours'] + "&food=" + returnInfo['food'] +
   "&Sights=" + returnInfo['Sights'] + "&Miles=" + returnInfo['numHrs'] +'&Preference' + returnInfo[typeFood];  
  fetch(serverUrl, {headers: new Headers({"ngrok-skip-browser-warning": "Sdf"})})
        .then(res => res.json())
        .then(data => {
            console.log(data)
            //document.getElementById('display').innerHTML = data.message
        })


}
