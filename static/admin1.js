
console.log('Hello There!')


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


