# Generated documentation for module arcpy.un


class ExportTraceConfigurations(object):
    """
    Exports named trace configurations from a utility network to JSON format (.json file).
    """

    @property
    def description(self) -> str:
        return """

        ExportTraceConfigurations_un(in_utility_network, trace_config_name;trace_config_name..., out_json_file)

        Exports named trace configurations from a utility network to JSON
        format (.json file).

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network containing the named trace configuration or
          configurations to export.
      trace_config_name (String):
          The named trace configuration or configurations to export.

     OUTPUTS:
      out_json_file (File):
          The output .json file.

        """