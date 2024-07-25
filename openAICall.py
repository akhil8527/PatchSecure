from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = "gpt-4o"

def createPatch (prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are highly experienced developer, who provides patch code to fix vulnerabilities without altering any variable names and other functionality."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens = 300
    )

    return response.choices[0].message.content


def createRecommendation (prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are highly experienced developer, who provides steps to fix vulnerabilities."},
            {"role": "user", "content": prompt},
        ],
        temperature=0,
        max_tokens = 300
    )

    return response.choices[0].message.content

"""Fix a XXS vulnerability in below PHP code. Your goal is to provide the section of the original code that needs to be changed and only the new patch code which will fix the vulnerability.
        Below is the PHP code:
<?php
 
define( 'DVWA_WEB_PAGE_TO_ROOT', '../' );
require_once DVWA_WEB_PAGE_TO_ROOT . 'dvwa/includes/dvwaPage.inc.php';
 
dvwaPageStartup( array( 'authenticated' ) );
 
$page = dvwaPageNewGrab();
$page[ 'title' ] .= 'Source' . $page[ 'title_separator' ].$page[ 'title' ];
 
if (array_key_exists ("id", $_GET) && array_key_exists ("security", $_GET)) {
	$id       = $_GET[ 'id' ];
	$security = $_GET[ 'security' ];
 
 
	switch ($id) {
		case "fi" :
			$vuln = 'File Inclusion';
			break;
		case "brute" :
			$vuln = 'Brute Force';
			break;
		case "csrf" :
			$vuln = 'CSRF';
			break;
		case "exec" :
			$vuln = 'Command Injection';
			break;
		case "sqli" :
			$vuln = 'SQL Injection';
			break;
		case "sqli_blind" :
			$vuln = 'SQL Injection (Blind)';
			break;
		case "upload" :
			$vuln = 'File Upload';
			break;
		case "xss_r" :
			$vuln = 'Reflected XSS';
			break;
		case "xss_s" :
			$vuln = 'Stored XSS';
			break;
		case "weak_id" :
			$vuln = 'Weak Session IDs';
			break;
		case "javascript" :
			$vuln = 'JavaScript';
			break;
		case "authbypass" :
			$vuln = 'Authorisation Bypass';
			break;
		case "open_redirect" :
			$vuln = 'Open HTTP Redirect';
			break;
		default:
			$vuln = "Unknown Vulnerability";
	}
 
	$source = @file_get_contents( DVWA_WEB_PAGE_TO_ROOT . "vulnerabilities/{$id}/source/{$security}.php" );
	$source = str_replace( array( '$html .=' ), array( 'echo' ), $source );
 
	$js_html = "";
	if (file_exists (DVWA_WEB_PAGE_TO_ROOT . "vulnerabilities/{$id}/source/{$security}.js")) {
		$js_source = @file_get_contents( DVWA_WEB_PAGE_TO_ROOT . "vulnerabilities/{$id}/source/{$security}.js" );
		$js_html = "
<h2>vulnerabilities/{$id}/source/{$security}.js</h2>
<div id=\"code\">
<table width='100%' bgcolor='white' style=\"border:2px #C0C0C0 solid\">
<tr>
<td><div id=\"code\">" . highlight_string( $js_source, true ) . "</div></td>
</tr>
</table>
</div>
		";
	}
 
	$page[ 'body' ] .= "
<div class=\"body_padded\">
<h1>{$vuln} Source</h1>
 
		<h2>vulnerabilities/{$id}/source/{$security}.php</h2>
<div id=\"code\">
<table width='100%' bgcolor='white' style=\"border:2px #C0C0C0 solid\">
<tr>
<td><div id=\"code\">" . highlight_string( $source, true ) . "</div></td>
</tr>
</table>
</div>
		{$js_html}
<br /> <br />
 
		<form>
<input type=\"button\" value=\"Compare All Levels\" onclick=\"window.location.href='view_source_all.php?id=$id'\">
</form>
</div>\n";
} else {
	$page['body'] = "<p>Not found</p>";
}
 
dvwaSourceHtmlEcho( $page );
 
?>"""