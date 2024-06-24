# Generated documentation for module arcpy.nd


class AddTraceRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically run a trace on a utility network or trace network during diagram building. The resulting traced network features and network objects are used to build the diagram content.
    """

    @property
    def description(self) -> str:
        return """

        AddTraceRule_nd(in_utility_network, template_name, is_active, {trace_type}, {domain_network}, {tier}, {target_tier}, {include_structures}, {include_barriers}, {condition_barriers;condition_barriers...}, {function_barriers;function_barriers...}, {traversability_scope}, {filter_barriers;filter_barriers...}, {filter_function_barriers;filter_function_barriers...}, {filter_scope}, {filter_bitset_network_attribute_name}, {filter_nearest}, {nearest_count}, {nearest_cost_network_attribute}, {nearest_categories;nearest_categories...}, {nearest_assets;nearest_assets...}, {propagators;propagators...}, {description}, {allow_indeterminate_flow}, {path_direction}, {path_network_weight_name}, {use_trace_config}, {trace_config_name}, {use_digitized_direction})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically run a trace on a utility network or trace
        network during diagram building. The resulting traced network features
        and network objects are used to build the diagram content.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network containing the diagram template
          that will be modified.
      template_name (String):
          The name of the diagram template that will be modified.
      is_active (Boolean):
          Specifies whether the rule will be enabled when generating and
          updating diagrams based on the specified template.ACTIVE-The added
          rule will become enabled during the generation and
          update of any diagrams based on the input template. This is the
          default.INACTIVE-The added rule will not become enabled during the
          generation
          or update of any diagrams based on the input template.
      trace_type {String}:
          Specifies the type of trace that will be run to build the diagram
          content.CONNECTED-A connected trace will be run from the utility
          network or
          trace network elements currently represented in the diagram when the
          rule starts and spans outward along connected elements. This is the
          default.SUBNETWORK-A subnetwork trace will be run from the utility
          network
          elements currently represented in the diagram when the rule starts and
          spans outward along connected elements to find sources or sinks from
          which it spans outward along the related subnetwork.UPSTREAM-An
          upstream trace will be run from the utility network or
          trace network elements currently represented in the diagram when the
          rule starts to discover elements upstream.DOWNSTREAM-A downstream
          trace will be run from the utility network or
          trace network elements currently represented in the diagram when the
          rule starts to discover elements downstream. SHORTEST_PATH-A
          shortest path trace will be run from the
          utility network or trace network features currently specified as
          starting points in the diagram when the rule starts to discover
          features along the shortest path between those starting points. The
          cost of traversing the path is determined based on the network
          attribute set for theparameter value / path_network_weight_name
          regardless of flow direction. Shortest Path Network Attribute
          Name
      domain_network {String}:
          The name of the domain network where the trace will be run for a
          utility network. This parameter is required when running the
          subnetwork, upstream, and downstream trace types.
      tier {String}:
          The name of the tier where the trace will start for a utility network.
          This parameter is optional when running the connected trace type; it
          is required when running the subnetwork, upstream, and downstream
          trace types.
      target_tier {String}:
          The name of the target tier to which the input tier will flow for a
          utility network. If this parameter is missing for upstream and
          downstream traces, those traces will stop when they reach the boundary
          of the starting subnetwork. This parameter can be used to allow these
          traces to continue either farther up or farther down the hierarchy.
      include_structures {Boolean}:
          Specifies whether structure features and objects will be included in
          the trace results.INCLUDE_STRUCTURES-Structure features and objects
          will be included in
          the trace results.EXCLUDE_STRUCTURES-Structure features and objects
          will not be included
          in the trace results. This is the default.
      include_barriers {Boolean}:
          Specifies whether the traversability barrier features will be included
          in the trace results. Traversability barriers are optional even if
          they have been preset in the subnetwork definition. This parameter
          does not apply to device features with
          terminals.INCLUDE_BARRIERS-Traversability barrier features will be
          included in
          the trace results. This is the default.EXCLUDE_BARRIERS-Traversability
          barrier features will not be included
          in the trace results.
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
          is specified in the name parameter.Value-Provide a specific value for
          the input attribute type that would
          cause termination based on the operator value.Combine Using-Set this
          value if you have multiple attributes to add.
          You can combine them using an And or an Or condition.The condition
          barriers operator value options are as follows:IS_EQUAL_TO-The
          attribute is equal to the value.DOES_NOT_EQUAL-The
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
          condition barriers Type value options are as
          follows:SPECIFIC_VALUE-Filter by a specific
          value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.The condition barriers Combine Using value options
          are as follows:AND-Combine the condition barriers.OR-Use if either
          condition barrier
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
          system.Operator-Choose from a number of different
          operators.Value-Provide a specific value for the input attribute type
          that, if
          discovered, will cause the termination.Use Local Values-Calculate
          values in each direction as opposed to an
          overall global value. For example, a function barrier that is
          calculating the sum of Shape length in which the trace terminates if
          the value is greater than or equal to 4. In the global case, after you
          traverse two edges with a value of 2, you will have reached a shape
          length sum of 4, so the trace stops. If local values are used, the
          local values along each path change, and the trace continues.The
          function barrier Function value options are as follows:AVERAGE-The
          average of the input values will be used.COUNT-The number
          of features will be used.MAX-The maximum of the input values will be
          used.MIN-The minimum of the input values will be used.ADD-The sum of
          the values will be used.SUBTRACT-The difference between the values
          will be used. Subnetwork
          controllers and loops trace types do not support the subtract
          function.The function barrier Operator value options are as
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
          in the value are present in the attribute (bitwise AND == False).The
          function barrier Use Local Values options are as follows:TRUE-Local
          values will be used.FALSE-Global values will be used. This
          is the default.
      traversability_scope {String}:
          The type of traversability that will be applied. Traversability scope
          determines whether traversability is applied at junctions, edges, or
          both. For example, if a condition barrier is defined to stop the trace
          if Device Status is equal to Open and traversability scope is set to
          edges only, even if the trace encounters an open device, the trace
          will not stop because Device Status is only applicable to junctions.
          In other words, this parameter indicates to the trace whether to
          ignore junctions, edges, or
          both.BOTH_JUNCTIONS_AND_EDGES-Traversability will be applied to both
          junctions and edges. This is the default.JUNCTIONS_ONLY-Traversability
          will be applied to junctions only.EDGES_ONLY-Traversability will be
          applied to edges only.
      filter_barriers {Value Table}:
          Specifies when a trace will stop for a specific category or network
          attribute. For example, stop a trace at features that have a life
          cycle status attribute that is equal to a certain value. This
          parameter is used to set a terminator based on a value of a network
          attribute that is defined in the system. If using more than one
          attribute, you can use the Combine Using option to define an And or an
          Or condition. Filter barrier components are as follows:
          Name-Filter
          by category or any network attribute defined in the
          system.Operator-Choose from a number of different
          operators.Type-Choose a specific value or network attribute from the
          value that
          is specified in the name parameter.Value-Provide a specific value of
          the input attribute type that would
          cause termination based on the operator value.Combine Using-Set this
          value if you have multiple attributes to add.
          You can combine them using an And or an Or condition.The filter
          barriers Operator value options are as follows:IS_EQUAL_TO-The
          attribute is equal to the value.DOES_NOT_EQUAL-The
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
          True).DOES_NOT_INLCUDE_ANY-A bitwise AND operation in which none of
          the bits
          in the value are present in the attribute (bitwise AND == False).The
          filter barriers Type value options are as
          follows:SPECIFIC_VALUE-Filter by a specific
          value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.The filter barriers Combine Using value options
          are as follows:AND-Combine the condition barriers.OR-Use if either
          condition barrier
          is met.
      filter_function_barriers {Value Table}:
          Filters the results of the trace for a specific category.
          Filter function barriers components are as follows:
          Function-Choose from a number of different calculation
          functions.Attribute-Filter by any network attribute defined in the
          system.Operator-Choose from a number of different
          operators.Value-Provide a specific value for the input attribute type
          that, if
          discovered, will cause the termination.Use Local Values-Calculate
          values in each direction as opposed to an
          overall global value. For example, a function barrier is calculating
          the sum of Shape length in which the trace terminates if the value is
          greater than or equal to 4. In the global case, after you traverse two
          edges with a value of 2, you will have reached a shape length sum of
          4, so the trace stops. If local values are used, the local values
          along each path change, or the trace continues.The filter function
          barriers Function value options are as follows:AVERAGE-The average of
          the input values will be used.COUNT-The number
          of features will be used.MAX-The maximum of the input values will be
          used.MIN-The minimum of the input values will be used.ADD-The sum of
          the values will be used.SUBTRACT-The difference between the values
          will be used. Subnetwork
          controllers and loops trace types do not support the subtract
          function.The filter function barriers Operator value options are as
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
          in the value are present in the attribute (bitwise AND == False).The
          filter function barriers Use Local Values options are as
          follows:TRUE-Local values will be used.FALSE-Global values will be
          used. This
          is the default.
      filter_scope {String}:
          Specifies whether the filter for a specific category will be applied
          to junctions, edges, or both. For example, if a filter barrier is
          defined to stop the trace if Device Status is equal to Open and
          traversability scope is set to edges only, the trace will not
          stop-even if the trace encounters an open device-because Device Status
          is only applicable to junctions. In other words, this parameter
          indicates to the trace whether to ignore junctions, edges, or
          both.BOTH_JUNCTIONS_AND_EDGES-The filter will be applied to both
          junctions
          and edges. This is the default.JUNCTIONS_ONLY-The filter will be
          applied to junctions only.EDGES_ONLY-The filter will be applied to
          edges only.
      filter_bitset_network_attribute_name {String}:
          The name of the network attribute that will be used to filter by
          bitset. This parameter is only applicable to upstream, downstream, and
          loops trace types. This parameter can be used to add special logic
          during a trace so the trace more closely reflects real-world
          scenarios. For example, for a loops trace, the Phases current network
          attribute can determine if the loop is a true electrical loop (the
          same phase is energized all around the loop, that is, A) and return
          only real electrical loops for the trace results. An example for an
          upstream trace is when tracing an electric distribution network,
          specify a Phases current network attribute, and the trace results will
          only include valid paths that are specified in the network attribute,
          not all paths.
      filter_nearest {Boolean}:
          Specifies whether the k-nearest neighbors algorithm will be used to
          return a number of features of a certain type within a given distance.
          You can provide a count and a cost as well as a collection of
          categories, an asset type, or both.FILTER_BY_NEAREST-The k-nearest
          neighbors algorithm will be used to
          return a number of features as specified in the nearest_count,
          nearest_cost_network_attribute, nearest_categories, or nearest_assets
          parameter.DO_NOT_FILTER-The k-nearest neighbors algorithm will not be
          used to
          filter results. This is the default.
      nearest_count {Long}:
          The number of features to be returned when filter_nearest is set to
          FILTER_BY_NEAREST.
      nearest_cost_network_attribute {String}:
          The numeric network attribute that will be used to calculate nearness,
          cost, or distance when filter_nearest is set to FILTER_BY_NEAREST-for
          example, shape length.
      nearest_categories {String}:
          The categories that will be returned when filter_nearest is set to
          FILTER_BY_NEAREST-for example, protective.
      nearest_assets {String}:
          The asset groups and asset types that will be returned when
          filter_nearest is set to FILTER_BY_NEAREST-for example,
          ElectricDistributionDevice/Transformer/Step Down.
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
          cause termination based on the operator value.The propagators Function
          value options are as follows:PROPAGATED_BITWISE_AND-Values will be
          compared from one feature to the
          next.PROPAGATED_MIN-The minimum value will be
          propagated.PROPAGATED_MAX-The maximum value will be propagated.The
          propagators Operator value options are as follows:IS_EQUAL_TO-The
          attribute is equal to the value.DOES_NOT_EQUAL-The
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
          in the value are present in the attribute (bitwise AND == False).This
          parameter is only available via Python.
      description {String}:
          The description of the rule.
      allow_indeterminate_flow {Boolean}:
          Specifies whether trace network features that have indeterminate or
          uninitialized flow will be traced. This parameter is only honored when
          running an upstream or downstream trace
          type.TRACE_INDETERMINATE_FLOW-Trace network features that have
          indeterminate or uninitialized flow direction in the trace will be
          included.IGNORE_INDETERMINATE_FLOW-Trace network features that have
          indeterminate or uninitialized flow direction will not be included.
          This is the default.
      path_direction {String}:
          Specifies the direction of the path for a trace network. The cost of
          traversing the path is determined by the path_network_weight_name
          parameter value. This parameter is only honored when running a
          SHORTEST_PATH trace type.NO_DIRECTION-The path will be between the two
          starting points
          regardless of the direction of flow. This is the
          default.PATH_UPSTREAM-The direction of the path will be downstream
          between the
          two starting points.PATH_DOWNSTREAM-The direction of the path will be
          upstream between the
          two starting points.
      path_network_weight_name {String}:
          The network attribute that will be used to calculate the path for a
          utility network or trace network. When running a shortest path trace
          type, the shortest path is calculated using a numeric network
          attribute such as shape length. Cost- and distance-based paths can
          both be achieved. This parameter is required when running a shortest
          path trace.
      use_trace_config {Boolean}:
          Specifies whether an existing named trace configuration will be used
          to define the properties of the trace. This parameter is only enabled
          for Utility Network version 7 and later.USE_TRACE_CONFIGURATION-An
          existing named trace configuration will be
          used to define the properties of the
          trace.DO_NOT_USE_TRACE_CONFIGURATION-An existing named trace
          configuration
          will not be used to define the properties of the trace. This is the
          default.
      trace_config_name {String}:
          The name of the existing named trace configuration that will be used
          to define the properties of the trace. This parameter is only enabled
          when the use_trace_config parameter is set to USE_TRACE_CONFIGURATION.
      use_digitized_direction {Boolean}:
          This parameter requires ArcGIS Enterprise 11.3 or later when
          using an enterprise geodatabase. Specifies whether
          upstream and downstream trace operations
          will determine flow using the digitized direction of the line and
          theattribute. This parameter is only available and active for Utility
          Network version 7 and later when the trace_type parameter is set to
          the UPSTREAM or DOWNSTREAM option. Flow
          directionUSE_DIGITIZED_DIRECTION-Trace operations will determine flow
          direction
          using the digitized direction of the line and the flow direction
          attribute. With this option, the domain_network, tier, and target_tier
          parameters are ignored.IGNORE_DIGITIZED_DIRECTION-Trace operations
          will determine flow
          direction based on the location of subnetwork controllers. This is the
          default.

        """