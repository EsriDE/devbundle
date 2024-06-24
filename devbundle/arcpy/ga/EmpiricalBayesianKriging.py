# Generated documentation for module arcpy.ga


class EmpiricalBayesianKriging(object):
    """
    Empirical Bayesian kriging is an interpolation method that accounts for the error in estimating the underlying semivariogram through repeated simulations.
    """

    @property
    def description(self) -> str:
        return """

        EmpiricalBayesianKriging_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {transformation_type}, {max_local_points}, {overlap_factor}, {number_semivariograms}, {search_neighborhood}, {output_type}, {quantile_value}, {threshold_type}, {probability_threshold}, {semivariogram_model_type})

        Empirical Bayesian kriging is an interpolation method that accounts
        for the error in estimating the underlying semivariogram through
        repeated simulations.

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
      transformation_type {String}:
          Type of transformation to be applied to the input data.NONE-Do not
          apply any transformation. This is the
          default.EMPIRICAL-Multiplicative Skewing transformation with Empirical
          base
          function.LOGEMPIRICAL-Multiplicative Skewing transformation with Log
          Empirical
          base function. All data values must be positive. If this option is
          chosen, all predictions will be positive.
      max_local_points {Long}:
          The input data will automatically be divided into groups that do not
          have more than this number of points.
      overlap_factor {Double}:
          A factor representing the degree of overlap between local models (also
          called subsets). Each input point can fall into several subsets, and
          the overlap factor specifies the average number of subsets that each
          point will fall into. A high value of the overlap factor makes the
          output surface smoother, but it also increases processing time.
          Typical values vary between 0.01 and 5.
      number_semivariograms {Long}:
          The number of simulated semivariograms of each local model.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Defines which surrounding points will be used to control the output.
          Standard Circular is the default.The following are Search Neighborhood
          classes:
          SearchNeighborhoodStandardCircular and
          SearchNeighborhoodSmoothCircular.Standard Circularradius-The length of
          the radius of the search circle.angle-The angle
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
      output_type {String}:
          Surface type to store the interpolation results.For more information
          about the output surface types, see What output
          surface types can the interpolation models
          generate?PREDICTION-Prediction surfaces are produced from the
          interpolated
          values.PREDICTION_STANDARD_ERROR-Standard Error surfaces are produced
          from
          the standard errors of the interpolated values.PROBABILITY-Probability
          surface of values exceeding or not exceeding a
          certain threshold.QUANTILE-Quantile surface predicting the specified
          quantile of the
          prediction distribution.
      quantile_value {Double}:
          The quantile value for which the output raster will be generated.
      threshold_type {String}:
          Specifies whether to calculate the probability of exceeding or not
          exceeding the specified threshold.EXCEED-Probability values exceed the
          threshold. This is the
          default.NOT_EXCEED-Probability values will not exceed the threshold.
      probability_threshold {Double}:
          The probability threshold value. If left empty, the median
          (50quantile) of the input data will be used. th
      semivariogram_model_type {String}:
          The semivariogram model that will be used for the
          interpolation.POWER-Power semivariogramLINEAR-Linear
          semivariogramTHIN_PLATE_SPLINE-Thin Plate Spline
          semivariogramEXPONENTIAL-Exponential
          semivariogramEXPONENTIAL_DETRENDED-Exponential semivariogram with
          first order trend
          removalWHITTLE-Whittle semivariogramWHITTLE_DETRENDED-Whittle
          semivariogram with first order trend removalK_BESSEL-K-Bessel
          semivariogramK_BESSEL_DETRENDED-K-Bessel semivariogram with first
          order trend
          removalThe available choices depend on the value of the
          transformation_type
          parameter. If the transformation type is set to NONE, only the first
          three semivariograms are available. If the type is EMPIRICAL or
          LOGEMPIRICAL, the last six semivariograms are available.For more
          information about choosing an appropriate semivariogram for
          your data, see the topic What is Empirical Bayesian Kriging.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only
          if no output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested.

        """