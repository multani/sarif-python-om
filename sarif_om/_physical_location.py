# This file was generated by jschema_to_python version 1.2.2.

import attr


@attr.s
class PhysicalLocation(object):
    """A physical location relevant to a result. Specifies a reference to a programming artifact together with a range of bytes or characters within that artifact."""

    address = attr.ib(default=None, metadata={"schema_property_name": "address"})
    artifact_location = attr.ib(default=None, metadata={"schema_property_name": "artifactLocation"})
    context_region = attr.ib(default=None, metadata={"schema_property_name": "contextRegion"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    region = attr.ib(default=None, metadata={"schema_property_name": "region"})
