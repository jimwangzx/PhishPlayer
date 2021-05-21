

var port= chrome.runtime.connect()
console.log("connection established  "+port);
//listens to message from the web page
window.addEventListener("message", function(event) {
  if (event.source != window)
    return;    
    console.log("Content script received: " + event.data.text);
    //posts the form data to the server 
    port.postMessage({data: event.data.text});
    console.log('Messsage posted');
  
}, false);


var tags=['INPUT','TEXTAREA','LABEL','SELECT','KEYGEN']

// on successful load of the web page
document.addEventListener('DOMContentLoaded', function () {
	//gets invoked whenever a form is submitted
	$("form").submit(function( event ) {
		
 		var frm = $("form");
		var str='';
 		var frmData = JSON.stringify(frm.serializeArray());
		//Form data in the form of JSON 
		var data= JSON.parse(frmData);
		//Iterates through the form data to gather more information about the nodes 
  		for (var key in data) {
			
    			if (data.hasOwnProperty(key)) 
			{
				var elements= document.getElementsByName(data[key].name);
			
				var tag = elements[0].tagName;
				var type=elements[0].type;
				var nodeType=elements[0].getAttribute("type");
    				var val = data[key].value;
				if(tags.indexOf(tag)>=0)
					if(nodeType==null)
						str=str+ '{"'+"name"+'"'+":"+'"'+ data[key].name+'"'+","+'"'+"tag"+'"'+":"+'"'+tag+'"'+","+'"'+"type"+'"'+":"+'"'+nodeType+'"'+","+'"'+"value"+'"'+":"+'"'+val+'"},'
					else if(nodeType.toUpperCase()!='HIDDEN')
						str=str+ '{"'+"name"+'"'+":"+'"'+ data[key].name+'"'+","+'"'+"tag"+'"'+":"+'"'+tag+'"'+","+'"'+"type"+'"'+":"+'"'+nodeType+'"'+","+'"'+"value"+'"'+":"+'"'+val+'"},'
  			}
		}	
		str="{"+'"'+"url"+'"'+":"+'"'+window.location.href+'"'+","+ '"pages":[{'+ '"'+"formId"+'"'+":"+'"'+event.target.id+'"'+","+'"'+"values"+'"'+":"+"["+str.substring(0,str.length-1)+"]}]}";	

		//JSON data of one web page form that got submitted
		var jsonData=JSON.parse(str);
		console.log(JSON.parse(str));
		//posts message to the content script listener as it runs in an isolated environment
		window.postMessage({ type: "submit", text:jsonData,url:window.location.href}, "*");
	

	}); 
 
},false);



