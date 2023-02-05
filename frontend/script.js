var returnInfo = {}
function NumHours()
{
    let x = document.getElementById('userInputBox1').value;
   
    //document.getElementById('userInputBox1').value = "";
   
    document.getElementById('demo').innerHTML = "Would you like to eat?";
    clickme();
}
function clickme()
{
    YesButton.classList.toggle("hide");
    NoButton.classList.toggle("hide");
    console.log(25)
}
function FoodYes()
{
    returnInfo['food'] = true;
   
    document.getElementById('demo2').innerHTML = "What type of places would you like to see?";
    userInputBox3.classList.toggle("hide2");
    sight.classList.toggle("hide2");
}

function FoodNo()
{
    returnInfo['food'] = false;
     
    document.getElementById('demo2').innerHTML = "What type of places would you like to see?";
    userInputBox3.classList.toggle("hide2");
    sight.classList.toggle("hide2");
}

function SightSeeing()
{


    let sights = document.getElementById('userInputBox3').value;
    returnInfo['Sights'] = sights;
    userInputBox4.classList.toggle("hide3");
    finisher.classList.toggle("hide3");
    document.getElementById('demo3').innerHTML = "How many miles away are you willing to travel?"


}
function SendOff()
{
  //give it to mlsa and mlha


}


