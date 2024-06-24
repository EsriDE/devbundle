# Generated documentation for module arcpy.un


class UpdateSubnetwork(object):
    """
    Updates subnetwork information in the Subnetworks table, the SubnetLine feature class, and subnetwork system diagrams for the specified subnetworks.
    """

    @property
    def description(self) -> str:
        return """

        UpdateSubnetwork_un(in_utility_network, domain_network, tier, all_subnetworks_in_tier, {subnetwork_name}, {continue_on_failure}, {condition_barriers;condition_barriers...}, {function_barriers;function_barriers...}, {include_barriers}, {traversability_scope}, {propagators;propagators...})

        Updates subnetwork information in the Subnetworks table, the
        SubnetLine feature class, and subnetwork system diagrams for the
        specified subnetworks.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the subnetwork.
      domain_network (String):
          The domain network that contains the subnetwork.
      tier (String):
          The tier that contains the subnetwork.
      all_subnetworks_in_tier (Boolean):
          Specifies whether all subnetworks in the tier will be updated. To
          update a subset of subnetworks in the tier, use the subnetwork_name
          parameter.ALL_SUBNETWORKS_IN_TIER-All subnetworks in the tier will be
          updated.
          This option uses asynchronous processing to update the subnetworks
          using the system UtilityNetworkTools geoprocessing service. The
          service is reserved for utility network geoprocessing tasks and has a
          longer default timeout setting. This is the
          default.SPECIFIC_SUBNETWORK-Only the subnetworks that are specified in
          the
          subnetwork_name parameter will be updated.
      subnetwork_name {String}:
          The name of the subnetwork that will be updated from the tier. If all
          subnetworks will be updated using the all_subnetworks_in_tier
          parameter, this parameter is ignored.
      continue_on_failure {Boolean}:
          Specifies whether the update process will stop if a subnetwork fails
          to update when updating multiple subnetworks.CONTINUE_ON_FAILURE-The
          update process will not stop if a subnetwork
          failure occurs; it will continue.STOP_ON_FAILURE-The update process
          will stop if a subnetwork failure
          occurs. This is the default.
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
          Name-Choose to filter by any network attribute defined in the
          system.Operator-Choose from a number of different
          operators.Type-Choose a specific value or network attribute from the
          value that
          is specified in the name parameter.Value-Set a specific value of the
          input attribute type that will cause
          termination based on the operator value.Combine Using-Set this value
          if you have multiple attributes to add.
          You can combine them using an And or an Or condition.The condition
          barrier Operator values are as follows:IS_EQUAL_TO-The attribute is
          equal to the value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation where all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation where not
          all of
          the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation where at least one bit in
          the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation where none of the
          bits in
          the value are present in the attribute (bitwise AND == False).The
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
          functions.Attribute-Choose to filter by any network attribute defined
          in the
          system.Operator-Choose from a number of different operators.Value-Set
          a specific value of the input attribute type that, if
          discovered, will cause the termination.Use Local Values-Calculate
          values in each direction as opposed to an
          overall global value, for example, for a function barrier that is
          calculating the sum of Shape length in which the trace terminates if
          the value is greater than or equal to 4. In the global case, after you
          have traversed two edges with a value of 2, you have already reached a
          shape length sum of 4, so the trace stops. If local values are used,
          the local values along each path change, so the trace goes
          farther.TRUE-Local values will be used.FALSE-Global values will be
          used. This
          is the default.Possible values for the function barrier function
          options are as
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
          value.INCLUDES_THE_VALUES-A bitwise AND operation where all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation where not
          all of
          the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation where at least one bit in
          the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation where none of the
          bits in
          the value are present in the attribute (bitwise AND == False).
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
          Specifies the type of traversability that will be enforced.
          Traversability scope determines whether traversability will be
          enforced at junctions, edges, or both. For example, if a condition
          barrier is defined to stop the trace if DEVICESTATUS is equal to Open
          and traversability scope is set to edges only, the trace will not
          stop-even if the trace encounters an open device-because DEVICESTATUS
          is only applicable to junctions. In other words, this parameter
          indicates to the trace whether to ignore junctions, edges, or
          both.BOTH_JUNCTIONS_AND_EDGES-Traversability will be applied to both
          junctions and edges. This is the default.JUNCTIONS_ONLY-Traversability
          will be applied only to junctions.EDGES_ONLY-Traversability will be
          applied only to edges.
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
          cause termination based on the operator value.The propagators function
          value options are as follows:PROPAGATED_BITWISE_AND-Compare the values
          from one feature to the
          next.PROPAGATED_MIN-Get the minimum value.PROPAGATED_MAX-Get the
          maximum value.The propagators operator value options are as
          follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation where all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation where not
          all of
          the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation where at least one bit in
          the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation where none of the
          bits in
          the value are present in the attribute (bitwise AND == False).

        """