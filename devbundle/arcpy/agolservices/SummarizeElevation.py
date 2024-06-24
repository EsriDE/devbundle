# Generated documentation for module arcpy.agolservices


class SummarizeElevation(object):
    """
    Calculates summary statistics of elevation for each input feature.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeElevation_agolservices(InputFeatures, {FeatureIDField}, {DEMResolution}, {IncludeSlopeAspect})

        Calculates summary statistics of elevation for each input feature.

     INPUTS:
      InputFeatures (Feature Set):
          The input point, line, or area features for which the elevation will
          be summarized.
      FeatureIDField {String}:
          The unique ID field to use for the input features.
      DEMResolution {String}:
          Specifies the approximate spatial resolution (cell size) of the source
          elevation data used for the calculation.The resolution keyword is an
          approximation of the spatial resolution
          of the digital elevation model. Many elevation sources are distributed
          in units of arc seconds; the keyword is an approximation in meters for
          easier understanding.FINEST-The finest units available for the extent
          are used.10m-The
          elevation source resolution is 1/3 arc second or approximately
          10 meters.24m-The elevation source is the Airbus WorldDEM4Ortho
          dataset at 24
          meters resolution.30m-The elevation source resolution is 1 arc second
          or approximately
          30 meters.90m-The elevation source resolution is 3 arc seconds or
          approximately
          90 meters. This is the default.
      IncludeSlopeAspect {Boolean}:
          Specifies whether slope and aspect values for the input features will
          be included in the output in addition to the elevation
          values.SLOPE_ASPECT-Slope and aspect values will be included in the
          output.NO_SLOPE_ASPECT-Slope and aspect values will not be included in
          the
          output. This is the default.

        """