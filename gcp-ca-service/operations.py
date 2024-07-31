"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
import os
import requests

import google.cloud.security.privateca_v1 as privateca_v1
import google.api_core.retry as retry
from google.oauth2 import service_account
from connectors.core.connector import get_logger, ConnectorError
from connectors.cyops_utilities.builtins import download_file_from_cyops
from google.protobuf import duration_pb2

logger = get_logger('gcp-ca-service')


class GoogleCloudCAService(object):

    def __init__(self, config):
        self.client_details = dict()
        scopes = ['https://www.googleapis.com/auth/cloud-platform']
        try:
            cert_file_iri = config.get('auth_file').get('@id')
            filename = download_file_from_cyops(cert_file_iri).get('cyops_file_path')
            file_data = os.path.join('/tmp/', filename)
            self.credentials = service_account.Credentials.from_service_account_file(file_data, scopes=scopes)
            self.p_id = self.credentials.project_id
        except Exception as err:
            logger.exception("{0}".format(str(err)))
            raise ConnectorError("{0}".format(str(err)))

    def create_clients(self):
        try:
            ca_service_client = privateca_v1.CertificateAuthorityServiceClient(credentials=self.credentials)
            self.client_details['ca_service_client'] = ca_service_client
        except Exception as e:
            logger.exception(
                'Failed to get clients. Please check the service account json contents for authentication.')
            raise ConnectorError('Error: {0}'.format(e))

    def make_client_call(self, client_types, health_check=False):
        clients = dict()
        if not self.client_details:
            logger.warn("Creating different clients.")
            self.create_clients()
        if health_check and not self.client_details:
            logger.error("Failed to create clients. Make sure the provided credentials are correct.")
            raise ConnectorError("Connector is not available. Health check failed.")
        for typ in client_types:
            clients[typ] = self.client_details[typ]
        return clients
    @retry.Retry()

    def list_certificate_authorities(self, params):
        project_id = self.p_id
        location = params.get('location')
        ca_pool_name = params.get('ca_pool_name')
        client_types = ['ca_service_client']
        clients = self.make_client_call(client_types)
        caServiceClient = clients[client_types[0]]
        ca_pool_path = caServiceClient.ca_pool_path(project_id, location, ca_pool_name)
        data_res = []
        for ca in caServiceClient.list_certificate_authorities(parent=ca_pool_path):
            ca_name_long = ca.name
            ca_short_name = ca_name_long.split('/')[-1]

            data_res_item = {
                'ca_name': ca_short_name,
                'ca_type': ca.type,
            }
            data_res.append(data_res_item)
        return data_res

    def get_ca_crl(self, params):
        project_id = self.p_id
        location = params.get('location')
        ca_name = params.get('ca_name')
        ca_pool_name = params.get('ca_pool_name')
        client_types = ['ca_service_client']
        clients = self.make_client_call(client_types)
        caServiceClient = clients[client_types[0]]
        ca_pool_path = caServiceClient.ca_pool_path(project_id, location, ca_pool_name)
        data_res = []
        for ca in caServiceClient.list_certificate_authorities(parent=ca_pool_path):
            ca_name_long = ca.name
            ca_short_name = ca_name_long.split('/')[-1]
            if ca_short_name == ca_name:
                ca_cert_url = ca.access_urls.ca_certificate_access_url
                crl_url = ca.access_urls.crl_access_urls[0]
                ca_cert = requests.get(ca_cert_url)
                crl_cert = requests.get(crl_url)
                data_res_item = {
                    'ca_crt': ca_cert.content,
                    'crl_crt': crl_cert.content
                }
                data_res.append(data_res_item)
        return data_res

    def csr(self, params):
        logger.warn(f"params:{params}")
        project_id = self.p_id
        location = params.get('location')
        ca_pool_name = params.get('ca_pool_name')
        ca_name = params.get('ca_name')
        certificate_name = params.get('certificate_name')
        certificate_lifetime = params.get('certificate_lifetime')
        pem_csr = params.get('pem_csr')
        client_types = ['ca_service_client']
        logger.warn("done with params")

        clients = self.make_client_call(client_types)
        caServiceClient = clients[client_types[0]]

        duration = duration_pb2.Duration(seconds=certificate_lifetime)

        # Create certificate with CSR.
        # The pem_csr contains the public key and the domain details required.
        certificate = privateca_v1.Certificate(
            pem_csr=pem_csr,
            lifetime=duration
        )
        # Create the Certificate Request.
        # Set the CA which is responsible for creating the certificate with the provided CSR.
        csrequest = privateca_v1.CreateCertificateRequest(
            parent=caServiceClient.ca_pool_path(project_id, location, ca_pool_name),
            certificate_id=certificate_name,
            certificate=certificate,
            issuing_certificate_authority_id=ca_name,
        )
        csresponse = caServiceClient.create_certificate(request=csrequest)

        signed_cert = csresponse.pem_certificate
        cert_chain = csresponse.pem_certificate_chain
        logger.warn("done with csr")

        return {"signed_cert": signed_cert, "cert_chain": "\n".join(cert_chain)}

    def revoke_certificate(self, params):
        logger.warn(f"params:{params}")
        project_id = self.p_id
        location = params.get('location')
        ca_pool_name = params.get('ca_pool_name')
        certificate_name = params.get('certificate_name')
        client_types = ['ca_service_client']
        clients = self.make_client_call(client_types)
        caServiceClient = clients[client_types[0]]

        certificate_path = caServiceClient.certificate_path(
            project_id, location, ca_pool_name, certificate_name
        )

        # Create Revoke Certificate Request and specify the appropriate revocation reason.
        request = privateca_v1.RevokeCertificateRequest(
            name=certificate_path, reason=privateca_v1.RevocationReason.PRIVILEGE_WITHDRAWN
        )
        revoke = caServiceClient.revoke_certificate(request=request)
        rev_res = revoke.revocation_details.revocation_time
        logger.warn("done with revocation")
        return (rev_res)


def _run_operation(config, params):
    compute_obj = GoogleCloudCAService(config)
    command = getattr(GoogleCloudCAService, params['operation'])
    response = command(compute_obj, params)
    return response


def _check_health(config):
    compute_obj = GoogleCloudCAService(config)
    logger.warn('Checking Health check.')
    return compute_obj.make_client_call(['ca_service_client'], True)