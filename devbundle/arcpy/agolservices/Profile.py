# Generated documentation for module arcpy.agolservices


class Profile(object):
    """
    Returns elevation profiles for the input line features.
    """

    @property
    def description(self) -> str:
        return """

        Profile_agolservices(InputLineFeatures, {ProfileIDField}, {DEMResolution}, {MaximumSampleDistance}, {MaximumSampleDistanceUnits})

        Returns elevation profiles for the input line features.

     INPUTS:
      InputLineFeatures (Feature Set):
          The line features that will be profiled over the surface inputs.
      ProfileIDField {String}:
          A unique identifier to associate profiles with their corresponding
          input line features.
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
          90 meters. This is the default.500m-The elevation source resolution is
          15 arc seconds or
          approximately 500 meters.1000m-The elevation source resolution is 30
          arc seconds or
          approximately 1000 meters.
      MaximumSampleDistance {Double}:
          The maximum sample distance along the line used to sample elevation
          values.
      MaximumSampleDistanceUnits {String}:
          Specifies the units for theparameter. Maximum Sample
          DistanceMeters-The units are meters. This is the
          default.Kilometers-The units
          are kilometers.Feet-The units are feet.Yards-The units are
          yards.Miles-The units are miles.

        """