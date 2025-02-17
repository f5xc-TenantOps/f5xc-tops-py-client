"""Module for DNS Zones and rrsets"""
from uplink import Consumer, get, post, put, delete, Body, Path
from . import helper

@helper.common_decorators
class Zone(Consumer):
    """Client for managing DNS zones in F5 Distributed Cloud."""
    def __init__(self, session):
        super().__init__(base_url=session._tenant_url, client=session._session)
    
    @get("/api/config/dns/namespaces/{namespace}/dns_zones")
    def list(self, namespace: Path = "system"):
        """Retrieve details of a specific DNS zone."""

    @get("/api/config/dns/namespaces/{namespace}/dns_zones/{name}")
    def get(self, name: Path, namespace: Path = "system"):
        """Retrieve details of a specific DNS zone."""

    @post("/api/config/dns/namespaces/{namespace}/dns_zones")
    def create(self, payload: Body, namespace: Path = "system"):
        """Create a new DNS zone in the given namespace."""

    @put("/api/config/dns/namespaces/{namespace}/dns_zones/{name}")
    def update(self, payload: Body, name: Path, namespace: Path = "system"):
        """Create a new DNS zone in the given namespace."""

    @delete("/api/config/dns/namespaces/{namespace}/dns_zones/{name}")
    def delete(self, name: Path, namespace: Path = "system"):
        """Delete a specific DNS zone."""

    @staticmethod
    def create_payload(
        name: str, 
        description: str = "", 
        labels: dict = None,
        default_rr_set_group: list = None, 
        lb_managed_records: bool = True):
        """Generate payload for creating a primary DNS zone."""
        return {
            "metadata": {
                "name": name,
                "namespace": "system",
                "description": description,
                "labels": labels or {},
                "annotations": {},
                "disable": False
            },
            "spec": {
                "primary": {
                    "rr_set_group": [],
                    "default_rr_set_group": default_rr_set_group or [],
                    "dnssec_mode": {"disable": {}},
                    "allow_http_lb_managed_records": lb_managed_records
                }
            }
        }

@helper.common_decorators
class RRSet(Consumer):
    """Client for managing DNS RRSet groups within a zone."""
    def __init__(self, session):
        super().__init__(base_url=session._tenant_url, client=session._session)

    @get("/api/config/dns/namespaces/{namespace}/dns_zones/{zone}/rrsets")
    def list(self, zone: Path, namespace: Path = "system"):
        """Retrieve a specific RRSet record."""
    
    @get("/api/config/dns/namespaces/{namespace}/dns_zones/{zone}/rrsets/{group}")
    def get(self, zone: Path, group: Path, namespace: Path = "system"):
        """Retrieve a specific RRSet record."""

    @post("/api/config/dns/namespaces/{namespace}/dns_zones/{zone}/rrsets/{group}")
    def create(self, zone: Path, group: Path, payload: Body, namespace: Path = "system"):
        """Create a new RRSet in a DNS zone."""

    @put("/api/config/dns/namespaces/{namespace}/dns_zones/{zone}/rrsets/{group}")
    def update(self, payload: Body, zone: Path, group: Path, namespace: Path = "system"):
        """Update an existing RRSet record."""

    @delete("/api/config/dns/namespaces/{namespace}/dns_zones/{zone}/rrsets/{group}")
    def delete(self, zone: Path, group: Path, namespace: Path = "system"):
        """Delete a specific RRSet record."""

    @staticmethod
    def create_payload(group_name: str, records: list):
        """Generate payload for creating an RRSet group."""
        return {
            "metadata": {
                "name": group_name
            },
            "records": records  # List of individual record payloads
        }

    @staticmethod
    def create_record(record_name: str, record_type: str, values: list, ttl: int = 300, description: str = ""):
        """Generate payload for creating an individual DNS record."""
        record_key = f"{record_type.lower()}_record"
        return {
            "ttl": ttl,
            record_key: {
                "name": record_name,
                "values": values if record_type.lower() != "cname" else values[0]  # CNAME has a single value
            },
            "description": description
        }
