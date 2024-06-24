# Generated documentation for module arcpy.management


class MakeAggregationQueryLayer(object):
    """
    Creates a query layer that summarizes, aggregates, and filters DBMS tables dynamically based on time, range, and attribute queries from a related table, and joins the result to a feature layer.
    """

    @property
    def description(self) -> str:
        return """

        MakeAggregationQueryLayer_management(target_feature_class, target_join_field, related_table, related_join_field, out_layer, {statistics;statistics...}, {parameter_definitions;parameter_definitions...}, {oid_fields;oid_fields...}, {shape_type}, {srid}, {spatial_reference}, {m_values}, {z_values}, {extent})

        Creates a query layer that summarizes, aggregates, and filters DBMS
        tables dynamically based on time, range, and attribute queries from a
        related table, and joins the result to a feature layer.

     INPUTS:
      target_feature_class (Feature Class):
          The feature class or spatial table from an enterprise database.
      target_join_field (Field):
          The field in the target feature class on which the join will be based.
      related_table (Table / Feature Class):
          The input table containing the fields that will be used to calculate
          statistics. Statistics are joined to the out_layer value.
      related_join_field (Field):
          A field in the summary table that contains the values on which the
          join will be based. Aggregation or summary statistics are also
          calculated separately for each unique attribute value from this field.
      statistics {Value Table}:
          Specifies the numeric field or fields containing the attribute values
          that will be used to calculate the specified statistic. Multiple
          statistic and field combinations can be specified. Null values are
          excluded from all statistical calculations. The output layer
          will include afield showing total count (or
          frequency) of each unique value from the related_join_field value. The
          difference between thefield and the COUNT statistic type is
          thatincludes null values while COUNT excludes null values.
          ROW_COUNTROW_COUNTROW_COUNTCOUNT-The number of values included in the
          statistical calculations
          will be found. Each value will be counted except null values.SUM-The
          values for the specified field will be added together.AVG-The average
          for the specified field will be calculated.MIN-The smallest value for
          all records of the specified field will be
          found.MAX-The largest value for all records of the specified field
          will be
          found.STDDEV-The standard deviation of values in the specified field
          will be
          calculated.
      parameter_definitions {Value Table}:
          Specifies one or more query parameters for criteria or conditions;
          records matching these criteria are used while computing aggregated
          results. A query parameter is similar to an SQL statement variable for
          which the value is defined when the query is run. This allows you to
          dynamically change query filters for the output layer. You can think
          of a parameter as a predicate or condition in a SQL where clause. For
          example Country_Name = 'Nigeria' in a SQL where clause is called a
          predicate in which the = is a comparison operator, Country_Name is a
          field name on the left, and 'Nigeria' is a value on the right. When
          you define more than one parameter, you must specify a logical
          operator between them (such as AND, OR, and so on).When not specified,
          all records from the related table will be used in
          computing aggregated or summary results. The two parameter
          definition types are the following:
          Range-Connect numeric or temporal values dynamically to the range and
          time sliders.Discrete-Update a query with literal values when the
          query is run.The following properties are available:Parameter Type-The
          parameter type can be RANGE or DISCRETE.Name-The
          name of the parameter, which is similar to a variable name. A
          name cannot contain spaces or special characters. Once the output
          query layer is created and the layer source SQL statement is checked,
          this name in the SQL statement that defines the output query layer
          source,will be prefixed with either::r: (for range parameter) or ::
          (for discrete parameter).Alias-The alias for the parameter name. The
          alias can include spaces
          and special characters.Field or Expression-A field name or a valid SQL
          expression that will
          be used in the left side of a predicate or condition in a where
          clause. Data type-The data type of the field or expression
          specified
          in the Field or Expression column. When the Parameter Type value is
          RANGE, the Data type column value cannot be STRING. DATE-The
          data type of the field or expression will be Date (date
          time).STRING-The data type of the field or expression will be String
          (text).INTEGER-The data type of the field or expression will be
          Integer
          (whole numbers).DOUBLE-The data type of the field or expression will
          be Double
          (fractional numbers).Start Value-The default start value for the RANGE
          column. This is the
          value that will be used when the time or range slider is not enabled.
          When the Start Value and End Value column values are omitted and the
          time or range slider is disabled, all records from the related table
          will be used to compute aggregated results. This value is ignored when
          the Parameter Type column is set to DISCRETE.End Value-The default end
          value for the RANGE parameter. This is the
          value that will be used when the time or range slider is not enabled.
          When the Start Value and End Value column values are omitted and the
          time or range slider is disabled, all records from the related table
          will be used to compute aggregated results. This value is ignored when
          the Parameter Type column is set to DISCRETE. Operator for
          Discrete Parameter-The comparison operator that
          will be used between the Field or Expression column value and a value
          in an SQL predicate or condition. NONE-Choose NONE when
          Parameter Type is set to RANGE.EQUAL TO-Compare
          the equality of a field or expression to a value.NOT EQUAL TO-Test
          whether a field or expression is not equal to a
          value.GREATER THAN-Test whether a field or expression is higher than a
          value.LESS THAN-Test whether a field or expression is lower than a
          value.INCLUDE VALUES-Determine whether a value from a field or
          expression
          matches any value in a list.Default Discrete Values-When the Parameter
          Type value is DISCRETE, you
          must provide a default value. When Operator for Discrete Parameter is
          INCLUDE VALUES, you can provide multiple values separated by commas,
          for example VANDALISM,BURGLARY/THEFT. Operator for Next
          Parameter-The logical operator between this
          operator and the next one. This column is only applicable when you
          have more than one parameter definition. NONE-Choose NONE when
          there are no more parameters.AND-Combine two
          conditions and select a record if both conditions are
          true.OR-Combine two conditions and select a record if at least one
          condition is true.
      oid_fields {String}:
          The unique identifier fields that will be used to uniquely identify
          each row in the table.
      shape_type {String}:
          Specifies the shape type of the query layer. Only those records from
          the result set of the query that match the specified shape type will
          be used in the output query layer. By default, the shape type of the
          first record in the result set will be used. This parameter is ignored
          if the result set of the query does not return a geometry
          field.POINT-The output query layer will use point
          geometry.MULTIPOINT-The
          output query layer will use multipoint geometry.POLYGON-The output
          query layer will use polygon geometry.POLYLINE-The output query layer
          will use polyline geometry.
      srid {String}:
          The spatial reference identifier (SRID) value for queries that return
          geometry. Only those records from the result set of the query that
          match the specified SRID value will be used in the output query layer.
          By default, the SRID value of the first record in the result set will
          be used. This parameter is ignored if the result set of the query does
          not return a geometry field.
      spatial_reference {Spatial Reference}:
          The coordinate system that will be used by the output query layer. By
          default, the spatial reference of the first record in the result set
          will be used. This parameter is ignored if the result set of the query
          does not return a geometry field.
      m_values {Boolean}:
          Specifies whether the output layer will include linear measurements
          (m-values).INCLUDE_M_VALUES-The layer will include
          m-values.DO_NOT_INCLUDE_M_VALUES-The layer will not include m-values.
          This is
          the default.
      z_values {Boolean}:
          Specifies whether the output layer will include elevation values
          (z-values).INCLUDE_Z_VALUES-The layer will include
          z-values.DO_NOT_INCLUDE_Z_VALUES-The layer will not include z-values.
          This is
          the default.
      extent {Extent}:
          Specifies the extent of the layer. The extent must include all
          features in the table.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

     OUTPUTS:
      out_layer (Feature Layer):
          The output name of the query layer that will be created.

        """