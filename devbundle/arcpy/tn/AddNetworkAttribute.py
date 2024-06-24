# Generated documentation for module arcpy.tn


class AddNetworkAttribute(object):
    """
    Adds a network attribute to a trace network.
    """

    @property
    def description(self) -> str:
        return """

        AddNetworkAttribute_tn(in_trace_network, attribute_name, attribute_type, {is_nullable}, {is_apportionable})

        Adds a network attribute to a trace network.

     INPUTS:
      in_trace_network (Trace Network / Trace Network Layer):
          The input trace network to which the network attribute will be added.
      attribute_name (String):
          The name of the network attribute to add to the trace network.
      attribute_type (String):
          Specifies the data type of the network attribute.SHORT-The field type
          will be short.LONG-The field type will be
          long.DOUBLE-The field type will be double.DATE-The field type will be
          date.
      is_nullable {Boolean}:
          Specifies whether the network attribute will support null
          values.NULLABLE-The network attribute will support null
          values.NOT_NULLABLE-The network attribute will not support null
          values. This
          is the default.
      is_apportionable {Boolean}:
          Specifies whether the network attribute will be apportioned across
          multiple edges belonging to the same feature.Apportioned behavior is
          only supported with double network attributes.
          Network attributes with the apportionable property can be assigned to
          fields in line or point feature classes, but only line features will
          have apportioned behavior.To illustrate, consider the shape_length
          network attribute and a line
          feature that consists of five edge elements of 20 feet each, where the
          total length of that line feature is 100 feet. This attribute will be
          apportioned across all edges. For example, using a function in a
          connected trace to count the shape_length attribute for this line will
          return a count of 5 because it accounts for each individual edge
          element and not the entire line. The distribution of the value depends
          on the percentage along each edge element with respect to the from
          point of the original feature.APPORTIONABLE-The network attribute will
          be
          apportioned.NOT_APPORTIONABLE-The network attribute will not be
          apportioned. This
          is the default.

        """