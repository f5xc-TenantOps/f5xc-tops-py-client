"""
Module for Load Balancers
https://docs.cloud.f5.com/docs-v2/api/views-http-loadbalancer
https://docs.cloud.f5.com/docs-v2/api/views-tcp-loadbalancer
"""
from uplink import Consumer, Path, Body, get, post, put, delete, json #pylint: disable=unused-import
from . import helper

@helper.common_decorators
class HTTPLoadBalancer(Consumer):
    """
    Class for HTTP Load Balancer API.
    """

    def __init__(self, session):
        """
        Initialize the HTTPLoadBalancer Consumer.
        :param session: Session object with tenant URL and auth.
        """
        super().__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/config/namespaces/{namespace}/http_loadbalancers')
    def list(self, namespace: Path):
        """
        List all HTTP Load Balancers in a namespace.
        """

    @get('/api/config/namespaces/{namespace}/http_loadbalancers/{name}')
    def get(self, namespace: Path, name: Path):
        """
        Get details of an HTTP Load Balancer.
        """

    @json
    @post('/api/config/namespaces/{namespace}/http_loadbalancers')
    def create(self, payload: Body, namespace: Path):
        """
        Create an HTTP Load Balancer.
        Use create_payload() to build Body.
        """

    @json
    @put('/api/config/namespaces/{namespace}/http_loadbalancers/{name}')
    def replace(self, payload: Body, namespace: Path, name: Path):
        """
        Replace an HTTP Load Balancer.
        Use create_payload() to build Body.
        """

    @delete('/api/config/namespaces/{namespace}/http_loadbalancers/{name}')
    def delete(self, namespace: Path, name: Path):
        """
        Delete an HTTP Load Balancer.
        """

    @staticmethod
    def create_payload(
        name: str,
        listeners: list,
        origin_pools: list,
        policies: list = None,
        description: str = "",
        labels: dict = None,
        namespace: str = "system",
    ):
        """
        Create a payload for HTTP Load Balancer.

        :param name: Name of the HTTP load balancer.
        :param listeners: List of listener configurations (use build_listener()).
        :param origin_pools: List of linked origin pools.
        :param policies: List of traffic policies (optional).
        :param description: Description of the load balancer.
        :param labels: Labels to tag the load balancer.
        :param namespace: Namespace for the load balancer.
        :return: Dictionary payload for the API request.
        """
        if labels is None:
            labels = {}
        if policies is None:
            policies = []

        return {
            "metadata": {
                "name": name,
                "namespace": namespace,
                "description": description,
                "labels": labels,
                "annotations": {},
            },
            "spec": {
                "listeners": listeners,
                "origin_pools": origin_pools,
                "policies": policies,
            },
        }

    @staticmethod
    def build_listener(
        name: str,
        port: int,
        tls_enabled: bool = False,
    ):
        """
        Build an HTTP/HTTPS listener configuration for a Load Balancer.

        :param name: Unique name for the listener.
        :param port: Port number for the listener.
        :param tls_enabled: Whether TLS is enabled (default: False).
        :return: Dictionary representing an HTTP listener.
        """
        return {
            "name": name,
            "port": port,
            "protocol": "HTTPS" if tls_enabled else "HTTP",
            "tls_enabled": tls_enabled,
        }

@helper.common_decorators
class TCPLoadBalancer(Consumer):
    """
    Class for TCP Load Balancer API.
    """

    def __init__(self, session):
        """
        Initialize the TCPLoadBalancer Consumer.
        :param session: Session object with tenant URL and auth.
        """
        super().__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/config/namespaces/{namespace}/tcp_loadbalancers')
    def list(self, namespace: Path):
        """
        List all TCP Load Balancers in a namespace.
        """

    @get('/api/config/namespaces/{namespace}/tcp_loadbalancers/{name}')
    def get(self, namespace: Path, name: Path):
        """
        Get details of a TCP Load Balancer.
        """

    @json
    @post('/api/config/namespaces/{namespace}/tcp_loadbalancers')
    def create(self, payload: Body, namespace: Path):
        """
        Create a TCP Load Balancer.
        Use create_payload() to build Body.
        """

    @json
    @put('/api/config/namespaces/{namespace}/tcp_loadbalancers/{name}')
    def replace(self, payload: Body, namespace: Path, name: Path):
        """
        Replace a TCP Load Balancer.
        Use create_payload() to build Body.
        """

    @delete('/api/config/namespaces/{namespace}/tcp_loadbalancers/{name}')
    def delete(self, namespace: Path, name: Path):
        """
        Delete a TCP Load Balancer.
        """

    @staticmethod
    def create_payload(
        name: str,
        listeners: list,
        origin_pools: list,
        policies: list = None,
        description: str = "",
        labels: dict = None,
        namespace: str = "system",
    ):
        """
        Create a payload for TCP Load Balancer.

        :param name: Name of the TCP load balancer.
        :param listeners: List of listener configurations (use build_listener()).
        :param origin_pools: List of linked origin pools.
        :param policies: List of traffic policies (optional).
        :param description: Description of the load balancer.
        :param labels: Labels to tag the load balancer.
        :param namespace: Namespace for the load balancer.
        :return: Dictionary payload for the API request.
        """
        if labels is None:
            labels = {}
        if policies is None:
            policies = []

        return {
            "metadata": {
                "name": name,
                "namespace": namespace,
                "description": description,
                "labels": labels,
                "annotations": {},
            },
            "spec": {
                "listeners": listeners,
                "origin_pools": origin_pools,
                "policies": policies,
            },
        }

    @staticmethod
    def build_listener(
        name: str,
        port: int,
    ):
        """
        Build a TCP listener configuration for a Load Balancer.

        :param name: Unique name for the listener.
        :param port: Port number for the listener.
        :return: Dictionary representing a TCP listener.
        """
        return {
            "name": name,
            "port": port,
            "protocol": "TCP",
        }
