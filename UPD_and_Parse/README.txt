UPD/Parser services:
UPD:
	Security (verify information is from the actual device)
	Receives information as the hex block thing and sends it to Kubernetes
Parser:
	Kubernetes receives information from UPD
	Kubernetes sends it to one of multiple parsers
		Do we really want to do this part? If we have a guaranteed thruput of once per second, is there a need to distribute it rather than completing each info extraction individually?
	Parser takes hex block and interprets into an object
		Here is where I see Kubernetes being more useful? Can use microservice to understand what info to send to the multiple microservices and then send the smaller info to the said microservices
	Microservices responds with relevant information
	Saves object as JSON (Or a custom object determined by the larger overall service) and sends to next microservice
