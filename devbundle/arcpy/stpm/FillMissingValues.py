# Generated documentation for module arcpy.stpm


class FillMissingValues(object):
    """
    Replaces missing (null) values with estimated values based on spatial neighbors, space-time neighbors, time-series, or global statistic values.
    """

    @property
    def description(self) -> str:
        return """

        FillMissingValues_stpm(in_features, {out_features}, fields_to_fill;fields_to_fill..., fill_method, {conceptualization_of_spatial_relationships}, {distance_band}, {temporal_neighborhood}, {time_field}, {number_of_spatial_neighbors}, {location_id}, {related_table}, {related_location_id}, {weights_matrix_file}, {unique_id}, {null_value}, {out_table}, {append_to_input})

        Replaces missing (null) values with estimated values based on spatial
        neighbors, space-time neighbors, time-series, or global statistic
        values.

     INPUTS:
      in_features (Table View):
          The point or polygon feature class or stand-alone table containing the
          null values to be filled.If the related_table parameter value is
          provided, the null values to
          be filled will be contained in the related table. The input features
          will be matched to the rows in the related table to specify the space-
          time neighborhood.
      fields_to_fill (Field):
          The numeric fields containing missing data (null values).
      fill_method (String):
          Specifies the type of calculation that will be applied. The
          TEMPORAL_TREND option is only available if the location_id and
          time_field parameter values are provided.AVERAGE-Null values will be
          replaced with the average (mean) value of
          the feature's neighbors.MINIMUM-Null values will be replaced with the
          minimum (smallest) value
          of the feature's neighbors.MAXIMUM-Null values will be replaced with
          the maximum (largest) value
          of the feature's neighbors.MEDIAN-Null values will be replaced with
          the median (sorted middle
          value) of the feature's neighbors.TEMPORAL_TREND-Null values will be
          replaced based on the trend at that
          unique location.
      conceptualization_of_spatial_relationships {String}:
          Specifies how spatial relationships among features will be
          defined.FIXED_DISTANCE-Neighboring features within a specified
          critical
          distance (the distance_band parameter value) of each feature will be
          included in the calculations; everything outside the critical distance
          will be excluded.K_NEAREST_NEIGHBORS-The closest k features will be
          included in the
          calculations; k is a specified numeric
          parameter.CONTIGUITY_EDGES_ONLY-Only neighboring polygon features
          that share a
          boundary or overlap will influence computations for the target polygon
          feature.CONTIGUITY_EDGES_CORNERS-Polygon features that share a
          boundary,
          share a node, or overlap will influence computations for the target
          polygon feature.GET_SPATIAL_WEIGHTS_FROM_FILE-Spatial relationships
          will be defined by
          a specified spatial weights file. The path to the spatial weights file
          is specified by the Weights_Matrix_File parameter.
      distance_band {Linear Unit}:
          The cutoff distance for the conceptualization_of_spatial_relationships
          parameter's FIXED_DISTANCE option. Features outside the specified
          cutoff for a target feature will be ignored in calculations for that
          feature. This parameter is not available for the CONTIGUITY_EDGES_ONLY
          or CONTIGUITY_EDGES_CORNERS options.
      temporal_neighborhood {Time Unit}:
          An interval forward and backward in time that determines the features
          that will be used in calculations for the target feature. Features
          that are not within this interval of the target feature will be
          ignored in calculations for that feature.
      time_field {Field}:
          The field containing the time stamp for each record in the dataset.
          This field must be of type Date.For feature input, the time field will
          define temporal neighbors while
          filling missing values. A value must be provided if a related table is
          provided.For feature and table input, the time field will be used when
          filling
          missing values using temporal trend at the location.
      number_of_spatial_neighbors {Long}:
          The number of nearest neighbors that will be included in
          calculations.If the conceptualization_of_spatial_relationships
          parameter's
          FIXED_DISTANCE, CONTIGUITY_EDGES_ONLY, or CONTIGUITY_EDGES_CORNERS
          option is chosen, this number is the minimum number of neighbors to
          include in calculations.
      location_id {Field}:
          An integer or text field containing a unique ID for each location.If a
          related table is provided, this field is used to match each input
          feature to rows in the related table; the values of this field must be
          unique for every input feature. If a related table is not provided,
          this field is used to specify each unique location in the input
          features to determine temporal neighbors. In this case, the values of
          this field must be unique to every location but do not need to be
          unique for each feature (because more than one feature can have the
          same location).
      related_table {Table View}:
          The table or table view containing the temporal data for each feature
          of the in_features parameter.
      related_location_id {Field}:
          An integer or text field in the related_table parameter that contains
          the location_id parameter value on which the relate will be based.
      weights_matrix_file {File}:
          The path to a file containing weights that define spatial, and
          potentially temporal, relationships among features.
      unique_id {Field}:
          An integer field containing a different value for every record in the
          in_features parameter value. This field can be used to join the
          results back to the original dataset. If you don't have afield,
          you can create one by adding an
          integer field to the feature class table and calculating the field
          values equal to theorfield. unique_idFIDOBJECTID
      null_value {Double}:
          The value that represents null (missing) values. If no value is
          provided, <Null> is assumed for geodatabase feature classes and
          tables. If a value is provided, both the value and all <Null> values
          will be filled. If the input or output is a shapefile or dBASE table,
          a numeric value of the null placeholder is required.
      append_to_input {Boolean}:
          Specifies whether the filled value fields will be appended to the
          input data or an output feature class or table will be created with
          the filled value fields. If you append the fields, you cannot provide
          a related table and the output coordinate system environment will be
          ignored.APPEND_TO_INPUT-The fields containing the filled values will
          be
          appended to the input data. This option modifies the input
          data.NEW_FEATURES-An output feature class or table will be created
          containing the filled value fields. This is the default.

     OUTPUTS:
      out_features {Feature Class / Table}:
          The output features or stand-alone table that will include the filled
          (estimated) values.If the related_table parameter value is provided,
          the output of this
          parameter will contain the number of estimated values at each
          location, and the out_table parameter value will contain the filled
          (estimated) values.
      out_table {Table}:
          The output table containing the filled (estimated) values.The output
          table is required if a related table is provided.

        """