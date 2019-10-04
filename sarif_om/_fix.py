# This file was generated by jschema_to_python version 1.2.2.

import attr


@attr.s
class Fix(object):
    """A proposed fix for the problem represented by a result object. A fix specifies a set of artifacts to modify. For each artifact, it specifies a set of bytes to remove, and provides a set of new bytes to replace them."""

    artifact_changes = attr.ib()
    description = attr.ib(default=None, metadata={"schema_property_name": "description"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
