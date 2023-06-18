console.log("test")

var oldValue = localStorage.getItem('name')

console.log(oldValue)

var newValue = document.querySelector("#result_list > tbody > tr:nth-child(1) > td.field-fullname").innerText

console.log(newValue)




localStorage.setItem('name', newValue)


if (oldValue === newValue) {

	console.log("No new information here")
}

else {
	console.log('There you go! New Arrived')
	bankName = document.querySelector("#result_list > tbody > tr:nth-child(1) > td.field-bankname").innerText
	var msg = new SpeechSynthesisUtterance();
	msg.text = "New Banking Details Submitted By" + newValue + "with bank name" + bankName;
	window.speechSynthesis.speak(msg);
}




    var time = new Date().getTime();
     $(document.body).bind("mousemove keypress", function(e) {
         time = new Date().getTime();
     });

     function refresh() {



         if(new Date().getTime() - time >= 5000)
             window.location.reload(true);
         else
             setTimeout(refresh, 5000);




     }


     setTimeout(refresh, 10000);

//myPreviousPassword = document.getElementsByClassName("field-password")[0];

oldName = document.querySelector("#result_list > tbody > tr:nth-child(1) > th")
console.log(oldName.innerText)




if (!window.Notification) {
    console.log('Browser does not support notifications.');
} else {
    // check if permission is already granted
    if (Notification.permission === 'granted') {
        // show notification here
    } else {
        // request permission from user
        Notification.requestPermission().then(function(p) {
           if(p === 'granted') {
               // show notification here
           } else {
               console.log('User blocked notifications.');
           }
        }).catch(function(err) {
            console.error(err);
        });
    }
}



newName = document.querySelector("#result_list > tbody > tr:nth-child(1) > th")
console.log(newName.innerText)


