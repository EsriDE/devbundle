# Generated documentation for module arcpy.un


class ExportSubnetwork(object):
    """
    Exports subnetworks from a utility network into a .json file. This tool also allows you to delete a row in the Subnetworks table as long as the Is deleted attribute is set to true. This indicates that the subnetwork controller has been removed from the subnetwork.
    """

    @property
    def description(self) -> str:
        return """

        ExportSubnetwork_un(in_utility_network, domain_network, tier, subnetwork_name, export_acknowledged, out_json_file, {condition_barriers;condition_barriers...}, {function_barriers;function_barriers...}, {include_barriers}, {traversability_scope}, {propagators;propagators...}, {include_geometry}, {result_types;result_types...}, {result_network_attributes;result_network_attributes...}, {result_fields;result_fields...}, {include_domain_descriptions})

        Exports subnetworks from a utility network into a .json file. This
        tool also allows you to delete a row in the Subnetworks table as long
        as the Is deleted attribute is set to true. This indicates that the
        subnetwork controller has been removed from the subnetwork.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the subnetwork to export.
      domain_network (String):
          The domain network that contains the subnetwork.
      tier (String):
          The tier that contains the subnetwork.
      subnetwork_name (String):
          The name of the subnetwork that will be exported from the tier. Select
          a specific source to export the corresponding subnetwork information.
      export_acknowledged (Boolean):
          Specifies whether theattribute for the corresponding
          controller in the Subnetworks table and feature in the SubnetLine
          feature class will be updated. LASTACKEXPORTSUBNETWORK
          ACKNOWLEDGE-Theattribute for the corresponding controller in
          the Subnetworks table will be updated. If the source has been marked
          for deletion (Is deleted = True), it will be deleted from the
          Subnetworks table. This option requires that the input utility network
          reference the default version. LASTACKEXPORTSUBNETWORK
          NO_ACKNOWLEDGE-Theattribute for the corresponding controller
          in the Subnetworks table will not be updated. This is the default.
          LASTACKEXPORTSUBNETWORK
      condition_barriers {Value Table}:
          Sets a traversability barrier condition on features based on a
          comparison to a network attribute or check for a category string. A
          condition barrier uses a network attribute, an operator and a type,
          and an attribute value. For example, stop a trace when a feature has
          theattribute equal to the specific value of Open. When a feature meets
          this condition, the trace stops. If you're using more than one
          attribute, you can use theparameter to define an And or an Or
          condition. Device StatusCombine using        Condition barrier
          components are as follows:
          Name-Filter by any network attribute defined in the
          system.Operator-Choose from a number of different
          operators.Type-Choose a specific value or network attribute from the
          value that
          is specified in the name parameter.Value-Set a specific value of the
          input attribute type that will cause
          termination based on the operator value.Combine Using-Set this value
          if you have multiple attributes to add.
          You can combine them using an And or an Or condition.The condition
          barrier operator values are as follows:IS_EQUAL_TO-The attribute is
          equal to the value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation in which all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation in which
          not all
          of the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation in which at least one bit
          in the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation in which none of
          the bits
          in the value are present in the attribute (bitwise AND == False).The
          condition barrier type options are as follows:SPECIFIC_VALUE-Filter by
          a specific value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.The Combine Using values are as
          follows:AND-Combine the condition barriers.OR-Use if either condition
          barrier
          is met.
      function_barriers {Value Table}:
          Sets a traversability barrier on features based on a function.
          Function barriers can be used to do such things as restrict how far
          the trace travels from the starting point, or set a maximum value to
          stop a trace. For example, the length of each line traveled is added
          to the total distance traveled so far. When the total length traveled
          reaches the value specified, the trace stops. Function barrier
          components are as follows:
          Function-Choose from a number of different calculation
          functions.Attribute-Filter by any network attribute defined in the
          system.Operator-Choose from a number of different operators.Value-Set
          a specific value of the input attribute type that, if
          discovered, will cause the termination.Use Local Values-Calculate
          values in each direction as opposed to an
          overall global value. For example, use for a function barrier that is
          calculating the sum of Shape length where the trace terminates if the
          value is greater than or equal to 4. In the global case, after you
          have traversed two edges with a value of 2, you have already reached a
          shape length sum of 4, so the trace stops. If local values are used,
          the local values along each path change, so the trace goes
          farther.TRUE-Use local values.FALSE-Use global values. This is the
          default.Possible values for the function barrier function options are
          as
          follows:AVERAGE-The average of the input values.COUNT-The number of
          features.MAX-The maximum of the input values.MIN-The minimum of the
          input values.ADD-Add the values.SUBTRACT-Subtract the values.
          Subnetwork controllers and loops trace
          types do not support the subtract function.For example, the starting
          point feature has a value of 20. The next
          feature has a value of 30. If you use the minimum function, the result
          is 20, maximum is 30, add is 50, average is 25, count is 2, and
          subtract is -10.The function barrier operator value options are as
          follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation in which all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation in which
          not all
          of the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation in which at least one bit
          in the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation in which none of
          the bits
          in the value are present in the attribute (bitwise AND == False).
      include_barriers {Boolean}:
          Specifies whether the traversability barrier features will be included
          in the trace results. Traversability barriers are optional even if
          they have been preset in the subnetwork
          definition.INCLUDE_BARRIERS-Traversability barriers will be included
          in the trace
          results. This is the default.EXCLUDE_BARRIERS-Traversability barriers
          will not be included in the
          trace results.
      traversability_scope {String}:
          Specifies the type of traversability that will be applied.
          Traversability scope determines whether traversability is applied to
          junctions, edges, or both. For example, if a condition barrier is
          defined to stop the trace if DEVICESTATUS is set to Open and the
          traversability scope is set to edges only, the trace will not stop
          even if the trace encounters an open device, because DEVICESTATUS is
          only applicable to junctions. In other words, this parameter indicates
          to the trace whether to ignore junctions, edges, or
          both.BOTH_JUNCTIONS_AND_EDGES-Traversability will be applied to both
          junctions and edges.JUNCTIONS_ONLY-Traversability will be applied to
          junctions only.EDGES_ONLY-Traversability will be applied to edges
          only.
      propagators {Value Table}:
          Specifies the network attributes to propagate as well as how that
          propagation will occur during a trace. Propagated class attributes
          denote the key values on subnetwork controllers that are disseminated
          to the rest of the features in the subnetwork. For example, in an
          electric distribution model, you can propagate the phase value.
          Propagators components are as follows:        Attribute-Filter
          by any network attribute defined in the
          system.Substitution Attribute-Use a substituted value instead of
          bitset
          network attribute values. Substitutions are encoded based on the
          number of bits in the network attribute being propagated. A
          substitution is a mapping of each bit in phase to another bit. For
          example, for Phase AC, one substitution could map bit A to B, and bit
          C to null. In this example, the substitution for 1010 (Phase AC) is
          0000-0010-0000-0000 (512). The substitution captures the mapping so
          you know that Phase A was mapped to B and Phase C was mapped to null,
          and not the other way around (that is, Phase A was not mapped to null
          and Phase C was not mapped to B).Function-Choose from a number of
          calculation functions.Operator-Choose from a number of
          operators.Value-Provide a specific value for the input attribute type
          that would
          cause termination based on the operator value.Possible values for the
          propagators function are as follows:PROPAGATED_BITWISE_AND-Compare the
          values from one feature to the
          next.PROPAGATED_MIN-Get the minimum value.PROPAGATED_MAX-Get the
          maximum value.The propagator operator values are as
          follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation in which all bits in
          the
          value are present in the attribute (bitwise AND == value).DOES NOT
          INCLUDE_THE_VALUES-A bitwise AND operation in which not all
          of the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation in which at least one bit
          in the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INLCUDE_ANY-A bitwise AND operation in which none of
          the bits
          in the value are present in the attribute (bitwise AND == False).
      include_geometry {Boolean}:
          Specifies whether geometry will be included in the
          results.INCLUDE_GEOMETRY-Geometry will be included in the
          results.EXCLUDE_GEOMETRY-Geometry will not be included in the results.
          This is
          the default.For enterprise geodatabases, this parameter requires
          ArcGIS Enterprise
          10.7 or later.
      result_types {String}:
          Specifies the types of results that will be
          returned.CONNECTIVITY-Features that are connected through geometric
          coincidence
          or connectivity associations will be returned. This is the
          default.FEATURES-Feature-level information will be
          returned.CONTAINMENT_AND_ATTACHMENT_ASSOCIATIONS-Features that are
          associated
          through containment and structural attachment associations will be
          returned.For enterprise geodatabases, this parameter requires ArcGIS
          Enterprise
          10.7 or later.The containment and attachment associations option
          requires ArcGIS
          Enterprise 10.8.1 or later.
      result_network_attributes {String}:
          The network attributes that will be included in the results.For
          enterprise geodatabases, this parameter requires ArcGIS Enterprise
          10.7 or later.
      result_fields {Value Table}:
          Fields from a feature class that will be returned as results. The
          values of the field will be returned in the results for the features
          in the subnetwork.For enterprise geodatabases, this parameter requires
          ArcGIS Enterprise
          10.7 or later.
      include_domain_descriptions {Boolean}:
          Specifies whether domain descriptions will be included in the output
          .json to communicate domain mapping for controllers, featureElements,
          connectivity, and associations.INCLUDE_DOMAIN_DESCRIPTIONS-Domain
          descriptions will be included in
          the results.EXCLUDE_DOMAIN_DESCRIPTIONS-Domain descriptions will not
          be included
          in the results. This is the default.For enterprise geodatabases, this
          parameter requires ArcGIS Enterprise
          10.9.1 or later.

     OUTPUTS:
      out_json_file (File):
          The name and location of the .json file that will be generated.

        """