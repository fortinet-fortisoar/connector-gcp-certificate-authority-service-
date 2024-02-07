# GCP Certificate Authority Service

This connector integrates with the GCP CA Service (CAS).  As of the creation of this connector, CAS does not support any of the industry standard certificate management protocols like SCEP and ACME.  Instead, GCP uses a more cloud-centric approach, providing an API which users can take advantage of in order to manage certificates.  There is no provision for storing Certificates or CRLs locally on FortiSOAR.  this connector will simply make the required requests and return the result.   

This connector was developed for a customer POC, it provides four different functions:

1. Get CA Certificate and Certificate Revocation List
1. Submit Certificate Signing Request (CSR)
1. Submit Certificate Revocation request

This represents a small subset of the functions avaialable, but generally covers the capabilities of certificate management protocols. 

In order to use this connector, users will need to create a Service Account with sufficient privileges and provide a .json key file for authentication.  See the below links for more information.

Certificate Authority Service docs:
https://cloud.google.com/certificate-authority-service/docs

For a complete list of the available python code samples for calling GCP CAS API:
https://cloud.google.com/certificate-authority-service/docs/samples?language=python

