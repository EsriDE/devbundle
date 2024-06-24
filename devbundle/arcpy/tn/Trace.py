# Generated documentation for module arcpy.tn


class Trace(object):
    """
    Returns selected features in a trace network based on connectivity or traversability from the specified starting points.
    """

    @property
    def description(self) -> str:
        return """

        Trace_tn(in_trace_network, {trace_type}, {starting_points}, {barriers}, {path_direction}, {shortest_path_network_attribute_name}, {include_barriers}, {validate_consistency}, {ignore_barriers_at_starting_points}, {allow_indeterminate_flow}, {condition_barriers;condition_barriers...}, {function_barriers;function_barriers...}, {traversability_scope}, {functions;functions...}, {output_conditions;output_conditions...}, {result_types;result_types...}, {selection_type}, {clear_all_previous_trace_results}, {trace_name}, {aggregated_points}, {aggregated_lines}, {out_network_layer}, {use_trace_config}, {trace_config_name}, {out_json_file})

        Returns selected features in a trace network based on connectivity or
        traversability from the specified starting points.

     INPUTS:
      in_trace_network (Trace Network / Trace Network Layer):
          The trace network on which the trace will be run. When working with an
          enterprise geodatabase, an input trace network must be from a feature
          service; a trace network from a database connection is not supported.
      trace_type {String}:
          Species the type of trace to execute.CONNECTED-A connected trace that
          begins at one or more starting points
          and spans outward along connected features will be used.UPSTREAM-An
          upstream trace that discovers features upstream from a
          location in the network will be used. This type of trace requires the
          flow direction to be set.DOWNSTREAM-A downstream trace that discovers
          features downstream from
          a location in the network will be used. This type of trace requires
          the flow direction to be set.SHORTEST_PATH-A shortest path trace that
          finds the shortest path
          between two starting points in the network regardless of flow
          direction will be used. The cost of traversing the path is determined
          based on the network attribute set for the
          shortest_path_network_attribute_name parameter.
      starting_points {Table View / Feature Layer}:
          A feature layer created using thetab in thepane, or a table or
          feature class containing one or more records that represent the
          starting points of the trace. The TN_Temp_Starting_Points feature
          class is used by default and is generated in the default geodatabase
          of the project when you create starting points using thetool in
          thepane. Starting PointsTrace LocationsStarting PointsTrace
          Locations
      barriers {Table View / Feature Layer}:
          A table or feature class containing one or more features that
          represent the barriers of the trace that prevent the trace from
          traversing beyond that point. The TN_Temp_Barriers feature class is
          used by default and is generated in the default geodatabase of the
          project when you create barriers using thetab in thepane.
          BarriersTrace Locations
      path_direction {String}:
          Specifies the direction of the trace path. The cost of traversing the
          path is determined by the shortest_path_network_attribute_name
          parameter value. This parameter is only honored when running a
          SHORTEST_PATH trace type.NO_DIRECTION-The path between the two
          starting points, regardless of
          the direction of flow, will be used. This is the
          default.PATH_UPSTREAM-The upstream path between the two starting
          points will
          be used.PATH_DOWNSTREAM-The downstream path between the two starting
          points
          will be used.
      shortest_path_network_attribute_name {String}:
          The name of the network attribute used to calculate the path. When
          running a shortest path trace type, the shortest path is calculated
          using a numeric network attribute such as shape length. Cost and
          distance based paths can both be achieved. This parameter is required
          when running a shortest path trace.
      include_barriers {Boolean}:
          Specifies whether the traversability barrier features will be included
          in the trace results.INCLUDE_BARRIERS-Traversability barrier features
          will be included in
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
      ignore_barriers_at_starting_points {Boolean}:
          Specifies whether barriers in the trace configuration will be ignored
          for starting points.IGNORE_BARRIERS_AT_STARTING_POINTS-Barriers at
          starting points will be
          ignored in the
          trace.DO_NOT_IGNORE_BARRIERS_AT_STARTING_POINTS-Barriers at starting
          points
          will not be ignored in the trace. This is the default.
      allow_indeterminate_flow {Boolean}:
          Specifies whether features with indeterminate or uninitialized flow
          will be traced. This parameter is only honored when running an
          upstream or downstream trace.TRACE_INDETERMINATE_FLOW-Features with
          indeterminate or uninitialized
          flow direction will be traced.IGNORE_INDETERMINATE_FLOW-Features with
          indeterminate or uninitialized
          flow direction will not be traced. This is the default.
      condition_barriers {Value Table}:
          Sets a traversability barrier condition on features based on a
          comparison to a network attribute. A condition barrier uses a network
          attribute, an operator and a type, and an attribute value. For
          example, stop a trace when a feature has theattribute equal to the
          specific value of ArtificialPath. When a feature meets this condition,
          the trace stops. If you're using more than one attribute, you can use
          the Combine Using component to define an And or an Or condition.
          Code        Condition barrier components are as follows:
          Name-Filter by any network attribute defined in the
          system.Operator-Choose from a number of different
          operators.Type-Choose a specific value or network attribute from the
          value
          specified in the Name component.Value-Provide a specific value for the
          input attribute type that would
          cause termination based on the operator value.Combine Using-Set this
          value if you have multiple attributes to add.
          You can combine them using an And or an Or condition.Operator
          components are as follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.Type components are as follows:SPECIFIC_VALUE-Filter by a
          specific value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.Combine Using component are as follows:AND-Combine
          the condition barriers.OR-Use if either condition barrier
          is met.
      function_barriers {Value Table}:
          Sets a traversability barrier on features based on a function.
          Function barriers can be used, for example, to restrict how far the
          trace travels from the starting point or to set a maximum value to
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
          overall global value. For example, a function barrier calculates the
          sum of shape length in which the trace terminates if the value is
          greater than or equal to 4. In the global case, after you have
          traversed two edges with a value of 2, you have already reached a
          shape length sum of 4, so the trace stops. If local values are used,
          the local values along each path change, and the trace
          continues.Function components are as follows:AVERAGE-The average of
          the input values.COUNT-The number of
          features.MAX-The maximum of the input values.MIN-The minimum of the
          input values.ADD-Add the values.SUBTRACT-Subtract the values.Operator
          components are as follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.Use Local Values components are as follows:TRUE-Use local
          values.FALSE-Use global values. This is the default.
      traversability_scope {String}:
          Specifies the type of traversability that will be applied.
          Traversability scope determines whether traversability is applied to
          junctions, edges, or both. For example, in a network of recreational
          trails, if a condition barrier is defined to stop the trace if the
          path type is gravel and traversability scope is set to junctions only,
          the trace will not stop even if it encounters a gravel path, because
          the path type is only applicable to
          edges.BOTH_JUNCTIONS_AND_EDGES-Traversability will be applied to both
          junctions and edges. This is the default.JUNCTIONS_ONLY-Traversability
          will be applied to junctions only.EDGES_ONLY-Traversability will be
          applied to edges only.
      functions {Value Table}:
          The calculation function or functions that will be applied to the
          trace results. Functions components are as follows:
          Function-Choose
          from a number of calculation
          functions.Attribute-Filter by any network attribute defined in the
          system.Filter Name-Filter the function results by attribute
          name.Filter Operator-Choose from a number of operators.Filter
          Type-Choose from a number of filter types.Filter Value-Provide a
          specific value for the input filter attribute.Function component
          options are as follows:AVERAGE-The average of the input
          values.COUNT-The number of
          features.MAX-The maximum of the input values.MIN-The minimum of the
          input values.ADD-The sum of the values.SUBTRACT-The difference between
          the values.For example, you have a starting point feature with a value
          of 20. The
          next feature has a value of 30. If you are using the MIN function, the
          result is 20. MAX is 30, ADD is 50, AVERAGE is 25, COUNT is 2, and
          SUBTRACT is -10.Filter Operator component options are as
          follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.Filter Type component options are as
          follows:SPECIFIC_VALUE-Filter by a specific
          value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.
      output_conditions {Value Table}:
          The types of features that will be returned based on a network
          attribute. For example, in a trace configured to filter out everything
          but Tap features, any traced features that do not have the Tap
          attribute assigned to them are not included in the results. Any traced
          features that do are returned in the result selection set. If using
          more than one attribute, you can use the Combine Using option to
          define an And or an Or condition. Output conditions components
          are as follows:
          Name-Filter by any network attribute defined in the
          system.Operator-Choose from a number of operators.Type-Choose a
          specific value or network attribute from the value
          =specified in the Name component.Value-Provide a specific value of the
          input attribute type that would
          cause termination based on the operator value.Combine Using-Set this
          value if you have multiple attributes to add.
          You can combine them using an And or an Or condition.Operator
          component options are as follows:IS_EQUAL_TO-The attribute is equal to
          the value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.Type component options are as follows:SPECIFIC_VALUE-Filter by a
          specific value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.Combine Using component options are as
          follows:AND-Combine the conditions.OR-Use if either condition is met.
      result_types {String}:
          Specifies the type of results that will be returned by the
          trace.SELECTION-The trace results will be returned as a selection set
          on
          the appropriate network features. This is the
          default.AGGREGATED_GEOMETRY-The trace results will be aggregated by
          geometry
          type and stored in feature classes displayed in layers in the active
          map.NETWORK_LAYERS-The trace results will be added to feature layers
          as a
          selection set in a group layer. CONNECTIVITY-The trace results
          will be returned as a
          connectivity graph in a specified output .json file. This option
          enables the out_json_file parameter. For enterprise
          geodatabases, this option requires ArcGIS Enterprise
          10.9.1 or later.ELEMENTS-The trace results will be returned as feature
          elements in a
          specified output .json file. This option enables the out_json_file
          parameter.
      selection_type {String}:
          Specifies how the selection will be applied and what to do if a
          current selection exists.NEW_SELECTION-The resulting selection will
          replace the current
          selection. This is the default.ADD_TO_SELECTION-The resulting
          selection will be added to the current
          selection if one exists. If no selection exists, this is the same as
          the new selection option.REMOVE_FROM_SELECTION-The resulting selection
          will be removed from the
          current selection. If no selection exists, this option has no
          effect.SUBSET_SELECTION-The resulting selection will be combined with
          the
          current selection. Only records that are common to both remain
          selected.SWITCH_SELECTION-The resulting selection will be switched.
          Results
          that were selected are removed from the current selection, while
          results that were not selected are added to the current selection. If
          no selection exists, this is the same as the new selection option.
      clear_all_previous_trace_results {Boolean}:
          Specifies whether content will be truncated from or appended to the
          feature classes chosen to store aggregated geometry. This parameter is
          only applicable to the aggregated geometry result
          type.CLEAR_ALL_PREVIOUS_TRACE_RESULTS-The feature classes storing
          aggregated trace geometry will be truncated. Only the output geometry
          from the current trace operation will be written. This is the
          default.DO_NOT_CLEAR_ALL_PREVIOUS_TRACE_RESULTS-The output geometry
          from the
          current trace operation will be appended to the feature classes
          storing aggregated geometry.
      trace_name {String}:
          The name of the trace operation. This value is stored in
          thefield of the output feature class to assist with identification of
          the trace results. This parameter is only applicable to the aggregated
          geometry result type. TRACENAME
      use_trace_config {Boolean}:
          Specifies whether an existing named trace configuration will be used
          to populate the parameters of the Trace
          tool.USE_TRACE_CONFIGURATION-An existing named trace configuration
          will be
          used to define the properties of the trace. All parameters except
          trace_config_name, starting_points, and barriers will be
          ignored.DO_NOT_USE_TRACE_CONFIGURATION-An exiting named trace
          configuration
          will not be used to define the properties of the trace. This is the
          default.This parameter requires Trace Network Version 2 or later.
      trace_config_name {String}:
          The name of the trace configuration that will be used to define the
          properties of the trace. This parameter is only enabled when the
          use_trace_config parameter is set to USE_TRACE_CONFIGURATION.This
          parameter requires Trace Network Version 2 or later.

     OUTPUTS:
      aggregated_points {Feature Class}:
          An output multipoint feature class containing the aggregated result
          geometry. By default, the parameter is populated with a system-
          generated feature class named Trace_Results_Aggregated_Points that
          will be stored in the project's default geodatabase. This
          feature class will be created automatically if it does
          not exist. An existing feature class can also be used to store
          aggregated geometry. If a feature class other than the default is
          used, it must be a multipoint feature class and contain a string field
          named. This parameter is only applicable to the aggregated geometry
          result type. TRACENAME
      aggregated_lines {Feature Class}:
          An output polyline feature class containing the aggregated result
          geometry. By default, the parameter is populated with a system-
          generated feature class named Trace_Results_Aggregated_Lines that will
          be stored in the project's default geodatabase. This feature
          class will be created automatically if it does
          not exist. An existing feature class can also be used to store
          aggregated geometry. If a feature class other than the default is
          used, it must be a polyline feature class and contain a string field
          named. This parameter is only applicable to the aggregated geometry
          result type. TRACENAME
      out_network_layer {Group Layer}:
          The name of the output group layer that contains feature layers with
          selection sets of features returned by the trace. The layer provides
          access to work with the output of a trace in ModelBuilder and
          Python.This parameter is only applicable to the network layers result
          type.
      out_json_file {File}:
          The name and location of the .json file that will be generated.

        """