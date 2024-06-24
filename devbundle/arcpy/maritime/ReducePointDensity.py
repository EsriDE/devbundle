# Generated documentation for module arcpy.maritime


class ReducePointDensity(object):
    """
    Thins points from a point or multipoint feature class.
    """

    @property
    def description(self) -> str:
        return """

        ReducePointDensity_maritime(in_features, out_feature_class, depth_field, depth_direction, depth_bias, radius_unit, start_thinning_radius, {end_thinning_radius}, {start_depth}, {end_depth})

        Thins points from a point or multipoint feature class.

     INPUTS:
      in_features (Feature Layer):
          The input point or multipoint features.
      depth_field (Field):
          The field where the depth is stored. It is either a numeric
          field or the shape field specified in in_features. For
          multipoint features, this must be the shape field.
      depth_direction (String):
          Specifies how the depth value will be captured in the depth field of
          the input features.POSITIVE_UP-Depth values will be positive above the
          surface and
          negative below the surface. This is default.POSITIVE_DOWN-Depth values
          will be positive below the surface and
          negative above the surface.
      depth_bias (String):
          Specifies the bias that will be used to select the depths to be
          retained.SHALLOW_BIASED-Shallow bias will be used for depth. This is
          default.DEEP_BIASED-Deep bias will be used for depth.
      radius_unit (String):
          Specifies the unit of measure that will be used by the
          start_thinning_radius and end_thinning_radius
          parameters.KILOMETERS-The radius unit will be kilometers.METERS-The
          radius unit
          will be meters. This is default.DECIMETERS-The radius unit will be
          decimeters.CENTIMETERS-The radius unit will be
          centimeters.MILLIMETERS-The radius unit will be
          millimeters.NAUTICAL_MILES-The radius unit will be nautical
          miles.MILES-The radius unit will be miles.YARDS-The radius unit will
          be yards.FEET-The radius unit will be feet.INCHES-The radius unit will
          be inches.DECIMAL_DEGREES-The radius unit will be decimal
          degrees.POINTS-The radius unit will be points.
      start_thinning_radius (Double):
          The beginning radius that will be used to remove or thin points
          relative to each other.
      end_thinning_radius {Double}:
          The end radius that will be used to remove or thin points relative to
          each other. The thinning radius will dynamically change as the
          algorithm progresses through the range of depth values.
      start_depth {Double}:
          The depth that will be used to begin the thinning algorithm. Depth
          values that appear before this depth based on the depth_direction
          parameter value will be ignored.
      end_depth {Double}:
          The depth that will be used to end the thinning algorithm. Depth
          values that appear after this depth based on the depth_direction
          parameter value will be ignored.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class.

        """