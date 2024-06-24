# Generated documentation for module arcpy.defense


class GenerateRangeRingsFromFeatures(object):
    """
    Creates range rings with attributes derived from fields in a point feature class.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRangeRingsFromFeatures_defense(in_features, output_feature_class, range_rings_type, {out_feature_class_radials}, {radial_count_field}, {min_range_field}, {max_range_field}, {ring_count_field}, {ring_interval_field}, {distance_units})

        Creates range rings with attributes derived from fields in a point
        feature class.

     INPUTS:
      in_features (Feature Layer):
          The point feature set that identifies the center of the range ring.
          The input must have at least one point.
      range_rings_type (String):
          Specifies how range rings will be generated.INTERVAL-Range rings will
          be generated based on the number of rings
          and distance between rings. This the default.MIN_MAX-Range rings will
          be generated based on a minimum and maximum
          distance.
      radial_count_field {Field}:
          The field that contains the number of radials to be created.
      min_range_field {Field}:
          The field that contains the values for the distance from the origin
          point to the inner ring.
      max_range_field {Field}:
          The field that contains the values for the distance from the origin
          point to the outer ring.
      ring_count_field {Field}:
          The field that contains the values for the number of rings to
          generate.
      ring_interval_field {Field}:
          The field that contains the values for the interval between rings.
      distance_units {String}:
          Specifies the linear unit of measure for the value of the
          ring_interval_field parameter or the values of the min_range_field and
          max_range_field parameters.METERS-The unit will be meters. This is the
          default.KILOMETERS-The
          unit will be kilometers.MILES-The unit will be
          miles.NAUTICAL_MILES-The unit will be nautical miles.FEET-The unit
          will be feet.US_SURVEY_FEET-The unit will be U.S. survey feet.

     OUTPUTS:
      output_feature_class (Feature Class):
          The feature class that will contain the output ring features.
      out_feature_class_radials {Feature Class}:
          The feature class that will contain the output radial features.

        """