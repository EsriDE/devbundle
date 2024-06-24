# Generated documentation for module arcpy.ga


class EmpiricalBayesianKriging3D(object):
    """
    Interpolates 3D points using Empirical Bayesian Kriging methodology. All points must have x-, y-, and z-coordinates and a measured value to be interpolated. The output is a 3D geostatistical layer that calculates and renders itself as a 2D transect at a given elevation. The elevation of the layer can be changed using the range slider, and the layer will update to show the interpolated predictions for the new elevation.
    """

    @property
    def description(self) -> str:
        return """

        EmpiricalBayesianKriging3D_ga(in_features, elevation_field, value_field, out_ga_layer, {elevation_units}, {measurement_error_field}, {semivariogram_model_type}, {transformation_type}, {subset_size}, {overlap_factor}, {number_simulations}, {trend_removal}, {elev_inflation_factor}, {search_neighborhood}, {output_elevation}, {output_type}, {quantile_value}, {threshold_type}, {probability_threshold})

        Interpolates 3D points using Empirical Bayesian Kriging methodology.
        All points must have x-, y-, and z-coordinates and a measured value to
        be interpolated. The output is a 3D geostatistical layer that
        calculates and renders itself as a 2D transect at a given elevation.
        The elevation of the layer can be changed using the range slider, and
        the layer will update to show the interpolated predictions for the new
        elevation.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the field that will be
          interpolated.
      elevation_field (Field):
          The field of the input features containing the elevation value of each
          input point.If the elevation values are stored as geometry attributes
          in Shape.Z,
          it is recommended that you use that field. If the elevation values are
          stored in an attribute field, the elevation values must indicate
          distance from mean sea level. Positive values indicate distance above
          sea level, and negative values indicate distance below sea level.
      value_field (Field):
          The field of the input features containing the measured values that
          will be interpolated.
      elevation_units {String}:
          The units of the elevation field.If Shape.Z is provided as the
          elevation field, the units will
          automatically match the z-units of the vertical coordinate
          system.INCH-Elevations are in U.S. survey inches.FOOT-Elevations are
          in U.S.
          survey feet.YARD-Elevations are in U.S. survey
          yards.MILE_US-Elevations are in U.S. survey
          miles.NAUTICAL_MILE-Elevations are in U.S. survey nautical
          miles.MILLIMETER-Elevations are in millimeters.CENTIMETER-Elevations
          are in centimeters.DECIMETER-Elevations are in
          decimeters.METER-Elevations are in meters.KILOMETER-Elevations are in
          kilometers.INCH_INT-Elevations are in international
          inches.FOOT_INT-Elevations are in international
          feet.YARD_INT-Elevations are in international
          yards.MILE_INT-Elevations are in statute
          miles.NAUTICAL_MILE_INT-Elevations are in international nautical
          miles.
      measurement_error_field {Field}:
          The field of the input features containing measurement error values
          for each point. The value should correspond to one standard deviation
          of the measured value of each point. Use this field if the measurement
          error values are not the same at each point.A common source of
          nonconstant measurement error is when the data is
          measured with different devices. One device may be more precise than
          another, which means that it will have a smaller measurement error.
          For example, a thermometer rounds to the nearest degree and another
          thermometer rounds to the nearest tenth of a degree. The variability
          of measurements is often provided by the manufacturer of the measuring
          device, or it may be known from empirical practice.Leave this
          parameter empty if there are no measurement error values or
          the measurement error values are unknown.
      semivariogram_model_type {String}:
          The semivariogram model that will be used for the
          interpolation.POWER-The Power semivariogram model will be
          used.LINEAR-The Linear
          semivariogram model will be used.THIN_PLATE_SPLINE-The Thin Plate
          Spline semivariogram model will be
          used.EXPONENTIAL-The Exponential semivariogram model will be
          used.WHITTLE-The Whittle semivariogram model will be used.K_BESSEL-The
          K-Bessel semivariogram model will be used.
      transformation_type {String}:
          The type of transformation that will be applied to the input
          features.NONE-No transformation will be applied. This is the
          default.EMPIRICAL-Multiplicative Skewing transformation with Empirical
          base
          function will be applied.LOGEMPIRICAL-Multiplicative Skewing
          transformation with Log Empirical
          base function will be applied. All data values must be positive. If
          this option is chosen, all predictions will be positive.
      subset_size {Long}:
          The size of the subset. The input data will automatically be divided
          into subsets before processing. This parameter controls the number of
          points that will be in each subset.
      overlap_factor {Double}:
          A factor representing the degree of overlap between local models (also
          called subsets).Each input point can fall into several subsets, and
          the overlap factor
          specifies the average number of subsets into which each point will
          fall. A high value of the overlap factor produces a smoother output
          surface, but it also increases processing time. Values must be between
          1 and 5. The actual overlap that will be used will usually be larger
          than this value, so each subset will contain the same number of
          points.
      number_simulations {Long}:
          The number of simulated semivariograms that will be used for each
          local model.Using more simulations will make the model calculations
          more stable,
          but the model will take longer to calculate.
      trend_removal {String}:
          Specifies the order of trend removal in the vertical direction.For
          most 3D data, the values of the points change faster vertically
          than horizontally. Removing trend in the vertical direction will help
          alleviate this and stabilize calculations.NONE-Vertical trend will not
          be removed. This is the
          default.FIRST-First order vertical trend will be removed.
      elev_inflation_factor {Double}:
          A constant value that is multiplied by thevalue prior to
          subsetting and model estimation. For most 3D data, the values of the
          points change faster vertically than horizontally, and this factor
          stretches the locations of the points so that one unit of distance
          vertically is statistically equivalent to one unit of distance
          horizontally. The locations of the points will be moved back to their
          original locations before returning the result of the interpolation.
          This correction is needed to accurately estimate the semivariogram
          model as well as the correct neighbors for theparameter. The elevation
          inflation factor is unitless and will provide the same results
          regardless of the units of the x-, y-, or z-coordinate of the input
          points. Elevation fieldSearch neighborhoodIf no value is
          provided for this parameter, one will be calculated at
          run time using a maximum likelihood estimation. The value will be
          printed as a geoprocessing message. The value calculated at run time
          will be between 1 and 1000. However, you can provide values between
          0.01 and 1,000,000. If the calculated value is equal to 1 or 1000, you
          can provide values outside that range and choose a value based on
          cross validation.
      search_neighborhood {Geostatistical Search Neighborhood}:
          Specifies the number and orientation of the neighbors using the
          SearchNeighborhoodStandard3D class.Standard3Dradius-The length of the
          radius of the search neighborhood.nbrMax-The
          maximum number of neighbors per sector that will be used to
          estimate the value at the unknown location.nbrMin-The minimum number
          of neighbors per sector that will be used to
          estimate the value at the unknown location. sectorType-The
          geometry of the 3D neighborhood. Sectors are
          used to ensure that neighbors are used in different directions around
          the prediction location. All sector types are formed from the Platonic
          solids. ONE_SECTOR-The closest neighbors from any direction
          will be
          used.FOUR_SECTORS-Space will be divided into 4 regions, and neighbors
          will
          be used in each of the 4 regions.SIX_SECTORS-Space will be divided
          into 6 regions, and neighbors will
          be used in each of the 6 regions.EIGHT_SECTORS-Space will be divided
          into 8 regions, and neighbors will
          be used in each of the 8 regions.TWELVE_SECTORS-Space will be divided
          into 12 regions, and neighbors
          will be used in each of the 12 regions.TWENTY_SECTORS-Space will be
          divided into 20 regions, and neighbors
          will be used in each of the 20 regions.
      output_elevation {Double}:
          The default elevation of the out_ga_layer parameter value.The
          geostatistical layer will draw as a horizontal surface at a given
          elevation, and this parameter specifies this elevation. After it's
          created, the elevation of the geostatistical layer can be changed
          using the range slider.
      output_type {String}:
          Surface type to store the interpolation results.For more information
          about output surface types, see What output
          surface types can the interpolation models
          generate.PREDICTION-Prediction surfaces are produced from the
          interpolated
          values.PREDICTION_STANDARD_ERROR-Standard Error surfaces are produced
          from
          the standard errors of the interpolated values.PROBABILITY-The output
          surface will be probability surfaces of values
          exceeding or not exceeding a certain threshold.QUANTILE-The output
          surface will be quantile surfaces predicting the
          specified quantile of the prediction distribution.
      quantile_value {Double}:
          The quantile value for which the output layer will be generated.
      threshold_type {String}:
          Specifies whether to calculate the probability that a value exceeds or
          does not exceed the specified threshold.EXCEED-The probability that
          the value exceeds the threshold will be
          calculated. This is the default.NOT_EXCEED-The probability that the
          value does not exceed the
          threshold will be calculated.
      probability_threshold {Double}:
          The probability threshold value. If no value is provided, the
          median (50quantile) of the input data will be used. th

     OUTPUTS:
      out_ga_layer (Geostatistical Layer):
          The output geostatistical layer that will display the interpolation
          result.

        """