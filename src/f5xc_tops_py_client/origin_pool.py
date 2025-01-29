"""
Module for Origin Pool
https://docs.cloud.f5.com/docs-v2/api/views-origin-pool
"""
from uplink import Consumer, Path, Body, get, post, put, delete, json #pylint: disable=unused-import
from . import helper

@helper.common_decorators
class OriginPool(Consumer):
    """
    Class for Origin Pool API.
    """

    def __init__(self, session):
        """
        Initialize the OriginPool Consumer.
        :param session: Session object with tenant URL and auth.
        """
        super().__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/config/namespaces/{namespace}/origin_pools')
    def list(self, namespace: Path):
        """
        List all Origin Pools in a namespace.
        """

    @get('/api/config/namespaces/{namespace}/origin_pools/{name}')
    def get(self, namespace: Path, name: Path):
        """
        Get details of an Origin Pool.
        """

    @json
    @post('/api/config/namespaces/{namespace}/origin_pools')
    def create(self, payload: Body, namespace: Path):
        """
        Create an Origin Pool.
        Use create_payload() to build Body.
        """

    @json
    @put('/api/config/namespaces/{namespace}/origin_pools/{name}')
    def replace(self, payload: Body, namespace: Path, name: Path):
        """
        Replace an Origin Pool.
        Use create_payload() to build Body.
        """

    @delete('/api/config/namespaces/{namespace}/origin_pools/{name}')
    def delete(self, namespace: Path, name: Path):
        """
        Delete an Origin Pool.
        """

    @staticmethod
    def create_payload(
        name: str,
        namespace: str,
        origin_servers: list,
        port: int = 443,
        loadbalancer_algorithm: str = "LB_OVERRIDE",
        endpoint_selection: str = "LOCAL_PREFERRED",
        healthcheck: list = None,
        description: str = "",
        labels: dict = None,
        disable: bool = False,
        same_as_endpoint_port: dict = None,
        no_tls: dict = None,  # Added no_tls parameter
    ):
        """
        Construct the full payload for an Origin Pool.

        :param name: Name of the Origin Pool.
        :param namespace: Namespace where the pool is created.
        :param origin_servers: List of origin server objects.
        :param port: Top-level port for the origin pool (default: 443).
        :param loadbalancer_algorithm: Load balancing algorithm (default: "LB_OVERRIDE").
        :param endpoint_selection: Endpoint selection policy (default: "LOCAL_PREFERRED").
        :param healthcheck: List of healthcheck references (optional).
        :param description: Description of the Origin Pool.
        :param labels: Labels to tag the Origin Pool (optional).
        :param disable: Whether to disable the Origin Pool (default: False).
        :param same_as_endpoint_port: Pass `{}` if using the same port as the endpoint.
        :param no_tls: Pass `{}` to disable TLS, or `None` to enable TLS (default: `{}`).
        :return: Dictionary representing the Origin Pool payload.
        """
        if labels is None:
            labels = {}

        if healthcheck is None:
            healthcheck = []

        if same_as_endpoint_port is None:
            same_as_endpoint_port = {}

        spec = {
            "origin_servers": [
                {k: v for k, v in server.items() if k != "name"}
                for server in origin_servers
            ],
            "port": port,
            "loadbalancer_algorithm": loadbalancer_algorithm,
            "endpoint_selection": endpoint_selection,
            "healthcheck": healthcheck,
            "same_as_endpoint_port": same_as_endpoint_port,
        }

        if no_tls is not None:
            spec["no_tls"] = no_tls

        return {
            "metadata": {
                "name": name,
                "namespace": namespace,
                "description": description,
                "labels": labels,
                "disable": disable,
            },
            "spec": spec,
        }

    @staticmethod
    def build_origin_server(
        name: str,
        port: int = 443,
        public_ip: str = None,
        public_name: str = None,
        private_ip: str = None,
        private_name: str = None,
        k8s_service: dict = None,
        custom_endpoint: dict = None,
        cbip_service: str = None,
        consul_service: dict = None,
        vn_private_ip: str = None,
        vn_private_name: str = None,
        refresh_interval: int = 300,
        site_locator: dict = None,
        labels: dict = None,
    ):
        """
        Build an origin server configuration for an Origin Pool.

        :param name: Unique name for the origin server.
        :param port: Port of the origin server (default: 443).
        :param public_ip: Public IP address of the origin server (optional).
        :param public_name: Public DNS name of the origin server (optional).
        :param private_ip: Private IP address of the origin server (optional).
        :param private_name: Private DNS name of the origin server (optional).
        :param k8s_service: Kubernetes service reference (optional, dict with 'service_name').
        :param custom_endpoint: Custom endpoint reference (optional, dict with 'name', 'namespace').
        :param cbip_service: Classic BIG-IP Virtual Server name (optional).
        :param consul_service: HashiCorp Consul service reference (optional, dict with 'service_name').
        :param vn_private_ip: Virtual Network IP address (optional).
        :param vn_private_name: Virtual Network DNS name (optional).
        :param refresh_interval: DNS resolution refresh interval (default: 300 seconds).
        :param site_locator: Site reference object (optional, dict with 'name', 'namespace').
        :param labels: Labels to tag the origin server (optional).
        :return: Dictionary representing an origin server.
        """
        if labels is None:
            labels = {}

        origin_server = {"name": name, "labels": labels, "port": port}

        if public_ip:
            origin_server["public_ip"] = {"ip": public_ip}

        if public_name:
            origin_server["public_name"] = {
                "dns_name": public_name,
                "refresh_interval": refresh_interval,
            }

        if private_ip:
            origin_server["private_ip"] = {"ip": private_ip}

        if private_name:
            origin_server["private_name"] = {
                "dns_name": private_name,
                "refresh_interval": refresh_interval,
            }

        if k8s_service:
            if not isinstance(k8s_service, dict) or "service_name" not in k8s_service:
                raise ValueError("'k8s_service' must be a dictionary with 'service_name'.")
            origin_server["k8s_service"] = k8s_service

        if custom_endpoint:
            if not isinstance(custom_endpoint, dict) or "name" not in custom_endpoint:
                raise ValueError("'custom_endpoint' must be a dictionary with 'name'.")
            origin_server["custom_endpoint_object"] = {"endpoint": custom_endpoint}

        if cbip_service:
            origin_server["cbip_service"] = {"service_name": cbip_service}

        if consul_service:
            if not isinstance(consul_service, dict) or "service_name" not in consul_service:
                raise ValueError("'consul_service' must be a dictionary with 'service_name'.")
            origin_server["consul_service"] = consul_service

        if vn_private_ip:
            origin_server["vn_private_ip"] = {"ip": vn_private_ip}

        if vn_private_name:
            origin_server["vn_private_name"] = {"dns_name": vn_private_name}

        if site_locator:
            if not isinstance(site_locator, dict) or "name" not in site_locator:
                raise ValueError("'site_locator' must be a dictionary with 'name'.")
            origin_server["site_locator"] = site_locator

        return origin_server
