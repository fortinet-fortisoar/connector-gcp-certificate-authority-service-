## About the connector
Certificate Authority Service is a highly available and scalable Google Cloud service that enables you to simplify, automate, and customize the deployment, management, and security of private certificate authorities (CA)
<p>This document provides information about the GCP Certificate Authority Service Connector, which facilitates automated interactions, with a GCP Certificate Authority Service server using FortiSOAR&trade; playbooks. Add the GCP Certificate Authority Service Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with GCP Certificate Authority Service.</p>

### Version information

Connector Version: 1.0.1

Authored By: Fortinet CSE

Contributor: Derrick Gooch

Certified: No
## Release Notes for version 1.0.1
Following enhancements have been made to the GCP Certificate Authority Service Connector in version 1.0.1:
<ul>
<li><p>Added the following new operation and playbook:</p>

<ul>
<li>Get CA and CRL</li>
</ul></li>
</ul>

## Installing the connector
<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-gcp-ca-service</pre>

## Prerequisites to configuring the connector
- You must have the credentials of GCP Certificate Authority Service server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the GCP Certificate Authority Service server.

## Minimum Permissions Required
- Not applicable

## Configuring the connector
For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)
### Configuration parameters
<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>GCP Certificate Authority Service</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Upload Service Account JSON File</td><td>Provide a service account json file
</td>
</tr></tbody></table>

## Actions supported by the connector
The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Certificate Authorities</td><td>Get a list of certificate authorities (CAs) in a given CA pool</td><td>list_certificate_authorities <br/>Investigation</td></tr>
<tr><td>Get CA and CRL</td><td>Get CA certificate and certificate revocation list (CRL). CRL is a list of digital certificates that have been revoked by the issuing certificate authority (CA)</td><td>get_ca_crl <br/>Investigation</td></tr>
<tr><td>Submit CSR</td><td>Submit a CSR(Certificate Signing Request) to GCP CA Service.  This will return a signed certificate</td><td>submit_csr <br/>Investigation</td></tr>
<tr><td>Revoke Certificate</td><td>Revoke a certificate request for issued is no longer operational</td><td>revoke_certificate <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Certificate Authorities
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Location</td><td>Provide the geographical regions where a Certificate Authority Service resource is stored and can be accessed
</td></tr><tr><td>CA Pool Name</td><td>Provide a CA pool name for a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "kind": "",
    "id": "",
    "items": [],
    "nextPageToken": "",
    "selfLink": "",
    "warning": {}
}</pre>

### operation: Get CA and CRL
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Location</td><td>Provide the geographical regions where a Certificate Authority Service resource is stored and can be accessed
</td></tr><tr><td>CA Name</td><td>Provide a  name of the certificate revocation list to retrieve.
</td></tr><tr><td>CA Pool Name</td><td>Provide a CA pool name for a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "kind": "",
    "id": "",
    "items": [],
    "nextPageToken": "",
    "selfLink": "",
    "warning": {}
}</pre>

### operation: Submit CSR
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Location</td><td>Provide the geographical regions where a Certificate Authority Service resource is stored and can be accessed
</td></tr><tr><td>CA Pool Name</td><td>Provide a CA pool name for a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy
</td></tr><tr><td>Certificate Authority (CA)</td><td>Provide a name of certificate authority (ca) for self signed certificate
</td></tr><tr><td>Certificate Name</td><td>Specify the name you would like to assign to the certificate
</td></tr><tr><td>Certificate Lifetime</td><td>Provide a lifetime of the certificate in seconds
</td></tr><tr><td>CSR with a PEM Formatted Key</td><td>Provide CSR contains the public key of the key pair generated with the user certificate
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "kind": "",
    "id": "",
    "items": [],
    "nextPageToken": "",
    "selfLink": "",
    "warning": {}
}</pre>

### operation: Revoke Certificate
#### Input parameters
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Location</td><td>Provide the geographical regions where a Certificate Authority Service resource is stored and can be accessed
</td></tr><tr><td>CA Pool Name</td><td>Provide a CA pool name for a collection of multiple CAs with a common certificate issuance policy and Identity and Access Management (IAM) policy
</td></tr><tr><td>Certificate Name</td><td>Specify the name you would like to assign to the certificate
</td></tr></tbody></table>

#### Output
The output contains the following populated JSON schema:

<pre>{
    "kind": "",
    "id": "",
    "items": [],
    "nextPageToken": "",
    "selfLink": "",
    "warning": {}
}</pre>
## Included playbooks
The `Sample - GCP Certificate Authority Service - 1.0.1` playbook collection comes bundled with the GCP Certificate Authority Service connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the GCP Certificate Authority Service connector.

- Get CA and CRL
- Get Certificate Authorities
- Revoke Certificate
- Submit CSR

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
