1. Enable access to few API's in API library for project:
      * For all projects to be onboarded, navigate to API & Services > Library and enable Cloud Resource Manager API, Compute Engine API, Kubernetes Engine API and Cloud SQL Admin API from the API library. 
[Image1](/image/1.png)
2. Create a service account in any project and download a configuration file: 
      * Navigate to IAM & admin > Service accounts and click CREATE SERVICE ACCOUNT. Provide a name and description (optional) for the service account and click CREATE. 
      * Click CREATE KEY.  Select JSON as Key type and click CREATE. A message saying “Private key saved to your computer” is displayed and the JSON file is downloaded to your computer. Click CLOSE and then click DONE. 

3. Attach role (Resource Manager -> Organization Viewer, Folder Viewer, Project Viewer and    IAM -> Security Reviewer) to the Service account created in step1: 
      * Navigate to Organization 
      * Navigate to IAM & admin > IAM 
      * Click on ADD tab 
      * Paste the service account email address in the New member field 
      * Add roles mentioned above in the Role field and click on CONTINUE 
       
