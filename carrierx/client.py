from carrierx.base.rest_client import RestClient, RestConnection
from carrierx.resources import core
from carrierx.resources import mediator
from carrierx.resources import flexml
from carrierx.exceptions import AuthNotProvidedException


class CoreClient(RestClient):
    def __init__(self, username='', password='', token='', base_url="htts://api.carrierx.com/core/v2"):

        if not token and not (username and password):
            raise AuthNotProvidedException('Secure token or login/password should be provided')

        super().__init__(RestConnection(username=username, password=password, token=token, base_url=base_url))

        self.endpoints = core.Endpoints(self.connection)
        self.storage = lambda: None
        self.storage.containers = core.storage.Containers(self.connection)
        self.storage.files = core.storage.Files(self.connection)
        self.sms = lambda: None
        self.sms.messages = core.sms.Messages(self.connection)
        self.shortener = lambda: None
        self.shortener.domains = core.shortener.Domains(self.connection)
        self.shortener.links = core.shortener.Links(self.connection)


class MediatorClient(RestClient):
    def __init__(self, username, password, base_url="htts://api.carrierx.com/mediator/v1"):
        super().__init__(RestConnection(username=username, password=password, base_url=base_url))

        self.bindings = mediator.Bindings(self.connection)
        self.dids = mediator.Dids(self.connection)


class FlexmlClient(RestClient):
    def __init__(self, username, password, base_url="htts://api.carrierx.com/flexml/v1"):
        super().__init__(RestConnection(username=username, password=password, base_url=base_url))

        self.calls = flexml.Calls(self.connection)
        self.dids = flexml.Dids(self.connection)
