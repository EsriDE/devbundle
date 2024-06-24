# Generated documentation for module arcpy.tn


class ExportTraceConfigurations(object):
    """
    Exports named trace configurations from a trace network to JSON format (.json file).
    """

    @property
    def description(self) -> str:
        return """

        ExportTraceConfigurations_tn(in_trace_network, trace_config_name;trace_config_name..., out_json_file)

        Exports named trace configurations from a trace network to JSON format
        (.json file).

     INPUTS:
      in_trace_network (Trace Network / Trace Network Layer):
          The trace network containing the named trace configuration or
          configurations to export.
      trace_config_name (String):
          The named trace configuration or configurations to export.

     OUTPUTS:
      out_json_file (File):
          The output .json file.

        """