# Generated documentation for module arcpy.ga


class GALayerToRasters(object):
    """
    Exports a geostatistical layer to one or multiple rasters.
    """

    @property
    def description(self) -> str:
        return """

        GALayerToRasters_ga(in_geostat_layer, out_raster, {output_type}, {quantile_probability_value}, {cell_size}, {points_per_block_horz}, {points_per_block_vert}, {additional_rasters;additional_rasters...}, {out_elevation})

        Exports a geostatistical layer to one or multiple rasters.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.
      output_type {String}:
          The surface type of the output raster.For more information, see What
          output surface types can the
          interpolation models generate?PREDICTION-A raster of predicted
          values.PREDICTION_STANDARD_ERROR-A
          raster of standard errors of prediction.PROBABILITY-A raster
          predicting the probability that a threshold is
          exceeded.QUANTILE-A raster predicting the quantile of the predicted
          value.STANDARD_ERROR_INDICATORS-A raster of standard errors of
          indicators.CONDITION_NUMBER-A raster showing the condition number for
          predictions
          in Local Polynomial Interpolation. The condition number surface
          indicates the stability of calculations at a particular location. The
          larger the condition number, the more unstable the prediction, so
          locations with large condition numbers may be prone to artifacts and
          erratic predicted values.
      quantile_probability_value {Double}:
          If theis set to, use this parameter to enter the requested
          quantile. If theis set to, use this parameter to enter the requested
          threshold value, then the probability that the threshold is exceeded
          will be calculated. Output surface typeQuantileOutput surface
          typeProbability
      cell_size {Analysis Cell Size}:
          The cell size of the output rasters. This value will be shared
          by theand theparameters. Output rasterAdditional output rasters
      points_per_block_horz {Long}:
          The number of predictions for each cell in the horizontal direction
          for block interpolation. The default is 1.
      points_per_block_vert {Long}:
          The number of predictions for each cell in the vertical direction for
          block interpolation. The default is 1.
      additional_rasters {Value Table}:
          Provide the name, output type, and quantile or probability
          value for each additional output raster. See the descriptions of
          parameters above for more information. These additional rasters will
          be saved in the same location as the. Output raster
      out_elevation {Linear Unit}:
          For 3D interpolation models, you can export rasters at any elevation.
          Use this parameter to specify the elevation you want to export. If
          left empty, the elevation will be inherited from the input layer. The
          units will default to the same units of the input layer.

     OUTPUTS:
      out_raster (Raster Dataset):
          The primary output raster to be created. Additional rasters
          can be created with theparameter. Additional output rasters

        """