1. Enable access to few API's in API library for project:
     * For all projects to be onboarded, navigate to API & Services > Library and enable Cloud Resource Manager API, Compute Engine API, Kubernetes Engine API and Cloud SQL Admin API from the API library. 
![Image1](/example/images/1.png) 
![Image2](/example/images/2.png) 
![Image3](/example/images/3.png)
![Image4](/example/images/4.png)


2. Create a service account in any project and download a configuration file: 
      * Navigate to IAM & admin > Service accounts and click CREATE SERVICE ACCOUNT. Provide a name and description (optional) for the service account and click CREATE. 
      
![Image5](/example/images/5.png)
![Image6](/example/images/6.png)
![Image7](/example/images/7.png)

      * Click CREATE KEY.  Select JSON as Key type and click CREATE. A message saying “Private key saved to your computer” is displayed and the JSON file is downloaded to your computer. Click CLOSE and then click DONE. 
      
![Image8](/example/images/8.png)
![Image9](/example/images/9.png)


3. Attach role (Resource Manager -> Organization Viewer, Folder Viewer, Project Viewer and    IAM -> Security Reviewer) to the Service account created in step1: 
      * Navigate to Organization 
      * Navigate to IAM & admin > IAM 
      * Click on ADD tab 
![Image10](/example/images/10.png)

      * Paste the service account email address in the New member field 
![Image11](/example/images/11.png)

      * Add roles mentioned above in the Role field and click on CONTINUE 
![Image12](/example/images/12.png)
