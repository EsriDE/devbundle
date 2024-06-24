# Generated documentation for module arcpy.defense


class GenerateRangeRings(object):
    """
    Creates a set of concentric circles from a point, given a number of rings and distance between rings or a minimum and maximum distance from center.
    """

    @property
    def description(self) -> str:
        return """

        GenerateRangeRings_defense(in_features, out_feature_class_rings, range_rings_type, {out_feature_class_radials}, {number_of_radials}, {distance_units}, {number_of_rings}, {interval_between_rings}, {minimum_range}, {maximum_range})

        Creates a set of concentric circles from a point, given a number of
        rings and distance between rings or a minimum and maximum distance
        from center.

     INPUTS:
      in_features (Feature Set):
          The point feature set that identifies the center of the range ring.
          The input must have at least one point.
      range_rings_type (String):
          Specifies the method to create the range rings.INTERVAL-Range rings
          will be generated based on the number of rings
          and distance between rings. This the default.MIN_MAX-Range rings will
          be generated based on a minimum and maximum
          distance.
      number_of_radials {Long}:
          The number of radials to generate.
      distance_units {String}:
          Specifies the linear unit of measurement for the
          interval_between_rings parameter or the minimum_range and
          maximum_range parameters.METERS-The unit will be meters. This is the
          default.KILOMETERS-The
          unit will be kilometers.MILES-The unit will be
          miles.NAUTICAL_MILES-The unit will be nautical miles.FEET-The unit
          will be feet.US_SURVEY_FEET-The unit will be U.S. survey feet.
      number_of_rings {Long}:
          The number of rings to generate.
      interval_between_rings {Double}:
          The distance between each ring.
      minimum_range {Double}:
          The distance from the center to the nearest ring.
      maximum_range {Double}:
          The distance from the center to the farthest ring.

     OUTPUTS:
      out_feature_class_rings (Feature Class):
          The feature class containing the output ring features.
      out_feature_class_radials {Feature Class}:
          The feature class containing the output radial features.

        """