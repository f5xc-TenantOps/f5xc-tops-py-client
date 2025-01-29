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
        origins: list,
        load_balancing_method: str = "ROUND_ROBIN",
        health_checks: list = None,
        description: str = "",
        labels: dict = None,
        namespace: str = "system",
    ):
        """
        Create a payload for Origin Pool.

        :param name: Name of the origin pool.
        :param origins: List of origin configurations built with build_origins().
        :param load_balancing_method: Load balancing method (e.g., "ROUND_ROBIN", "LEAST_CONNECTIONS").
        :param health_checks: List of health checks to attach to the origin pool.
        :param description: Description of the origin pool.
        :param labels: Labels to tag the origin pool.
        :param namespace: Namespace for the origin pool.
        :return: Dictionary payload for the API request.
        """
        if labels is None:
            labels = {}
        if health_checks is None:
            health_checks = []

        # Ensure the load balancing method is uppercase
        load_balancing_method = load_balancing_method.upper()

        return {
            "metadata": {
                "name": name,
                "namespace": namespace,
                "description": description,
                "labels": labels,
                "annotations": {},
            },
            "spec": {
                "load_balancing": {
                    "method": load_balancing_method,
                },
                "origins": origins,
                "health_checks": health_checks,
            },
        }

    @staticmethod
    def build_origins(
        name: str,
        ip: str = None,
        hostname: str = None,
        port: int = 443,
        weight: int = 1,
        tls_enabled: bool = False,
        connection_timeout: int = 5,
        max_connections: int = 100,
    ):
        """
        Build an origin configuration for an origin pool.

        :param name: Unique name for the origin.
        :param ip: IP address of the origin (optional).
        :param hostname: Hostname of the origin (optional).
        :param port: Port of the origin (default: 443).
        :param weight: Weight for load balancing (default: 1).
        :param tls_enabled: Whether TLS is enabled for the origin (default: False).
        :param connection_timeout: Connection timeout in seconds (default: 5).
        :param max_connections: Maximum number of connections allowed (default: 100).
        :return: Dictionary representing an origin.
        """
        if not ip and not hostname:
            raise ValueError("Either 'ip' or 'hostname' must be provided for an origin.")

        origin = {
            "name": name,
            "port": port,
            "weight": weight,
            "tls": tls_enabled,
            "connection_timeout": connection_timeout,
            "max_connections": max_connections,
        }

        if ip:
            origin["ip"] = ip
        if hostname:
            origin["hostname"] = hostname

        return origin
