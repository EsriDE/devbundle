# Generated documentation for module arcpy.defense


class GenerateRangeFansFromFeatures(object):
    """
    Creates range fans with attributes derived from fields in a point feature class or shapefile.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRangeFansFromFeatures_defense(in_features, output_feature_class, inner_radius_field, outer_radius_field, start_angle_field, end_angle_field, {distance_units}, {angle_units})

        Creates range fans with attributes derived from fields in a point
        feature class or shapefile.

     INPUTS:
      in_features (Feature Layer):
          The point feature set that identifies the origin points of the range
          fans. The input must have at least one point.
      inner_radius_field (Field):
          The field that contains the values for the distance from the origin
          point to the start of the range fan.
      outer_radius_field (Field):
          The field that contains the values for the distance from the origin
          point to the end of the range fan.
      start_angle_field (Field):
          The field that contains the values for the angle from the origin point
          to the start of the range fan.
      end_angle_field (Field):
          The field that contains the values for the angle from the origin point
          to the end of the range fan.
      distance_units {String}:
          Specifies the linear unit of measure for minimum and maximum
          distance.METERS-The unit will be meters. This is the
          default.KILOMETERS-The
          unit will be kilometers.MILES-The unit will be
          miles.NAUTICAL_MILES-The unit will be nautical miles.FEET-The unit
          will be feet.US_SURVEY_FEET-The unit will be U.S. survey feet.
      angle_units {String}:
          Specifies the angular unit of measure for start and end
          angles.DEGREES-The angle will be degrees. This is the default.MILS-The
          angle
          will be mils.RADS-The angle will be radians.GRADS-The angle will be
          gradians.

     OUTPUTS:
      output_feature_class (Feature Class):
          The feature class that will contain the output range fan features.

        """