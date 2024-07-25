
import jsonParser as jp
import openAICall as llm
import json
import os

import datetime
current_time = datetime.datetime.now().strftime("%d-%m-%y_%H-%M-%S")

jsonFile = open(rf"{os.environ['USERPROFILE']}\OneDrive - Deloitte (O365D)\Gen AI\Patch Management v1\20240523_JSON_https_localhost_DVWA.json")
data1 = json.load(jsonFile)

# Location of the Vulnerable application (DVWA)
folder = rf"{os.environ['USERPROFILE']}\OneDrive - Deloitte (O365D)\Gen AI"    #r"C:\Users\msheoran\Desktop\Gen AI"

#Location of the Output
output = rf"{os.environ['USERPROFILE']}\OneDrive - Deloitte (O365D)\Gen AI\Patch Management v1\Reports"      #C:\Users\msheoran\Desktop\Gen AI\Patch Management\Reports

# def scanInfo (data):
#     return jp.scanInfromatin(data)  # rectify typos

def vulnInfo (data):
    allVulnDetails = jp.vulnerabilityInformation(data)

    for vuln in allVulnDetails:
        if(vuln["severity"] == "Critical" or vuln["severity"] == "High"): #or vuln["severity"] == "Medium"):
            if (vuln["loc_type"] == "file"):
                
                vulnFilePath = rf"{folder}{vuln["path"].replace("/","\\")}"
                vulnFile = open(vulnFilePath)
                #print(vulnFile.read())
                
                Prompt= f"""Fix a '{vuln["name"]}' vulnerability in below '{vuln["path"].rsplit('.', 1)[-1]}' code. Your goal is to provide the section of the original code that needs to be changed and only the new patch code which will fix the vulnerability.
    Below is the '{vuln["path"].rsplit('.', 1)[-1]}' code:
    {vulnFile.read()}
                """

                patchResult = llm.createPatch(Prompt)
                vuln.update({"PatchResultkkk": patchResult})
                print(vuln)

            elif (vuln["recommendation"] != ""):
                Prompt = vuln["recommendation"]
                patchResult = llm.createPatch(Prompt)
                vuln.update({"PatchResult jjj": patchResult})
                print(vuln)

            else:
                Prompt = f"""Fix a '{vuln["name"]}' with '{vuln["details"]}' details. Your goal is to provide the steps how to fix this vulnerability. Provide only the best answer briefly in 100 words. If the vulnerability is fixed by the latest version please give this as suggestion."""

                patchResult = llm.createRecommendation(Prompt)
                vuln.update({"PatchResultooo": patchResult})
                print(vuln)

    return allVulnDetails

def main():
    #result = vulnInfo (data1)
    result = jp.vulnerabilityInformation(data1)
    with open(rf"{output}\domain-{current_time}.json", "w") as outfile:
        json.dump(result, outfile)
    return result