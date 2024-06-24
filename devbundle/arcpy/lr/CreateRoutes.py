# Generated documentation for module arcpy.lr


class CreateRoutes(object):
    """
    Creates routes from existing lines. The input line features that share a common identifier are merged to create a single route.
    """

    @property
    def description(self) -> str:
        return """

        CreateRoutes_lr(in_line_features, route_id_field, out_feature_class, measure_source, {from_measure_field}, {to_measure_field}, {coordinate_priority}, {measure_factor}, {measure_offset}, {ignore_gaps}, {build_index})

        Creates routes from existing lines. The input line features that share
        a common identifier are merged to create a single route.

     INPUTS:
      in_line_features (Feature Layer):
          The features from which routes will be created.
      route_id_field (Field):
          The field containing values that uniquely identify each route. The
          field can be a numeric, text, or GUID field.
      measure_source (String):
          Specifies how route measures will be accumulated.LENGTH-The geometric
          length of the input features will be used to
          accumulate the measures. This is the default.ONE_FIELD-The value
          stored in a single field will be used to
          accumulate the measures.TWO_FIELDS-The values stored in both the from-
          and to-measure fields
          will be used to accumulate the measures.
      from_measure_field {Field}:
          A field containing measure values. This field must be numeric and is
          required when the measure source is ONE_FIELD or TWO_FIELDS.
      to_measure_field {Field}:
          A field containing measure values. This field must be numeric and is
          required when the measure source is TWO_FIELDS.
      coordinate_priority {String}:
          The position from which measures will be accumulated for each output
          route. This parameter is ignored when the measure source is
          TWO_FIELDS.UPPER_LEFT-Measures will be accumulated from the point
          closest to the
          minimum bounding rectangle's upper left corner. This is the
          default.LOWER_LEFT-Measures will be accumulated from the point closest
          to the
          minimum bounding rectangle's lower left corner.UPPER_RIGHT-Measures
          will be accumulated from the point closest to the
          minimum bounding rectangle's upper right corner.LOWER_RIGHT-Measures
          will be accumulated from the point closest to the
          minimum bounding rectangle's lower right corner.
      measure_factor {Double}:
          A value multiplied by the measure length of each input line before
          they are merged to create route measures. The default is 1.
      measure_offset {Double}:
          A value added to the route measures after the input lines have been
          merged to create a route. The default is 0.
      ignore_gaps {Boolean}:
          Specifies whether spatial gaps will be ignored when calculating the
          measures on disjointed routes. This parameter is applicable when the
          measure source is LENGTH or ONE_FIELD.IGNORE-Spatial gaps will be
          ignored. Measure values will be continuous
          for disjointed routes. This is the default.NO_IGNORE-Spatial gaps will
          not be ignored. The measure values on
          disjointed routes will have gaps. The gap distance is calculated using
          the straight-line distance between the endpoints of the disjointed
          parts.
      build_index {Boolean}:
          Specifies whether an attribute index will be created for the route
          identifier field that is written to the output route feature
          class.INDEX-An attribute index will be created. This is the
          default.NO_INDEX-An attribute index will not be created.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will be created. It can be a shapefile or a
          geodatabase feature class.

        """