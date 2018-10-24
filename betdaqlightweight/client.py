from suds.client import Client as SudsClient
from betdaqlightweight.endpoints import readonly, secure


class Client:

    def __init__(self, username='', password='', language='en', application_identifier=None):
        """
        Client object carrying the connection information.

        :param username: Betdaq username
        :type username: str
        :param password: Betdaq password
        :type password: str
        :param language: Language code (2 letters)
        :return: response of request success.
        """
        self.url_readonly = 'https://api.betdaq.com/v2.0/ReadOnlyService.asmx?WSDL'
        self.url_secure = 'https://api.betdaq.com/v2.0/Secure/SecureService.asmx?WSDL'
        self.username = username
        self.password = password
        self.version = '2.0'
        self.language = language
        self.application_identifier = application_identifier
        self._read_only_client = SudsClient(self.url_readonly)
        self._add_headers(False)
        self._secure_client = SudsClient(self.url_secure)
        self._add_headers(True)

        self.readonly = readonly.Endpoint(self._read_only_client)
        self.secure = secure.Endpoint(self._secure_client)

    def _add_headers(self, is_secure=True):
        if is_secure:
            client = self._secure_client
        else:
            client = self._read_only_client
        token = client.factory.create('ExternalApiHeader')
        token._version = self.version
        token._username = self.username
        token._password = self.password
        token._languageCode = self.language
        token._applicationIdentifier = self.application_identifier
        client.set_options(soapheaders=token)
