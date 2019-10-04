# This file was generated by jschema_to_python version 1.2.2.

import attr


@attr.s
class Exception(object):
    """Describes a runtime exception encountered during the execution of an analysis tool."""

    inner_exceptions = attr.ib(default=None, metadata={"schema_property_name": "innerExceptions"})
    kind = attr.ib(default=None, metadata={"schema_property_name": "kind"})
    message = attr.ib(default=None, metadata={"schema_property_name": "message"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    stack = attr.ib(default=None, metadata={"schema_property_name": "stack"})
