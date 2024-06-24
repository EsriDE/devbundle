# Generated documentation for module arcpy.un


class SetNetworkCategory(object):
    """
    Assigns a network category to a feature class or table at the asset type level to be used during tracing operations.
    """

    @property
    def description(self) -> str:
        return """

        SetNetworkCategory_un(in_utility_network, domain_network, featureclass, assetgroup, assettype, {category;category...})

        Assigns a network category to a feature class or table at the asset
        type level to be used during tracing operations.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the network category.
      domain_network (String):
          The domain network in the utility network that contains the network
          category.
      featureclass (String):
          The utility network feature class or table to which the asset type
          belongs.
      assetgroup (String):
          The asset group to which the asset type belongs.
      assettype (String):
          The asset type to alter the category configuration.
      category {String}:
          The categories to be assigned to the asset type. The categories that
          are specified for this parameter will replace the current categories
          that are assigned to the asset type. To unassign a network category
          from an asset type, do not specify a category for this parameter.
          Thesystem-provided network category is only available for
          asset types in the device feature class and junction object table. In
          a domain network with a partitioned tier definition, the selected
          asset type must also have a directional terminal configuration
          assigned with a minimum of one upstream and one downstream terminal.
          Subnetwork Controller

        """