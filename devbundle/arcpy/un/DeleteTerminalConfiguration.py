# Generated documentation for module arcpy.un


class DeleteTerminalConfiguration(object):
    """
    Deletes a terminal configuration from a utility network.
    """

    @property
    def description(self) -> str:
        return """

        DeleteTerminalConfiguration_un(in_utility_network, terminal_configuration_name)

        Deletes a terminal configuration from a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the terminal configuration to be
          deleted.
      terminal_configuration_name (String):
          The name of the terminal configuration to delete.

        """