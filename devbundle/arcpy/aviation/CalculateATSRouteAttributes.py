# Generated documentation for module arcpy.aviation


class CalculateATSRouteAttributes(object):
    """
    Calculates segment distance and bearing attributes on Air Traffic Service (ATS) route features.
    """

    @property
    def description(self) -> str:
        return """

        CalculateATSRouteAttributes_aviation(in_features, atsroute_attributes;atsroute_attributes..., {magnetic_variation_date})

        Calculates segment distance and bearing attributes on Air Traffic
        Service (ATS) route features.

     INPUTS:
      in_features (Feature Layer):
          The polyline features for which ATS route attributes will be
          calculated.
      atsroute_attributes (Value Table):
          Specifies the ATS route attributes that will be calculated.LENGTH-The
          length of the route segment in nautical miles will be
          calculated.TRUE_TRACK-The True North azimuth of the route segment's
          track from
          its start point will be calculated.REVERSE_TRUE_TRACK-The True North
          azimuth of the route segment's
          reverse track from its end point will be calculated.MAG_TRACK-The
          Magnetic North azimuth of the route segment's track from
          its start point will be calculated.REVERSE_MAG_TRACK-The Magnetic
          North azimuth of the route segment's
          reverse track from its end point will be calculated.
      magnetic_variation_date {Date}:
          The date for which the magnetic field values will be calculated.

        """