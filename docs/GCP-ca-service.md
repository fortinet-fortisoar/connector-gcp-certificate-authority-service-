<h2>About the connector</h2>

<p>Certificate Authority Service is a highly available and scalable Google Cloud service that enables you to simplify, automate, and customize the deployment, management, and security of private certificate authorities (CA)</p>

<p>This document provides information about the GCP Certificate Authority Service Connector, which facilitates automated interactions, with a GCP Certificate Authority Service server using FortiSOAR&trade; playbooks. Add the GCP Certificate Authority Service Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with GCP Certificate Authority Service.</p>

<h3>Version information</h3>

<p>Connector Version: 1.0.0</p>

<p>Certified: No</p>

<p>Authored By: Fortinet CSE</p>

<p>Contributors: Derrick Gooch</p>


<h2>Installing the connector</h2>

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>

<pre>yum install cyops-connector-gcp-ca-service</pre>

<h2>Prerequisites to configuring the connector</h2>

<ul>
<li>You must have the credentials of GCP Certificate Authority Service server to which you will connect and perform automated operations.</li>
<li>The FortiSOAR&trade; server should have outbound connectivity to port 443 on the GCP Certificate Authority Service server.</li>
</ul>

<h2>Minimum Permissions Required</h2>

<ul>
<li>Not applicable</li>
</ul>

<h2>Configuring the connector</h2>

<p>For the procedure to configure a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector">here</a></p>

<h3>Configuration parameters</h3>

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>GCP Certificate Authority Service</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Upload Service Account JSON File</td>Provide a service account json file<td></td>
</tr></tbody></table>

<h2>Actions supported by the connector</h2>

<p>The following automated operations can be included in playbooks and you can also use the annotations to access operations:</p>

<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Certificate Authorities</td><td>Get certificate revocation list (CRL) is a list of digital certificates that have been revoked by the issuing certificate authority (CA)</td><td>list_certificate_authorities <br/>Investigation</td></tr>
<tr><td>Submit CSR</td><td>Submit a CSR(Certificate Signing Request)</td><td>submit_csr <br/>Investigation</td></tr>
<tr><td>Revoke Certificate</td><td>Revoke a certificate request for issued is no longer operational</td><td>revoke_certificate <br/>Investigation</td></tr>
</tbody></table>

<h3>operation: Get Certificate Authorities</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Location</td><td>Provide the geographical regions where a Certificate Authority Service resource is stored and can be accessed
</td></tr><tr><td>CA Pool Name</td><td>Provide a CA pool name for a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "kind": "",
    "id": "",
    "items": [],
    "nextPageToken": "",
    "selfLink": "",
    "warning": {}
}</pre>

<h3>operation: Submit CSR</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Location</td><td>Provide the geographical regions where a Certificate Authority Service resource is stored and can be accessed
</td></tr><tr><td>CA Pool Name</td><td>Provide a CA pool name for a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy
</td></tr><tr><td>Certificate Authority (CA)</td><td>Provide a name of certificate authority (ca) for self signed certificate
</td></tr><tr><td>Certificate Name</td><td>Specify the name you would like to assign to the certificate
</td></tr><tr><td>Certificate Lifetime</td><td>Provide a lifetime of the certificate in seconds
</td></tr><tr><td>CSR with a PEM Formatted Key</td><td>Provide CSR contains the public key of the key pair generated with the user certificate
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "kind": "",
    "id": "",
    "items": [],
    "nextPageToken": "",
    "selfLink": "",
    "warning": {}
}</pre>

<h3>operation: Revoke Certificate</h3>

<h4>Input parameters</h4>

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Location</td><td>Provide the geographical regions where a Certificate Authority Service resource is stored and can be accessed
</td></tr><tr><td>CA Pool Name</td><td>Provide a CA pool name for a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy
</td></tr><tr><td>Certificate Name</td><td>Specify the name you would like to assign to the certificate
</td></tr></tbody></table>

<h4>Output</h4>

<p>The output contains the following populated JSON schema:</p>

<pre>{
    "kind": "",
    "id": "",
    "items": [],
    "nextPageToken": "",
    "selfLink": "",
    "warning": {}
}</pre>
