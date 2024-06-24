# Generated documentation for module arcpy.aviation


class LightSignalClearanceSurface(object):
    """
    Creates a Light Signal Clearance Surface (LSCS) based on the FAA Engineering Brief (EB) 95.
    """

    @property
    def description(self) -> str:
        return """

        LightSignalClearanceSurface_aviation(in_features, target, {runway_direction}, {length}, {divergence}, {slope}, {distance_from_threshold}, {first_papi_light}, {last_papi_light}, {start_height}, {airport_control_point_feature_class}, {surface_position})

        Creates a Light Signal Clearance Surface (LSCS) based on the FAA
        Engineering Brief (EB) 95.

     INPUTS:
      in_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target (Feature Layer):
          The target feature class that will contain the generated OIS.
      runway_direction {String}:
          Specifies the end of the runway where the approach surface will be
          created.HIGH_RUNWAY_END_DESIGNATOR-The approach surface will be
          created at
          the high end of the runway. This is the
          default.LOW_RUNWAY_END_DESIGNATOR-The approach surface will be created
          at the
          low end of the runway.
      length {Double}:
          The length of the surface in miles. The default value is 8.
      divergence {Double}:
          The divergence of the surface in degrees. The default value is 14.
      slope {Double}:
          The slope of the surface in degrees. The default value is 1.
      distance_from_threshold {Double}:
          The distance from the threshold in feet. The default value is 1000.
      first_papi_light {Double}:
          The location of the first precision approach path indicator. The
          default value is 60.
      last_papi_light {Double}:
          The location of the last precision approach path indicator. The
          default value is 120.
      start_height {Double}:
          The start height of the surface. The default value is 35.
      airport_control_point_feature_class {Feature Layer}:
          Supplies x-, y-, and z-geometry for displaced threshold features. If
          displaced thresholds are included, surfaces will be constructed based
          on their x-, y-, and z-geometry instead of their corresponding runway
          feature endpoint.
      surface_position {String}:
          Specifies the position of the precision approach path indicator (PAPI)
          lights on either side of a runway. The position of the PAPI lights
          will be used to determine the position of the output
          surface.SURFACE_GENERATED_ON_LEFT-PAPI lights are on the left approach
          side of
          the runway. The surface will generate on the left approach side of the
          runway. This is the default.SURFACE_GENERATED_ON_RIGHT-PAPI lights are
          on the right approach side
          of the runway. The surface will generate on the right approach side of
          the runway.

        """