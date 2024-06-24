# Generated documentation for module arcpy.un


class SetTerminalConfiguration(object):
    """
    Assigns a terminal configuration to an asset type in a utility network.
    """

    @property
    def description(self) -> str:
        return """

        SetTerminalConfiguration_un(in_utility_network, domain_network, device_featureclass, assetgroup, assettype, terminal_configuration)

        Assigns a terminal configuration to an asset type in a utility
        network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network containing the terminal configuration that will be
          assigned to a specific asset type.
      domain_network (String):
          The domain network to which the asset type belongs.
      device_featureclass (String):
          The utility network feature class or table to which the asset type
          belongs.
      assetgroup (String):
          The asset group to which the asset type belongs.
      assettype (String):
          The asset type that will receive the terminal configuration.
      terminal_configuration (String):
          The terminal configuration that will be assigned to the asset type.

        """