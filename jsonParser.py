import json

# To add comments for better readability
# To rectify typos


def scanInformation (data):
    host = data["export"]["scans"][0]["info"]["host"]
    start_date = data["export"]["scans"][0]["info"]["start_date"]
    end_date = data["export"]["scans"][0]["info"]["end_date"]
    start_url = data["export"]["scans"][0]["info"]["start_url"]
    duration = data["export"]["scans"][0]["info"]["duration"]
    server = data["export"]["scans"][0]["info"]["server"]
    
    information = {
    "Host": host,
    "StartDate": start_date,
    "EndDate": end_date,
    "StartUrl": start_url,
    "Duration": duration,
    "Server" : server
    }    

    return information

def vulnerabilityInformation (data):
    scanInfo = scanInformation(data)
    vulnerabilityTypes = data["export"]["scans"][0]["vulnerability_types"]
    vulnerabilities = data["export"]["scans"][0]["vulnerabilities"]
    location = data["export"]["scans"][0]["locations"]
    finalData = []

    for i in vulnerabilities:
        vulnerabilitiesId = i["info"]["vt_id"]
        vulnerabilitiesLocId = i["info"]["loc_id"]
        
        for x in vulnerabilityTypes:
            vulnerabilityTypesId = x["vt_id"]

            for j in location:
                locationId =  j["loc_id"]

                if (vulnerabilitiesId == vulnerabilityTypesId):
                    
                    if (vulnerabilitiesLocId == locationId):
                        if (x["severity"] == 4):
                            severity = "Critical"
                        elif (x["severity"] == 3):
                            severity = "High"
                        elif (x["severity"] == 2):
                            severity = "Medium"
                        elif (x["severity"] == 1):
                            severity = "Low"
                        elif (x["severity"] == 0):
                            severity = "Information"
                        finalDataInfo = {
                            "vt_id"         : i["info"]["vt_id"],
                            "name"          : i["info"]["name"],
                            "loc_url"       : i["info"]["loc_url"],
                            "status"        : i["info"]["status"],
                            "loc_detail"    : i["info"]["loc_detail"],
                            "details"       : i["info"]["details"],
                            "path"          : j["path"],
                            "loc_type"      : j["loc_type"],
                            "impact"        : x["impact"],
                            "description"   : x["description"],
                            "recommendation": x["recommendation"],
                            "cvss4_score"   : x["cvss4_score"],
                            "severity"      : severity
                        }

                        finalData.append(finalDataInfo)
    finalDataJson = {
        "scanInfo":scanInfo,
        "vulnInfo":finalData
        }
                        
    return finalDataJson