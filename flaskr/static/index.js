function ApplyFromInput() {
	var red = document.getElementById("red").value
	var green = document.getElementById("green").value
	var blue = document.getElementById("blue").value

	red = red ? Math.min(Math.max(parseInt(red), 0), 255) : 0
	green = green ? Math.min(Math.max(parseInt(green), 0), 255) : 0
	blue = blue ? Math.min(Math.max(parseInt(blue), 0), 255) : 0
	let displayColor = `rgb(${red}, ${green}, ${blue})`

	document.getElementById("colorDisplay").style.backgroundColor = displayColor

	sendColUpdate(red, green, blue)
}
function sendColUpdate(red, green, blue){
	const data = {red, green, blue};
	fetch('/', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify(data)
	})
}

function gotoSolid() {
	console.log("Solid")
}

function sendReboot(){
	console.log("Reboot")
}

function sendShutdown(){
	console.log("Shutdown")
	sendColUpdate(0, 0, 0);
}

function gotoFade() {
	console.log("Fade")
}

function gotoFlash() {
	console.log("Flash")
}


document.addEventListener("DOMContentLoaded", function() {
	cBoxes = document.querySelectorAll(".c-box");
	cBoxes.forEach(box => {
		box.onclick = function(){
			cBoxes.forEach(function(box){
				box.classList.remove('c-box-selected');
			});
			box.classList.add('c-box-selected');

			switch(box.id){
				case 'c-red':
					sendColUpdate(255, 0, 0);
					break;
				case 'c-green':
					sendColUpdate(0, 255, 0);
					break;
				case 'c-blue':
					sendColUpdate(0, 0, 255);
					break;
				case 'c-lightgreen':
					sendColUpdate(200, 255, 100);
					break;
				case 'c-white':
					sendColUpdate(255, 255, 255);
					break;
				case 'c-purple':
					sendColUpdate(255, 20, 255);
					break;
				default:
					break;
			}
		}
	})
});
