# Generated documentation for module arcpy.ga


class KernelInterpolationWithBarriers(object):
    """
    A moving window predictor that uses the shortest distance between points so that points on either side of the line barriers are connected.
    """

    @property
    def description(self) -> str:
        return """

        KernelInterpolationWithBarriers_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {in_barrier_features}, {kernel_function}, {bandwidth}, {power}, {ridge}, {output_type})

        A moving window predictor that uses the shortest distance between
        points so that points on either side of the line barriers are
        connected.

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
      in_barrier_features {Feature Layer}:
          Absolute barrier features using non-Euclidean distances rather than
          line-of-sight distances.
      kernel_function {String}:
          The kernel function used in the simulation.EXPONENTIAL-The function
          grows or decays proportionally.GAUSSIAN-
          Bell-shaped function that falls off quickly toward
          plus/minus infinity.QUARTIC-Fourth-order polynomial
          function.EPANECHNIKOV-A discontinuous parabolic function.POLYNOMIAL5-
          Fifth-order polynomial function.CONSTANT-An indicator function.
      bandwidth {Double}:
          Used to specify the maximum distance at which data points are used for
          prediction. With increasing bandwidth, prediction bias increases and
          prediction variance decreases.
      power {Long}:
          Sets the order of the polynomial.
      ridge {Double}:
          Used for the numerical stabilization of the solution of the system of
          linear equations. It does not influence predictions in the case of
          regularly distributed data without barriers. Predictions for areas in
          which the data is located near the feature barrier or isolated by the
          barriers can be unstable and tend to require relatively large ridge
          parameter values.
      output_type {String}:
          Surface type to store the interpolation results.For more information
          about the output surface types, see What output
          surface types can the interpolation models
          generate?PREDICTION-Prediction surfaces are produced from the
          interpolated
          values.PREDICTION_STANDARD_ERROR-Standard Error surfaces are produced
          from
          the standard errors of the interpolated values.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only
          if no output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested.

        """