# Generated documentation for module arcpy.ga


class GlobalPolynomialInterpolation(object):
    """
    Fits a smooth surface that is defined by a mathematical function (a polynomial) to the input sample points.
    """

    @property
    def description(self) -> str:
        return """

        GlobalPolynomialInterpolation_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {power}, {weight_field})

        Fits a smooth surface that is defined by a mathematical function (a
        polynomial) to the input sample points.

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
      power {Long}:
          The order of the polynomial.
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