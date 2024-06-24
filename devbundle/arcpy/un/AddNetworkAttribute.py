# Generated documentation for module arcpy.un


class AddNetworkAttribute(object):
    """
    Adds a network attribute to a utility network.
    """

    @property
    def description(self) -> str:
        return """

        AddNetworkAttribute_un(in_utility_network, attribute_name, attribute_type, {is_inline}, {is_apportionable}, {domain}, {is_overridable}, {is_nullable}, {is_substitution}, {network_attribute_to_substitute})

        Adds a network attribute to a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The input utility network where the network attribute will be added.
      attribute_name (String):
          The name of the network attribute that will be added to the utility
          network.
      attribute_type (String):
          Specifies the data type of the network attribute.SHORT-The field type
          will be short.LONG-The field type will be
          long.DOUBLE-The field type will be double.DATE-The field type will be
          date.BIGINTEGER-The field type will be big integer.
      is_inline {Boolean}:
          Specifies whether the network attribute will be persisted in line. In-
          line network attributes are slightly more efficient, but the number of
          bits for user-defined in-line network attributes is limited to 25 per
          utility network. Store the most frequently used network attributes
          (for example, phase for electric networks, pressure for gas and water
          networks) in line if possible. The size of the bits is determined by
          the domain parameter. In-line attributes are only supported for
          integer network attributes (short or long).INLINE-The attribute will
          be added internally to the topology, making
          retrieval more efficient.NOT_INLINE-The attribute will be stored in an
          external table, and
          retrieval will require a call to the external weights table. This is
          the default.
      is_apportionable {Boolean}:
          Specifies whether the network attribute will be apportioned across
          multiple edges belonging to the same feature.Apportioned behavior is
          only supported with double network attributes.
          Network attributes with the apportionable property can be assigned to
          fields in line or junction feature classes, but only line features
          will have apportioned behavior.For example, with the shape_length
          network attribute and a line
          feature that consists of five edge elements of 20 feet each in which
          the total length of that line feature is 100 feet, the attribute will
          be apportioned across all edges. For example, using a function in a
          connected trace to count the shape_length attribute for this line will
          return a count of 5 because it accounts for each individual edge
          element and not the entire line. The distribution of the value depends
          on the percentage along each edge element with respect to the from
          point of the original feature.APPORTIONABLE-The network attribute will
          be
          apportioned.NOT_APPORTIONABLE-The network attribute will not be
          apportioned. This
          is the default.
      domain {String}:
          The domain with which the network attribute will be associated. This
          parameter is required when is_inline = "INLINE". This domain is used
          to determine the number of bits to allocate for the in-line attribute
          and must be a coded value type. For example, the LifeCycleStatusDomain
          (0, Unknown | 1, In-Service | 2, Proposed | 3, Abandoned) domain has
          four entries, which means 2 bits are required to store the in-line
          attribute. The coded value domain must have sequential codes starting
          from 0.
      is_overridable {Boolean}:
          Specifies whether the current value stored in the topology
          will be overridden using an external override table. This parameter
          can be used, for example, to input live data from external systems,
          such as present position in the case of electric or pressure value in
          the case of gas. An example is a SCADA system pushing the updated
          switching positions of Device A to the override table of the
          DeviceStatus network attribute, which the topology engine then uses to
          override its current value of device status for Device A with the
          override value. This parameter is not used in the current
          release, and any value
          provided will be ignored. The functionality of this parameter is under
          development and will be applicable in a future release.OVERRIDE-The
          current value stored in the topology will be
          overridden.NOT_OVERRIDABLE-The current value stored in the topology
          will not be
          overridden. This is the default.
      is_nullable {Boolean}:
          Specifies whether the network attribute will support null
          values.NULLABLE-The network attribute will support null values. This
          is the
          default.NOT_NULLABLE-The network attribute will not support null
          values.
      is_substitution {Boolean}:
          Specifies whether the network attribute will be used as a
          substitution. Substitution network attributes allow a substituted
          value to be used instead of bitset network attribute values during a
          propagation in a trace operation. Substitution is only supported with
          long integer network attributes.SUBSTITUTION-The network attribute
          will be used as a
          substitution.NOT_SUBSTITUTION-The network attribute will not be used
          as a
          substitution. This is the default.
      network_attribute_to_substitute {String}:
          The network attribute that will be used as a substitution.
          Substitutions are encoded based on the number of bits in the network
          attribute being propagated. The network attribute must be in line and
          an integer field type less than or equal to 8 bits.

        """