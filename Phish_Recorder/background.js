//Author: Karthika Subramani
//listener that listens to teh content scriipts
chrome.runtime.onConnect.addListener(function(port) {

chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  	console.log('connected to server');
	
 	//listens to messages from content script that are posted via PostMessage 
    	port.onMessage.addListener(function getResp(response) {
      	console.log(response.data);
	if(sessionStorage[tabs[0].id]==null)
		sessionStorage.setItem(tabs[0].id,JSON.stringify(response.data));
	else
	{
		console.log(sessionStorage[tabs[0].id]);
		var res=JSON.parse(sessionStorage[tabs[0].id])
		
		res.pages.push(response.data.pages[0]);
		sessionStorage.setItem(tabs[0].id,JSON.stringify(res));
		
	}
 	

	     	return true;
    	});
       port.onDisconnect.addListener(function() {
      console.log('port disconnected');
    });
  });

chrome.tabs.onRemoved.addListener(function (tabId){
	//sends the data to server page that stores the data in a  JSON file
	var res=JSON.parse(sessionStorage[tabId])
	//JSON data that is recorded throughout a session
        console.log('\nres'+JSON.stringify(res));
        sessionStorage[tabId]=null;
        $.post(
        'http://localhost/welcome.php',res,
        function(data){
       
        console.log("Data " + data);
        });
	
	

});

});


