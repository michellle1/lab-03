# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Michelle Arredondo
- 

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

	RESTful APIs are scalable because there is little to no client-server interactions, which removes server load. 
	
	Source: AWS article 

Question 2: According to the definition of “resources” provided in the AWS article above, What are the resources the mail server is providing to clients?
	The resources the mail server provides to clients are mail entries that contain a recipient, sender, subject, and body. 

Question 3: What is one common REST Method not used in our mail server? How could we extend our mail server to use this method?
	We did not use PUT in our mail server. PUT can be used to "update existing resources on the server." We could extend our mail server and use PUT to be able to edit drafts of mail entries. 
	
	Source: AWS article

Question 4: Why are API keys used for many RESTful APIs? What purpose do they serve? Make sure to cite any online resources you use to answer this question!

	API keys help call on APIs and let RESTful API web services verify client identities. This way server resources are only sent to authorized clients. 
	
	source: AWS article 
	source: https://openweathermap.org/appid 
