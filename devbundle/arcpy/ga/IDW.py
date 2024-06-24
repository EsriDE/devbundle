# Generated documentation for module arcpy.ga


class IDW(object):
    """
    Uses the measured values surrounding the prediction location to predict a value for any unsampled location, based on the assumption that things that are close to one another are more alike than those that are farther apart.
    """

    @property
    def description(self) -> str:
        return """

        IDW_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {power}, {search_neighborhood}, {weight_field})

        Uses the measured values surrounding the prediction location to
        predict a value for any unsampled location, based on the assumption
        that things that are close to one another are more alike than those
        that are farther apart.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can
          be a numeric field or the Shape field if the input features contain
          z-values or m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created. This
          value can be explicitly set in theby theparameter.
          EnvironmentsCell SizeIf not set, it is the shorter of the width or the
          height of the extent
          of the input point features, in the input spatial reference, divided
          by 250.
      power {Double}:
          The exponent of distance that controls the significance of surrounding
          points on the interpolated value. A higher power results in less
          influence from distant points.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Defines which surrounding points will be used to control the output.
          Standard is the default.The following are Search Neighborhood classes:
          SearchNeighborhoodStandard, SearchNeighborhoodSmooth,
          SearchNeighborhoodStandardCircular, and
          SearchNeighborhoodSmoothCircular.StandardmajorSemiaxis-The major
          semiaxis value of the searching
          neighborhood.minorSemiaxis-The minor semiaxis value of the searching
          neighborhood.angle-The angle of rotation for the axis (circle) or
          semimajor axis
          (ellipse) of the moving window.nbrMax-The maximum number of neighbors
          that will be used to estimate
          the value at the unknown location.nbrMin-The minimum number of
          neighbors that will be used to estimate
          the value at the unknown location. sectorType-The geometry of
          the neighborhood.
          ONE_SECTOR-Single ellipse.FOUR_SECTORS-Ellipse divided into four
          sectors.FOUR_SECTORS_SHIFTED-Ellipse divided into four sectors and
          shifted 45
          degrees.EIGHT_SECTORS-Ellipse divided into eight
          sectors.SmoothmajorSemiaxis-The major semiaxis value of the searching
          neighborhood.minorSemiaxis-The minor semiaxis value of the searching
          neighborhood.angle-The angle of rotation for the axis (circle) or
          semimajor axis
          (ellipse) of the moving window.smoothFactor-The Smooth Interpolation
          option creates an outer ellipse
          and an inner ellipse at a distance equal to the Major Semiaxis
          multiplied by the Smoothing factor. The points that fall outside the
          smallest ellipse but inside the largest ellipse are weighted using a
          sigmoidal function with a value between zero and one.Standard
          Circularradius-The length of the radius of the search circle.angle-The
          angle
          of rotation for the axis (circle) or semimajor axis
          (ellipse) of the moving window.nbrMax-The maximum number of neighbors
          that will be used to estimate
          the value at the unknown location.nbrMin-The minimum number of
          neighbors that will be used to estimate
          the value at the unknown location. sectorType-The geometry of
          the neighborhood.
          ONE_SECTOR-Single ellipse.FOUR_SECTORS-Ellipse divided into four
          sectors.FOUR_SECTORS_SHIFTED-Ellipse divided into four sectors and
          shifted 45
          degrees.EIGHT_SECTORS-Ellipse divided into eight sectors.Smooth
          Circularradius-The length of the radius of the search
          circle.smoothFactor-The
          Smooth Interpolation option creates an outer ellipse
          and an inner ellipse at a distance equal to the Major Semiaxis
          multiplied by the Smoothing factor. The points that fall outside the
          smallest ellipse but inside the largest ellipse are weighted using a
          sigmoidal function with a value between zero and one.
      weight_field {Field}:
          Used to emphasize an observation. The larger the weight, the more
          impact it has on the prediction. For coincident observations, assign
          the largest weight to the most reliable measurement.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only
          if no output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested.

        """