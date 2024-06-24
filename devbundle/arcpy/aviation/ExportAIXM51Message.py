# Generated documentation for module arcpy.aviation


class ExportAIXM51Message(object):
    """
    Exports aeronautical data to an AIXM 5.1 message.
    """

    @property
    def description(self) -> str:
        return """

        ExportAIXM51Message_aviation(in_aviation_workspace, out_message_file, export_type, {last_modified_time}, {in_filter_layers;in_filter_layers...}, {from_time}, {to_time}, {validate_output}, {out_validation_log})

        Exports aeronautical data to an AIXM 5.1 message.

     INPUTS:
      in_aviation_workspace (Workspace):
          The AIS schema workspace.
      export_type (String):
          Specifies the AIXM temporality type the message represents.BASELINE-
          The message contains all features in a given
          message.SNAPSHOT-The message contains all features at a specific point
          in
          time.PERM_DELTA-The message contains updates in a given time slice in
          features as a result of a baseline update.TEMP_DELTA-The message
          contains changes for some features in a given
          time slice representing a temporary event.
      last_modified_time {Date}:
          The date that will be used to filter the output to only features
          modified after that date.
      in_filter_layers {Table View}:
          The layers that will filter output to a smaller spatial subset. The
          input layers should be AIXM 5.1 feature types. This value should be in
          the same AIS geodatabase as the in_filter_layers parameter value.
      from_time {Date}:
          The starting time that will be applied to theandfields in the
          output message types for any missingorfield values in the features to
          export. The value will be converted to UTC. If a value is not
          specified, the current system date and time in UTC will be applied to
          the missing field values in the output message. validTime\begin
          PositionfeatureLifetime\beginPositionValidFrom_DateFeatureFrom_DateThi
          s parameter will be used differently depending on the export_type
          parameter value. BASELINE-The parameter will be honored only
          when the actual
          database record does not have theorattributes populated.
          FromFeature_DateValidFrom_Date         SNAPSHOT-The parameter value
          provided will be exported
          regardless of theandattributes in the database.
          FromFeature_DateValidFrom_Date         PERM_DELTA-The parameter will
          be honored only when the actual
          database record does not have theorattributes populated.
          FromFeature_DateValidFrom_Date         TEMP_DELTA-The parameter will
          be honored only when the actual
          database record does not have theor theattributes populated.
          FromFeature_DateValidFrom_Date
      to_time {Date}:
          The ending time that will be applied to theandfields in the
          output Baseline or Permanent Delta message types for any
          missingorfield values in the features to export. The value will be
          converted to UTC. If a value is not specified, the current system date
          and time in UTC will be applied to the missing field values in the
          output message. validTime\endPositionfeatureLifetime\endPositio
          nValidTo_DateFeatureTo_DateThis parameter is only valid when the
          export_type parameter is set to
          TEMP_DELTA.
      validate_output {Boolean}:
          Specifies whether the exported message will be validated for the XML
          format. You must be connected to the internet for validation to
          succeed.VALIDATE-The exported message will be validated for the XML
          format.NO_VALIDATE-The exported message will not be validated for the
          XML
          format. This is the default.

     OUTPUTS:
      out_message_file (File):
          The exported AIXM 5.1 message as an .xml file.
      out_validation_log {File}:
          The output XML validation log file.

        """