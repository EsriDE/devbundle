# Generated documentation for module arcpy.un


class AddTraceConfiguration(object):
    """
    Creates a named trace configuration in the utility network.
    """

    @property
    def description(self) -> str:
        return """

        AddTraceConfiguration_un(in_utility_network, trace_config_name, trace_type, {description}, {tags;tags...}, {domain_network}, {tier}, {target_tier}, {subnetwork_name}, {shortest_path_network_attribute_name}, {include_containers}, {include_content}, {include_structures}, {include_barriers}, {validate_consistency}, {condition_barriers;condition_barriers...}, {function_barriers;function_barriers...}, {traversability_scope}, {filter_barriers;filter_barriers...}, {filter_function_barriers;filter_function_barriers...}, {filter_scope}, {filter_bitset_network_attribute_name}, {filter_nearest}, {nearest_count}, {nearest_cost_network_attribute}, {nearest_categories;nearest_categories...}, {nearest_assets;nearest_assets...}, {functions;functions...}, {propagators;propagators...}, {output_assettypes;output_assettypes...}, {output_conditions;output_conditions...}, {include_isolated_features}, {ignore_barriers_at_starting_points}, {include_up_to_first_spatial_container}, {result_types;result_types...}, {allow_indeterminate_flow}, {validate_locatability}, {use_digitized_direction}, {synthesize_geometries})

        Creates a named trace configuration in the utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that will contain the new named trace
          configuration.
      trace_config_name (String):
          The name of the named trace configuration.
      trace_type (String):
          Specifies the type of trace that will be configured.CONNECTED-A
          connected trace that begins at one or more starting
          points and spans outward along connected features will be used. This
          is the default.SUBNETWORK-A subnetwork trace that begins at one or
          more starting
          points and spans outward to encompass the extent of the subnetwork
          will be used.SUBNETWORK_CONTROLLERS-A subnetwork controllers trace
          that locates
          sources and sinks on subnetwork controllers associated with a
          subnetwork will be used.UPSTREAM-An upstream trace that discovers
          features upstream from a
          location in the network will be used.DOWNSTREAM-A downstream trace
          that discovers features downstream from
          a location in the network will be used.LOOPS-Loops are areas of the
          network where flow direction is
          ambiguous. A loops trace that spans outward from the starting point
          based on connectivity will be used.SHORTEST_PATH-A shortest path trace
          that identifies the shortest path
          between two starting points will be used. ISOLATION-An
          isolation trace that discovers features that
          isolate an area of a network will be used. This trace type
          requires ArcGIS Enterprise 10.7 or later.
      description {String}:
          The description of the named trace configuration.
      tags {String}:
          A set of tags used to identify the named trace configuration. The tags
          can be used in search and indexing.
      domain_network {String}:
          The name of the domain network where the trace will be run. This
          parameter is required when running the subnetwork, subnetwork
          controllers, upstream, and downstream trace types.
      tier {String}:
          The name of the tier to start the trace. This parameter is required
          when running the subnetwork, subnetwork controllers, upstream, and
          downstream trace types.
      target_tier {String}:
          The name of the target tier to which the input tier flows. If this
          parameter is not specified for upstream and downstream traces, those
          traces will stop when they reach the boundary of the starting
          subnetwork. This parameter can be used to allow these traces to
          continue either farther up or farther down the hierarchy.
      subnetwork_name {String}:
          The name of the subnetwork where the trace will be run. This parameter
          can be used when running a subnetwork trace type. If a subnetwork name
          is specified, the starting_points parameter is not required.
      shortest_path_network_attribute_name {String}:
          The name of the network attribute used to calculate the shortest path.
          When running a shortest path trace type, the shortest path is
          calculated using a numeric network attribute such as shape length.
          Cost- and distance-based paths can both be achieved. This parameter is
          required when running a shortest path trace.
      include_containers {Boolean}:
          Specifies whether the container features will be included in the trace
          results.INCLUDE_CONTAINERS-Container features will be included in the
          trace
          results.EXCLUDE_CONTAINERS-Container features will not be included in
          the
          trace results. This is the default.
      include_content {Boolean}:
          Specifies whether the trace will return content in containers in the
          results.INCLUDE_CONTENT-Content in container features will be included
          in the
          trace results.EXCLUDE_CONTENT-Content in container features will not
          be included in
          the trace results. This is the default.
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
      validate_consistency {Boolean}:
          Specifies whether an error will be returned if dirty areas are
          encountered in any of the traversed features. This is the only way to
          guarantee a trace is passing through features with consistent status
          in the network. To remove dirty areas, validate the network
          topology.VALIDATE_CONSISTENCY-The trace will return an error if dirty
          areas are
          encountered in any of the traversed features. This is the
          default.DO_NOT_VALIDATE_CONSISTENCY-The trace will return results
          regardless
          of whether dirty areas are encountered in any of the traversed
          features.
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
          system.Operator-Choose from a number of operators.Type-Choose a
          specific value or network attribute from the value that
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
          Function-Choose from a number of calculation
          functions.Attribute-Filter by any network attribute defined in the
          system.Operator-Choose from a number of operators.Value-Provide a
          specific value for the input attribute type that, if
          discovered, will cause the termination.Use Local Values-Calculate
          values in each direction as opposed to an
          overall global value. For example, a function barrier that is
          calculating the sum of shape length in which the trace terminates if
          the value is greater than or equal to 4. In the global case, after you
          have traversed two edges with a value of 2, you will have already
          reached a shape length sum of 4, so the trace stops. If local values
          are used, the local values along each path change, and the trace
          continues.The function barrier function value options are as
          follows:AVERAGE-The average of the input values will be
          calculated.COUNT-The
          number of features will be identified.MAX-The maximum of the input
          values will be identified.MIN-The minimum of the input values will be
          identified.ADD-The sum of the values will be calculated.SUBTRACT-The
          difference between the values will be calculated.
          Subnetwork controllers and loops trace types do not support the
          subtract function.The function barrier operator value options are as
          follows:IS_EQUAL_TO-The function result is equal to the
          value.DOES_NOT_EQUAL-The function result is not equal to the
          value.IS_GREATER_THAN-The function result is greater than the
          value.IS_GREATER_THAN_OR_EQUAL_TO-The function result is greater than
          or
          equal to the value.IS_LESS_THAN-The function result is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The function result is less than or
          equal to
          the value.INCLUDES_THE_VALUES-A bitwise AND operation in which all
          bits in the
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
          Specifies whether traversability will be applied to junctions, edges,
          or both. For example, if a condition barrier is defined to stop the
          trace if Device Status is equal to Open and traversability scope is
          set to edges only, the trace will not stop-even if it encounters an
          open device-because Device Status is only applicable to junctions. In
          other words, this parameter indicates to the trace whether to ignore
          junctions, edges, or both.BOTH_JUNCTIONS_AND_EDGES-Traversability will
          be applied to both
          junctions and edges. This is the default.JUNCTIONS_ONLY-Traversability
          will be applied to junctions only.EDGES_ONLY-Traversability will be
          applied to edges only.
      filter_barriers {Value Table}:
          Specifies when a trace will stop for a specific category or network
          attribute. For example, stop a trace at features that have a life
          cycle status attribute that is equal to a certain value. This
          parameter is used to set a terminator based on a value of a network
          attribute that is defined in the system. If you're using more than one
          attribute, you can use the Combine Using option to define an And or an
          Or condition. Filter barrier components are as follows:
          Name-Filter
          by category or any network attribute defined in the
          system.Operator-Choose from a number of operators.Type-Choose a
          specific value or network attribute from the value that
          is specified in the name parameter.Value-Provide a specific value of
          the input attribute type that would
          cause termination based on the operator value.Combine Using-Set this
          value if you have multiple attributes to add.
          You can combine them using an And or an Or condition.The filter
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
          Function-Choose from a number of calculation
          functions.Attribute-Filter by any network attribute defined in the
          system.Operator-Choose from a number of operators.Value-Provide a
          specific value for the input attribute type that, if
          discovered, will cause the termination.Use Local Values-Calculate
          values in each direction as opposed to an
          overall global value. For example, a function barrier that is
          calculating the sum of shape length where the trace terminates if the
          value is greater than or equal to 4. In the global case, after you
          have traversed two edges with a value of 2, you will have already
          reached a shape length sum of 4, so the trace stops. If local values
          are used, the local values along each path change, or the trace
          continues.The filter function barriers function value options are as
          follows:AVERAGE-The average of the input values will be
          calculated.COUNT-The
          number of features will be identified.MAX-The maximum of the input
          values will be identified.MIN-The minimum of the input values will be
          identified.ADD-The sum of the values will be calculated.SUBTRACT-The
          difference between the values will be calculated.
          Subnetwork controllers and loops trace types do not support the
          subtract function.The filter function barriers operator value options
          are as follows:IS_EQUAL_TO-The attribute is equal to the
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
          When this parameter is used, you can specify a count and a cost as
          well as a collection of categories, an asset type, or
          both.FILTER_BY_NEAREST-The k-nearest neighbors algorithm will be used
          to
          return a number of features as specified in the nearest_count,
          nearest_cost_network_attribute, nearest_categories, or nearest_assets
          parameter.DO_NOT_FILTER-The k-nearest neighbors algorithm will not be
          used to
          filter results. This is the default.
      nearest_count {Long}:
          The number of features to be returned when filter_nearest is
          FILTER_BY_NEAREST.
      nearest_cost_network_attribute {String}:
          The numeric network attribute that will be used to calculate nearness,
          cost, or distance when filter_nearest is FILTER_BY_NEAREST-for
          example, shape length.
      nearest_categories {String}:
          The category or categories that will be returned when filter_nearest
          is FILTER_BY_NEAREST-for example, Protective.
      nearest_assets {String}:
          The asset groups and asset types that will be returned when
          filter_nearest is FILTER_BY_NEAREST-for example,
          ElectricDistributionDevice/Transformer/Step Down.
      functions {Value Table}:
          Applies a calculation function to the trace results. Functions
          components are as follows:        Function-Choose
          from a number of calculation
          functions.Attribute-Filter by any network attribute defined in the
          system.Filter Name-Filter the function results by attribute
          name.Filter Operator-Choose from a number of operators.Filter
          Type-Choose from a number of filter types.Filter Value-Provide a
          specific value for the input filter attribute.The functions Function
          value options are as follows:AVERAGE-The average of the input values
          will be calculated.COUNT-The
          number of features will be identified.MAX-The maximum of the input
          values will be identified.MIN-The minimum of the input values will be
          identified.ADD-The sum of the values will be calculated.
          SUBTRACT-The difference between the values will be
          calculated. Subnetwork controllers and loops trace types do
          not support the
          subtract function.For example, a starting point feature has a value of
          20. The next
          feature has a value of 30. If you are using the MINIMUM function, the
          result is 20, MAXIMUM is 30, ADD is 50, AVERAGE is 25, COUNT is 2, and
          SUBTRACT is -10.The Filter Operator value options are as
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
          functions Filter Type value options are as
          follows:SPECIFIC_VALUE-Filter by a specific
          value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.
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
          value options are as follows:PROPAGATED_BITWISE_AND-The values of one
          feature to the next will be
          compared.PROPAGATED_MIN-Get the minimum value.PROPAGATED_MAX-Get the
          maximum value.The propagators operator value options are as
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
          in the value are present in the attribute (bitwise AND == False).This
          parameter is only available in Python.
      output_assettypes {String}:
          Filters the output asset types to be included in the results-for
          example, only return overhead transformers.
      output_conditions {Value Table}:
          The types of features that will be returned based on a network
          attribute or category. For example, in a trace configured to filter
          out everything but Tap features, any traced features that do not have
          the Tap category assigned to them will not be included in the results.
          Any traced features that do will be returned in the result selection
          set. If you're using more than one attribute, you can use the Combine
          Using option to define an And or an Or condition. Output
          conditions components are as follows:
          Name-Filter by any network attribute defined in the
          system.Operator-Choose from a number of operators.Type-Choose a
          specific value or network attribute from the value that
          is specified in the name parameter.Value-Provide a specific value of
          the input attribute type that would
          cause termination based on the operator value.Combine Using-Set this
          value if you have multiple attributes to add.
          You can combine them using an And or an Or condition.The output
          conditions operator value options are as follows:IS_EQUAL_TO-The
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
          output conditions Type value options are as
          follows:SPECIFIC_VALUE-Filter by a specific
          value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.The output conditions Combine Using value options
          are as follows:AND-Combine the conditions.OR-Use if either condition
          is met.
      include_isolated_features {Boolean}:
          Specifies whether isolated features will be included in the trace
          results. This parameter is only used when running an isolation
          trace.INCLUDE_ISOLATED_FEATURES-Isolated features will be included in
          the
          trace results.EXCLUDE_ISOLATED_FEATURES-Isolated features will not be
          included in
          the trace results. This is the default.The isolation trace type
          requires ArcGIS Enterprise 10.7 or later when
          using an enterprise geodatabase.
      ignore_barriers_at_starting_points {Boolean}:
          Specifies whether dynamic barriers in the trace configuration will be
          ignored for starting points. This may be useful when performing an
          upstream protective device trace using the discovered protective
          devices (barriers) as starting points to find subsequent upstream
          protective devices.IGNORE_BARRIERS_AT_STARTING_POINTS-Barriers at
          starting points will be
          ignored in the
          trace.DO_NOT_IGNORE_BARRIERS_AT_STARTING_POINTS-Barriers at starting
          points
          will not be ignored in the trace. This is the default.
      include_up_to_first_spatial_container {Boolean}:
          Specifies whether the containers returned will be limited to those
          encountered up to, and including, the first spatial container for each
          network element in the trace results. If no spatial containers are
          encountered but nonspatial containers are present for a given network
          element, all nonspatial containers will be included in the results.
          This parameter is only enabled when Include Containers is
          INCLUDE_CONTAINERS.INCLUDE_UP_TO_FIRST_SPATIAL_CONTAINER-Only
          containers encountered up
          to, and including, the first spatial container will be included in the
          results when nested containment associations are encountered along the
          trace path. If no spatial containers exist, all nonspatial containers
          will be included in the results for a given network
          element.DO_NOT_INCLUDE_UP_TO_FIRST_SPATIAL_CONTAINER-All containers
          will be
          returned in the results. This is the default.
      result_types {String}:
          Specifies the type of results that will be returned by the
          trace.SELECTION-The trace results will be returned as a selection set
          on
          the appropriate network features. This is the
          default.AGGREGATED_GEOMETRY-The trace results will be aggregated by
          geometry
          type and stored in multipart feature classes displayed in layers in
          the active map.
      allow_indeterminate_flow {Boolean}:
          Specifies whether features with indeterminate flow will be traced.
          This parameter is only used when running an upstream, downstream, or
          isolation trace.TRACE_INDETERMINATE_FLOW-Features with indeterminate
          flow will be
          traced. This is the default.IGNORE_INDETERMINATE_FLOW-Features with
          indeterminate flow will stop
          traversability and will not be traced.
      validate_locatability {Boolean}:
          Specifies whether an error will be returned if nonspatial junction or
          edge objects are encountered without an associated container or
          structure in the association hierarchy for the traversed features.
          This parameter ensures that nonspatial objects returned by a trace are
          associated with spatial features.VALIDATE_LOCATABILITY-The trace will
          return an error if nonspatial
          junction or edge objects are encountered without an associated
          container or structure in the association hierarchy for the traversed
          features.DO_NOT_VALIDATE_LOCATABILITY-The trace will not perform a
          check for
          unlocatable objects and will return results regardless of whether
          unlocatable objects are present in the association hierarchy of the
          traversed features. This is the default.
      use_digitized_direction {Boolean}:
          This parameter requires ArcGIS Enterprise 11.3 or later when
          using an enterprise geodatabase. Specifies whether
          upstream and downstream trace operations
          will determine flow direction using the digitized direction of the
          line, the From and To global ID of the edge object in the association,
          and theattribute. This parameter is only available and active for
          utility network version 7 and later when the trace_type parameter is
          set to UPSTREAM or DOWNSTREAM. Flow
          directionUSE_DIGITIZED_DIRECTION-Trace operations will determine flow
          direction
          using the digitized direction of the line, the From and To global ID
          of the edge object in the association, and the flow direction
          attribute. With this option, the domain_network, tier, and target_tier
          parameters are ignored.IGNORE_DIGITIZED_DIRECTION-Trace operations
          will determine flow
          direction based on the location of subnetwork controllers. This is the
          default.
      synthesize_geometries {Boolean}:
          Specifies whether geometries will be inferred and created
          (synthesized) for associations and edge objects traversed as part of a
          trace operation. This parameter is only applicable to the aggregated
          geometry result type.DO_NOT_SYNTHESIZE_GEOMETRIES-Geometries will not
          be synthesized for
          the traversed associations and edge objects. This is the
          default.SYNTHESIZE_GEOMETRIES-Geometries will be inferred and created
          for the
          traversed associations and edge objects in the output
          Trace_Results_Aggregated_Lines feature class. This parameter
          requires ArcGIS Enterprise 11.3 or later when
          using an enterprise geodatabase.

        """