# gcp-cv-connector

## License
_**THIS SCRIPT IS PROVIDED TO YOU "AS IS."  TO THE EXTENT PERMITTED BY LAW, QUALYS HEREBY DISCLAIMS ALL WARRANTIES AND LIABILITY FOR THE PROVISION OR USE OF THIS SCRIPT.  IN NO EVENT SHALL THESE SCRIPTS BE DEEMED TO BE CLOUD SERVICES AS PROVIDED BY QUALYS**_

## Description
The aim of this repository is to build a solution which will help you onboard multiple projects or all projects within an organization to Qualys CloudView. We have built a python program which will perform this solution.

> Deployment Options
* **An Organization** : To onboard **all** the projects in an organization
    * Input ```"all"``` in the projects field of [configuration file](/config.yml)
  
* **Multiple Projects within an organization** : To onboard selected projects within an organization
    * Input the complete path of CSV file containing the list of projects to be onboarded in the projects field of [configuration file](/config.yml)

This repository contains ==>

  1. [**Main Python Program**](/gcp-cv-connector.py) 
  2. [**configuration File**](/example/config.yml)
  3. [**CSV with list of ProjectIds**](/example/gcp-projectids.csv)
  4. [**Demo-Key**](/example/demokey.json)
  
## Usage

#### Get started 
  * Making the choice of deployment mode ``` All Projects in an organization or Multiple Projects within the organization ```
  
  * preparing the configuration file ( [An example](/example/config.yml))
      * _username: "Qualys username to call CloudView API"_
      * _password: "Qualys password to call CloudView API"_
      * _apiURL: "Qualys baseurl for CloudView API"_
      * _keyfile: "The configuration/key file downloaded for the service account "_
      * _projects: "Either the CSV containing list of projectIds or **all**"_
      * _debug: true/false_
      
  * preparing the csv file if deployment mode is not all the projects in an organization ( [An example](/example/gcp-projectids.csv))
      ProjectId |
      ---------|
      mikeshproject|
