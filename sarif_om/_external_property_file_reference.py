# This file was generated by jschema_to_python version 1.2.3.

from ._artifact_location import ArtifactLocation
from ._property_bag import PropertyBag
from attrs import define
from attrs import field


@define()
class ExternalPropertyFileReference:
    """Contains information that enables a SARIF consumer to locate the external property file that contains the value of an externalized property associated with the run."""

    guid : str = field(default=None, metadata={"schema_property_name": "guid"})
    item_count : int = field(default=-1, metadata={"schema_property_name": "itemCount"})
    location : ArtifactLocation = field(default=None, metadata={"schema_property_name": "location"})
    properties : PropertyBag = field(default=None, metadata={"schema_property_name": "properties"})
