# Generated documentation for module arcpy.ga


class GALayer3DToMultidimensionalRaster(object):
    """
    Exports a 3D geostatistical layer created using the Empirical Bayesian Kriging 3D tool to a multidimensional Cloud Raster Format (*.crf file) raster dataset. Tools in the Multidimensional Analysis toolset of the Image Analyst toolbox are designed to work directly on multidimensional rasters and can identify the 3D nature of the data.
    """

    @property
    def description(self) -> str:
        return """

        GALayer3DToMultidimensionalRaster_ga(in_3d_geostat_layer, out_multidimensional_raster, {cell_size}, {explicit_only}, {min_elev}, {max_elev}, {elev_interval}, {elev_values;elev_values...}, {elev_units}, {output_type}, {quantile_probability_value}, {additional_outputs;additional_outputs...}, {build_transpose})

        Exports a 3D geostatistical layer created using the Empirical Bayesian
        Kriging 3D tool to a multidimensional Cloud Raster Format (*.crf file)
        raster dataset. Tools in the Multidimensional Analysis toolset of the
        Image Analyst toolbox are designed to work directly on
        multidimensional rasters and can identify the 3D nature of the data.

     INPUTS:
      in_3d_geostat_layer (Geostatistical Layer):
          The 3D geostatistical layer representing the model to be exported to a
          multivariate raster dataset.
      cell_size {Analysis Cell Size}:
          The cell size of the output multidimensional raster.
      explicit_only {Boolean}:
          Specifies whether elevations will be provided as an explicit list or
          an iterator will be used.EXPLICIT_VALUES-Elevation values will be
          provided as a
          list.NO_EXPLICIT_VALUES-Elevation values will be provided using an
          iterator. This is the default.
      min_elev {Double}:
          The minimum elevation that will be used to start the iteration.
      max_elev {Double}:
          The maximum elevation that will be used to stop the iteration.
      elev_interval {Double}:
          The increment that the elevation will increase with each iteration.
      elev_values {Double}:
          The elevation values to export.
      elev_units {String}:
          Specifies the measurement unit of the elevation values.INCH-Elevations
          are in U.S. survey inches.FOOT-Elevations are in U.S.
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
      output_type {String}:
          Specifies the primary output type of the output
          multidimensional raster. Theparameter can be used to specify
          additional variables in the output multidimensional raster.
          Additional output typesFor more information, see What output surface
          types can the
          interpolation models generate?PREDICTION-A multidimensional raster of
          predicted values. This is the
          default.PREDICTION_STANDARD_ERROR-A multidimensional raster of
          standard errors
          of prediction.PROBABILITY-A multidimensional raster predicting the
          probability that
          a threshold is exceeded.QUANTILE-A multidimensional raster predicting
          the quantile of the
          predicted value.
      quantile_probability_value {Double}:
          Ifis set to, use this parameter to enter the requested
          quantile. Ifis set to, use this parameter to enter the requested
          threshold value, and the probability that the threshold is exceeded
          will be calculated. Subtract this value from one to get the
          probability that the threshold is not exceeded. Output
          typeQuantileOutput typeProbability
      additional_outputs {Value Table}:
          Specifies the output type and quantile or probability value for each
          additional output type. If multiple output types are provided, the
          output raster will be a multivariate raster dataset with a different
          variable for each output type.For more information, see What output
          surface types can the
          interpolation models generate?
      build_transpose {Boolean}:
          Specifies whether multidimensional transposes will be built on the
          output multidimensional raster.BUILD_TRANSPOSE-Multidimensional
          transposes will be built on the
          output multidimensional raster.DO_NOT_BUILD_TRANSPOSE-Multidimensional
          transposes will not be built
          on the output multidimensional raster. This is the default.

     OUTPUTS:
      out_multidimensional_raster (Raster Dataset):
          The output raster dataset containing the results of exporting the
          geostatistical model. The output must be saved as a Cloud Raster
          Format file (*.crf).

        """