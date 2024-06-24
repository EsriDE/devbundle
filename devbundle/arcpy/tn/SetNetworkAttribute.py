# Generated documentation for module arcpy.tn


class SetNetworkAttribute(object):
    """
    Assigns a network attribute to a feature class to be used during trace operations.
    """

    @property
    def description(self) -> str:
        return """

        SetNetworkAttribute_tn(in_trace_network, network_attribute, featureclass, field)

        Assigns a network attribute to a feature class to be used during trace
        operations.

     INPUTS:
      in_trace_network (Trace Network / Trace Network Layer):
          The trace network that contains the network attribute to set.
      network_attribute (String):
          The network attribute to be assigned to the feature class field.
      featureclass (String):
          The input feature class that contains the field that will be used to
          set the network attribute.
      field (String):
          An existing field that will be assigned the network attribute. The
          field data type must match the data type of the network attribute. For
          example, if the network attribute is a short integer type, the field
          must also be a short integer type. Network attributes that do not
          support null values can only be assigned to fields that do not allow
          null values.

        """