# Generated documentation for module arcpy.tn


class ImportTraceConfigurations(object):
    """
    Imports named trace configurations from JSON format (.json file) to a trace network.
    """

    @property
    def description(self) -> str:
        return """

        ImportTraceConfigurations_tn(in_trace_network, in_json_file)

        Imports named trace configurations from JSON format (.json file) to a
        trace network.

     INPUTS:
      in_trace_network (Trace Network / Trace Network Layer):
          The target trace network to which the named trace configurations will
          be imported.
      in_json_file (File):
          The .json file containing the named trace configurations to import.

        """