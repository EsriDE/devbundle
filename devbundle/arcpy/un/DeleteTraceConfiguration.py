# Generated documentation for module arcpy.un


class DeleteTraceConfiguration(object):
    """
    Deletes one or more named trace configurations from a utility network.
    """

    @property
    def description(self) -> str:
        return """

        DeleteTraceConfiguration_un(in_utility_network, trace_config_name;trace_config_name...)

        Deletes one or more named trace configurations from a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network containing the named trace configuration to be
          deleted.
      trace_config_name (String):
          The named trace configurations to be deleted.

        """