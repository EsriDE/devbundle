# Generated documentation for module arcpy.tn


class DeleteTraceConfiguration(object):
    """
    Deletes one or more named trace configurations from a trace network.
    """

    @property
    def description(self) -> str:
        return """

        DeleteTraceConfiguration_tn(in_trace_network, trace_config_name;trace_config_name...)

        Deletes one or more named trace configurations from a trace network.

     INPUTS:
      in_trace_network (Trace Network / Trace Network Layer):
          The trace network containing the named trace configuration to be
          deleted.
      trace_config_name (String):
          The named trace configurations to be deleted.

        """