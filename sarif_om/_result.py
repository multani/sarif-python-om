# This file was generated by jschema_to_python version 1.2.3.

from ._artifact_location import ArtifactLocation
from ._attachment import Attachment
from ._code_flow import CodeFlow
from ._fix import Fix
from ._graph import Graph
from ._graph_traversal import GraphTraversal
from ._location import Location
from ._message import Message
from ._property_bag import PropertyBag
from ._reporting_descriptor_reference import ReportingDescriptorReference
from ._result_provenance import ResultProvenance
from ._stack import Stack
from ._suppression import Suppression
from ._web_request import WebRequest
from ._web_response import WebResponse
from attrs import define
from attrs import field


@define()
class Result:
    """A result produced by an analysis tool."""

    message : Message = field(metadata={"schema_property_name": "message"})
    analysis_target : ArtifactLocation = field(default=None, metadata={"schema_property_name": "analysisTarget"})
    attachments : list[Attachment] = field(factory=list, metadata={"schema_property_name": "attachments"})
    baseline_state : str = field(default=None, metadata={"schema_property_name": "baselineState"})
    code_flows : list[CodeFlow] = field(factory=list, metadata={"schema_property_name": "codeFlows"})
    correlation_guid : str = field(default=None, metadata={"schema_property_name": "correlationGuid"})
    fingerprints : dict[str, str] = field(default=None, metadata={"schema_property_name": "fingerprints"})
    fixes : list[Fix] = field(factory=list, metadata={"schema_property_name": "fixes"})
    graph_traversals : list[GraphTraversal] = field(factory=list, metadata={"schema_property_name": "graphTraversals"})
    graphs : list[Graph] = field(factory=list, metadata={"schema_property_name": "graphs"})
    guid : str = field(default=None, metadata={"schema_property_name": "guid"})
    hosted_viewer_uri : str = field(default=None, metadata={"schema_property_name": "hostedViewerUri"})
    kind : str = field(default="fail", metadata={"schema_property_name": "kind"})
    level : str = field(default="warning", metadata={"schema_property_name": "level"})
    locations : list[Location] = field(factory=list, metadata={"schema_property_name": "locations"})
    occurrence_count : int = field(default=None, metadata={"schema_property_name": "occurrenceCount"})
    partial_fingerprints : dict[str, str] = field(default=None, metadata={"schema_property_name": "partialFingerprints"})
    properties : PropertyBag = field(default=None, metadata={"schema_property_name": "properties"})
    provenance : ResultProvenance = field(default=None, metadata={"schema_property_name": "provenance"})
    rank : float = field(default=-1.0, metadata={"schema_property_name": "rank"})
    related_locations : list[Location] = field(factory=list, metadata={"schema_property_name": "relatedLocations"})
    rule : ReportingDescriptorReference = field(default=None, metadata={"schema_property_name": "rule"})
    rule_id : str = field(default=None, metadata={"schema_property_name": "ruleId"})
    rule_index : int = field(default=-1, metadata={"schema_property_name": "ruleIndex"})
    stacks : list[Stack] = field(factory=list, metadata={"schema_property_name": "stacks"})
    suppressions : list[Suppression] = field(factory=list, metadata={"schema_property_name": "suppressions"})
    taxa : list[ReportingDescriptorReference] = field(factory=list, metadata={"schema_property_name": "taxa"})
    web_request : WebRequest = field(default=None, metadata={"schema_property_name": "webRequest"})
    web_response : WebResponse = field(default=None, metadata={"schema_property_name": "webResponse"})
    work_item_uris : list[str] = field(factory=list, metadata={"schema_property_name": "workItemUris"})
