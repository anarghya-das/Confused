function clickTweet() {
	var xhttp = new XMLHttpRequest();
	xhttp.open('GET', '/tweet');
	xhttp.send();
	alert('Tweeted!');
}
