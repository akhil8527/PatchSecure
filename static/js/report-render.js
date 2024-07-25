
// This function is used for rendering the reports 
function reportRender (results){

    //getting the placeholder Id from html file - scan-info
    const scanDiv = document.getElementById('scan-info');
    scanDiv.innerHTML = '';
    
    //Creating <div> function with classname as scanResultDiv
    const scanResultDiv = document.createElement('div');
    scanResultDiv.className = 'scanResultDiv';

    //Creating <div> function with classname as scanInfoDiv
    const scanInfoDiv = document.createElement('div');
    scanInfoDiv.className = 'scanInfoDiv';

    //function used to append elements to the scanInfoDiv
    function appendScanInformation(titleInfo, keyInfo, ScanInfo) {
        const p = document.createElement('p');
        // const header = document.createElement('header');
        // header.className = keyInfo;
        // p.className = `Scan${keyInfo}`
        // header.textContent = `${titleInfo}:`;
        p.textContent = `${titleInfo}: ${ScanInfo}`;
        // scanInfoDiv.appendChild(header);
        scanInfoDiv.appendChild(p);   
    }

    //appending each values
    appendScanInformation("Host","Host",results.scanInfo.Host)
    appendScanInformation("Start Date","StartDate",results.scanInfo.StartDate)
    appendScanInformation("End Date","EndDate",results.scanInfo.EndDate)
    appendScanInformation("Star Url","StartUrl",results.scanInfo.StartUrl)
    appendScanInformation("Duration","Duration",results.scanInfo.Duration)
    appendScanInformation("Server" ,"Server",results.scanInfo.Server)
     
    //getting the placeholder Id from html file - output
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = '';

    //for loop to read each vulnerability
    results.vulnInfo.forEach(result => {

        //Creating <div> function with classname as result
        const resultDiv = document.createElement('div');
        resultDiv.className = 'result';

        //Creating <div> function with classname as result-header
        const resultHeader = document.createElement('div');
        resultHeader.className = 'result-header';

        //Creating <h2> function to disply the heading of severity: vuln name
        const nameP = document.createElement('h2');
        nameP.textContent = `${result.severity}: ${result.name}`;
        nameP.style.cursor = 'pointer';

        //Creating <h2> function to disply the heading of status: open
        const statusP = document.createElement('h2');
        statusP.textContent = `Status: ${result.status}`;
        statusP.style.marginLeft = 'auto';

        //Append the information to parent element
        resultHeader.appendChild(nameP);
        resultHeader.appendChild(statusP);
        resultDiv.appendChild(resultHeader);

        const vulnDataDiv = document.createElement('div');
        vulnDataDiv.className = 'vulnerability-info';

        const additionalInfoDiv = document.createElement('div');
        additionalInfoDiv.className = 'additional-info';

        // for (const key in result) {
        //     if (result.hasOwnProperty(key) && key !== 'name') {
        //         const p = document.createElement('p');
        //         const header = document.createElement('header');
        //         header.className = key;
        //         p.className = `Result${key}`
        //         header.textContent = key;
        //         p.textContent = result[key];
        //         additionalInfoDiv.appendChild(header);
        //         additionalInfoDiv.appendChild(p);
        //     }
        // }
        
        const div = document.createElement('div');
        div.className = "seprator-bold-green";
        vulnDataDiv.appendChild(div);

        function appendResultInformation(titleInfo, keyInfo, ResultInfo) {
            const p = document.createElement('p');
            const header = document.createElement('header');
            header.className = keyInfo;
            p.className = `Result${keyInfo}`
            header.textContent = `${titleInfo}:`;
            p.textContent = ResultInfo;
            additionalInfoDiv.appendChild(header);
            additionalInfoDiv.appendChild(p);   
        }

        appendResultInformation("Affected URLs","loc_url",result.loc_url)
        appendResultInformation("Description","description",result.description)
        appendResultInformation("Impact","impact",result.impact)
        appendResultInformation("Recommendation","recommendation",result.recommendation)
        appendResultInformation("Patch Result","PatchResult",result.PatchResult)


        scanResultDiv.appendChild(scanInfoDiv);
        scanDiv.appendChild(scanResultDiv);

        vulnDataDiv.appendChild(additionalInfoDiv);
        resultDiv.appendChild(vulnDataDiv);
        outputDiv.appendChild(resultDiv);   

        //To show details of the vulnerability after clicking the title
        resultHeader.addEventListener('click', () => {
            const isHidden = vulnDataDiv.style.display === 'none' || vulnDataDiv.style.display === '';
            vulnDataDiv.style.display = isHidden ? 'block' : 'none';
        });
    });

    document.getElementById('output-title').style.display = 'block';
    document.getElementById('scan-title').style.display = 'block';
           
}

document.addEventListener('DOMContentLoaded', reportRender);
