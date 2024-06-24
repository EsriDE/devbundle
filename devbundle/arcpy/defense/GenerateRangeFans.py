# Generated documentation for module arcpy.defense


class GenerateRangeFans(object):
    """
    Creates range fans originating from a starting point given a horizontal start angle, horizontal end angle, minimum distance, and maximum distance.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRangeFans_defense(in_features, out_range_fan_feature_class, inner_radius, outer_radius, horizontal_start_angle, horizontal_end_angle, {distance_units}, {angle_units})

        Creates range fans originating from a starting point given a
        horizontal start angle, horizontal end angle, minimum distance, and
        maximum distance.

     INPUTS:
      in_features (Feature Set):
          The input point feature set that identifies the origin points of the
          range fans. The input must have at least one point.
      inner_radius (Double):
          The distance from the origin point to the start of the range fan.
      outer_radius (Double):
          The distance from the origin point to the end of the range fan.
      horizontal_start_angle (Double):
          The angle from the origin point to the start of the range fan.
      horizontal_end_angle (Double):
          The angle from the origin point to the end of the range fan.
      distance_units {String}:
          Specifies the linear unit of measurement for minimum and maximum
          distance.METERS-The unit will be meters. This is the
          default.KILOMETERS-The
          unit will be kilometers.MILES-The unit will be
          miles.NAUTICAL_MILES-The unit will be nautical miles.FEET-The unit
          will be feet.US_SURVEY_FEET-The unit will be U.S. survey feet.
      angle_units {String}:
          Specifies the angular unit of measurement for start and end
          angles.DEGREES-The angle will be degrees. This is the default.MILS-The
          angle
          will be mils.RADS-The angle will be radians.GRADS-The angle will be
          gradians.

     OUTPUTS:
      out_range_fan_feature_class (Feature Class):
          The feature class that will contain the output range fan features.

        """