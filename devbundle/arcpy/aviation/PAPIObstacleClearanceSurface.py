# Generated documentation for module arcpy.aviation


class PAPIObstacleClearanceSurface(object):
    """
    Creates a Precision Approach Path Indicator (PAPI) Obstacle Clearance Surface (OCS) based on the FAA Engineering Brief (EB) 95.
    """

    @property
    def description(self) -> str:
        return """

        PAPIObstacleClearanceSurface_aviation(in_features, target, {runway_direction}, {length}, {divergence}, {slope}, {distance_from_threshold}, {start_height}, {airport_control_point_feature_class})

        Creates a Precision Approach Path Indicator (PAPI) Obstacle Clearance
        Surface (OCS) based on the FAA Engineering Brief (EB) 95.

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
          defaultLOW_RUNWAY_END_DESIGNATOR-The approach surface will be created
          at the
          low end of the runway.
      length {Double}:
          The length of the surface in miles. The default is 4.
      divergence {Double}:
          The divergence of the surface in degrees. The default is 10.
      slope {Double}:
          The slope of the surface in degrees. The default is 3.
      distance_from_threshold {Double}:
          The distance from the threshold in feet. The default is 700.
      start_height {Double}:
          The start height of the surface in feet. The default is 35.
      airport_control_point_feature_class {Feature Layer}:
          Supplies x-, y-, and z-geometry for displaced threshold features. If
          displaced thresholds are included, surfaces will be constructed based
          on their x-, y-, and z-geometry instead of their corresponding runway
          feature endpoint.

        """