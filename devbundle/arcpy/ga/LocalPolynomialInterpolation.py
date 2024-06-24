# Generated documentation for module arcpy.ga


class LocalPolynomialInterpolation(object):
    """
    Fits the specified order (zero, first, second, third, and so on) polynomial, each within specified overlapping neighborhoods, to produce an output surface.
    """

    @property
    def description(self) -> str:
        return """

        LocalPolynomialInterpolation_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {power}, {search_neighborhood}, {kernel_function}, {bandwidth}, {use_condition_number}, {condition_number}, {weight_field}, {output_type})

        Fits the specified order (zero, first, second, third, and so on)
        polynomial, each within specified overlapping neighborhoods, to
        produce an output surface.

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
      kernel_function {String}:
          The kernel function used in the simulation.EXPONENTIAL-The function
          grows or decays proportionally.GAUSSIAN-Bell-
          shaped function that falls off quickly toward plus or
          minus infinity.QUARTIC-Fourth-order polynomial function.EPANECHNIKOV-A
          discontinuous parabolic function.POLYNOMIAL5-Fifth-order polynomial
          function.CONSTANT-An indicator function.
      bandwidth {Double}:
          Used to specify the maximum distance at which data points are used for
          prediction. With increasing bandwidth, prediction bias increases and
          prediction variance decreases.
      use_condition_number {Boolean}:
          Option to control the creation of prediction and prediction standard
          errors where the predictions are unstable. This option is only
          available for polynomials of order 1, 2, and
          3.NO_USE_CONDITION_NUMBER-Predictions will be created everywhere,
          including areas where the predictions are unstable. This is the
          default.USE_CONDITION_NUMBER-Prediction and prediction standard errors
          will
          not be created where the predictions are unstable.
      condition_number {Double}:
          Every invertible square matrix has a condition number that indicates
          how inaccurate the solution to the linear equations can be with a
          small change in the matrix coefficients (it can be due to imprecise
          data). If the condition number is large, a small change in the matrix
          coefficients results in a large change in the solution vector.
      weight_field {Field}:
          Used to emphasize an observation. The larger the weight, the more
          impact it has on the prediction. For coincident observations, assign
          the largest weight to the most reliable measurement.
      output_type {String}:
          Surface type to store the interpolation results.For more information
          about the output surface types, see What output
          surface types can the interpolation models
          generate?PREDICTION-Prediction surfaces are produced from the
          interpolated
          values.PREDICTION_STANDARD_ERROR-Standard Error surfaces are produced
          from
          the standard errors of the interpolated values.CONDITION_NUMBER-The
          Spatial condition number surface indicates the
          stability of calculations at a particular location. The larger the
          condition number, the more unstable the prediction, so locations with
          large condition numbers may be prone to artifacts and erratic
          predicted values.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only
          if no output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested.

        """