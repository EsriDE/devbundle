# Generated documentation for module arcpy.intelligence


class GenerateBlindSpotAreas(object):
    """
    Creates an output nonvisible area, or blind spot, for input Intelligence, Surveillance, Reconnaissance (ISR) or patrol visible buffer features based on start and end times. The output blind spot layer is used with the time slider to visualize and explore areas that are not visible to ISR or patrol assets at specified times. For example, the output can show areas that a guard is not able to observe for given input time periods at posts along a patrol route.
    """

    @property
    def description(self) -> str:
        return """

        GenerateBlindSpotAreas_intelligence(in_features, out_feature_class, {clip_features}, {start_time_field}, {end_time_field})

        Creates an output nonvisible area, or blind spot, for input
        Intelligence, Surveillance, Reconnaissance (ISR) or patrol visible
        buffer features based on start and end times. The output blind spot
        layer is used with the time slider to visualize and explore areas that
        are not visible to ISR or patrol assets at specified times. For
        example, the output can show areas that a guard is not able to observe
        for given input time periods at posts along a patrol route.

     INPUTS:
      in_features (Feature Layer):
          The input visible buffer features.
      clip_features {Feature Set}:
          The features used to define the input boundary.
      start_time_field {Field}:
          The field containing the start date and time when the asset is
          available.
      end_time_field {Field}:
          The field containing the end date and time when the asset is no longer
          available.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output blind spot area features.

        """