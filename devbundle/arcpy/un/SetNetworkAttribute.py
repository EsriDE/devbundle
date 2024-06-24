# Generated documentation for module arcpy.un


class SetNetworkAttribute(object):
    """
    Assigns a network attribute to a feature class or table at the asset type level to be used during tracing operations.
    """

    @property
    def description(self) -> str:
        return """

        SetNetworkAttribute_un(in_utility_network, network_attribute, domain_network, featureclass, field)

        Assigns a network attribute to a feature class or table at the asset
        type level to be used during tracing operations.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the network attribute to set.
      network_attribute (String):
          The network attribute to be assigned to the field in the feature class
          or table.
      domain_network (String):
          The domain network that contains the feature class or table that will
          have a network attribute set on it.
      featureclass (String):
          The input feature class or table that contains the field that will be
          used to set the network attribute.
      field (String):
          An existing field that will be assigned the network attribute. The
          field data type must match the data type of the network attribute. For
          example, if the network attribute is a short integer type, the field
          must also be a short integer type. Network attributes that do not
          support nulls can only be assigned to fields that do not allow null
          values.

        """