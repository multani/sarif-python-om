# This file was generated by jschema_to_python version 1.2.2.

import attr


@attr.s
class Invocation(object):
    """The runtime environment of the analysis tool run."""

    execution_successful = attr.ib()
    account = attr.ib(default=None, metadata={"schema_property_name": "account"})
    arguments = attr.ib(default=None, metadata={"schema_property_name": "arguments"})
    command_line = attr.ib(default=None, metadata={"schema_property_name": "commandLine"})
    end_time_utc = attr.ib(default=None, metadata={"schema_property_name": "endTimeUtc"})
    environment_variables = attr.ib(default=None, metadata={"schema_property_name": "environmentVariables"})
    executable_location = attr.ib(default=None, metadata={"schema_property_name": "executableLocation"})
    exit_code = attr.ib(default=None, metadata={"schema_property_name": "exitCode"})
    exit_code_description = attr.ib(default=None, metadata={"schema_property_name": "exitCodeDescription"})
    exit_signal_name = attr.ib(default=None, metadata={"schema_property_name": "exitSignalName"})
    exit_signal_number = attr.ib(default=None, metadata={"schema_property_name": "exitSignalNumber"})
    machine = attr.ib(default=None, metadata={"schema_property_name": "machine"})
    notification_configuration_overrides = attr.ib(default=None, metadata={"schema_property_name": "notificationConfigurationOverrides"})
    process_id = attr.ib(default=None, metadata={"schema_property_name": "processId"})
    process_start_failure_message = attr.ib(default=None, metadata={"schema_property_name": "processStartFailureMessage"})
    properties = attr.ib(default=None, metadata={"schema_property_name": "properties"})
    response_files = attr.ib(default=None, metadata={"schema_property_name": "responseFiles"})
    rule_configuration_overrides = attr.ib(default=None, metadata={"schema_property_name": "ruleConfigurationOverrides"})
    start_time_utc = attr.ib(default=None, metadata={"schema_property_name": "startTimeUtc"})
    stderr = attr.ib(default=None, metadata={"schema_property_name": "stderr"})
    stdin = attr.ib(default=None, metadata={"schema_property_name": "stdin"})
    stdout = attr.ib(default=None, metadata={"schema_property_name": "stdout"})
    stdout_stderr = attr.ib(default=None, metadata={"schema_property_name": "stdoutStderr"})
    tool_configuration_notifications = attr.ib(default=None, metadata={"schema_property_name": "toolConfigurationNotifications"})
    tool_execution_notifications = attr.ib(default=None, metadata={"schema_property_name": "toolExecutionNotifications"})
    working_directory = attr.ib(default=None, metadata={"schema_property_name": "workingDirectory"})
