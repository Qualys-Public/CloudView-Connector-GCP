from google.cloud import resource_manager
import json
import base64
import sys
import requests
import yaml
import time
import os
import csv

def config():
    with open('config.yml', 'r') as config_settings:
        config_info = yaml.load(config_settings)
        username = str(config_info['defaults']['username']).rstrip()
        password = str(config_info['defaults']['password']).rstrip()
        URL = str(config_info['defaults']['apiURL']).rstrip()
        keyfile = str(config_info['defaults']['keyfile']).rstrip()
        projects = str(config_info['defaults']['projects']).rstrip()
        debug = config_info['defaults']['debug']
        if username == '' or password == '' or URL == '' or keyfile == '' or projects == '':
            print "Config information in ./config.yml not configured correctly. Exiting..."
            sys.exit(1)
    return username, password, URL, keyfile, projects, debug

def Post_Call(username,password,URL,keyfile,data_connector):
    usrPass = str(username)+':'+str(password)
    b64Val = base64.b64encode(usrPass)
    headers = {
        'Accept': 'application/json',
        'Authorization': "Basic %s" % b64Val
    }
    files = {
        'configFile': (keyfile, open(keyfile, 'rb')),
    } 
    try:
        r = requests.post(URL, headers=headers,data=data_connector , files=files,verify=False)
        #print (r.json()) Enable for debugging
    except Exception as e:
        print (e)
    return r.raise_for_status()

def Add_GCP_Connector():
    username, password, URL, keyfile, projects, debug = config()
    URL = URL + "/cloudview-api/rest/v1/gcp/connectors"
    print '------------------------------GCP Connectors--------------------------------'
    if not os.path.exists("debug"):
        os.makedirs("debug")
    debug_file_name = "debug/debug_file"+ time.strftime("%Y%m%d-%H%M%S") + ".txt"
    debug_file = open(debug_file_name, "w")
    debug_file.write('------------------------------GCP Connectors--------------------------------' + '\n')
    
    client = resource_manager.Client()
    #List all projects you have access to
    abc = []
    if projects.lower() == "all":
        for project in client.list_projects():
            abc.append(json.dumps(project.project_id))
    else:
        with open(projects, 'rb') as f:
            reader = csv.DictReader(f)
            a = list(reader)
            for i in a:
                abc.append(i['ProjectId'])
            f.close()

    counter=0   
    for project in abc:
        with open(keyfile,"r") as fil:
            json_data = json.load(fil)
            json_data['project_id'] = project.strip('\"')
        with open(keyfile,"w") as fil:
            json.dump(json_data, fil, indent=2)
        counter += 1
        print str(counter) + ' : GCP Connector'
        print 'Project ID : ' + str(json_data['project_id'])
        debug_file.write(str(counter)  + ' : Project ID :  ' + str(json_data['project_id']) + '\n')

        data_connector = {
            "name": str(json_data['project_id'])
        }

        try:
            Post_Call(username, password, URL, keyfile, data_connector)
            print str(counter) + ' : Connector Added Successfully'
            print '-------------------------------------------------------------'
            debug_file.write(str(counter) + ' : Connector Added Successfully' + '\n\n')

        except requests.exceptions.HTTPError as e:  # This is the correct syntax
            print str(counter) + ' : Failed to Add GCP Connector'
            print e
            print '-------------------------------------------------------------'
            debug_file.write(str(counter) + ' : Failed to Add GCP Connector' + '\n')
            debug_file.write(str(e) + '\n\n')

    debug_file.close()

Add_GCP_Connector()
