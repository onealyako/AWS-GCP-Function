O'Neal Yako
#1003370
Assignment 4 Read ME

-- Quick Comments --
	- In my Assignment4 folder, there is lambda_function.py (AWS)
	- There is a Google Cloud subfolder which contains python file for GCP ('function_gcp.py')
		- I have also included the requirements.txt that's generated automatically from 
		  the Google Cloud

-- AWS Steps --

	- Using the account provided by Deborah, I will run my oyako-s3-listener function 
 	  that is triggered every time an object is created in my S3 bucket. 

	- For every trigger, there is a copy of the file uploaded in my original 
	  S3 bucket 'cis4010-oyako' also uploaded to my backup 'cis4010-oyako-bucket'

	- Using CloudWatch, I log what  is occurring (ie. whether the file is uploaded or copied)

	- NOTE: Throughout the creation of the bucket and function, I must ensure I am in
		the same location. For AWS, I am in 'ca-central-1'

-- Google Cloud --

	- Using my personal GCP account, I will create a function located in the place I have 
	  my project created on the Google Cloud console. 
	
	- Location selected is us-east1 (South Carolina) for function and bucket creation.
	
	- The following is selected for triggering my function in GCP:
		- Trigger type: "Cloud Storage"
		- Event type: "Finalize/Create"
		- Bucket name: 'oyako-a4'

	- GCP already provides a log for me when I create/setup the trigger. All I do is 
	  implement the copy bucket information by adding 'from google.cloud import storage' to
	  the python file. I follow the Copying an object doc for Cloud Storage.

	- Logs will be found in the Logs Explorer. You will also notice that the object uploaded
	  is successfully copied to the backup bucket.  
