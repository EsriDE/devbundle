# Generated documentation for module arcpy.ia.Functions


class AnalyzeChangesUsingCCDC(object):
    """
    Evaluates changes in pixel values over time using the Continuous Change Detection and Classification (CCDC) method and generates a change analysis raster containing the model results.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeChangesUsingCCDC_ia(in_multidimensional_raster, out_ccdc_result, {bands;bands...}, {tmask_bands;tmask_bands...}, {chi_squared_threshold}, {min_anomaly_observations}, {update_frequency})

        Evaluates changes in pixel values over time using the Continuous
        Change Detection and Classification (CCDC) method and generates a
        change analysis raster containing the model results.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Mosaic Layer / Raster Layer / Image Service):
          The input multidimensional raster dataset.
      bands {Long}:
          The band IDs to use for change detection. If no band IDs are provided,
          all the bands from the input raster dataset will be used.
      tmask_bands {Long}:
          The band IDs to be used in the temporal mask (Tmask). It is
          recommended that you use the green band and the SWIR band. If no band
          IDs are provided, no masking will occur.
      chi_squared_threshold {Double}:
          The chi-square statistic change probability threshold. If an
          observation has a calculated change probability that is above this
          threshold, it is flagged as an anomaly, which is a potential change
          event. The default value is 0.99.
      min_anomaly_observations {Long}:
          The minimum number of consecutive anomaly observations that must occur
          before an event is considered a change. A pixel must be flagged as an
          anomaly for the specified number of consecutive time slices before it
          is considered a true change. The default value is 6.
      update_frequency {Double}:
          The frequency, in years, at which to update the time series model with
          new observations. The default value is 1.

     OUTPUTS:
      out_ccdc_result (Raster Dataset):
          The output Cloud Raster Format (CRF) multidimensional raster
          dataset.The output change analysis raster containing model information
          from
          the CCDC analysis.

        """