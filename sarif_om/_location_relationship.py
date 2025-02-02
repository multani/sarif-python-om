# This file was generated by jschema_to_python version 1.2.3.

from ._message import Message
from ._property_bag import PropertyBag
from attrs import define
from attrs import field


@define()
class LocationRelationship:
    """Information about the relation of one location to another."""

    target : int = field(metadata={"schema_property_name": "target"})
    description : Message = field(default=None, metadata={"schema_property_name": "description"})
    kinds : list[str] = field(factory=lambda: ['relevant'], metadata={"schema_property_name": "kinds"})
    properties : PropertyBag = field(default=None, metadata={"schema_property_name": "properties"})
