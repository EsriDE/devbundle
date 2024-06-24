# Generated documentation for module arcpy.ia.Functions


class AnalyzeChangesUsingLandTrendr(object):
    """
    Evaluates changes in pixel values over time using the Landsat-based detection of trends in disturbance and recovery (LandTrendr) method and generates a change analysis raster containing the model results.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeChangesUsingLandTrendr_ia(in_multidimensional_raster, {processing_band}, {snapping_date}, {max_num_segments}, {vertex_count_overshoot}, {spike_threshold}, {recovery_threshold}, {prevent_one_year_recovery}, {recovery_trend}, {min_num_observations}, {best_model_proportion}, {pvalue_threshold}, {output_other_bands})

        Evaluates changes in pixel values over time using the Landsat-based
        detection of trends in disturbance and recovery (LandTrendr) method
        and generates a change analysis raster containing the model results.

     INPUTS:
      in_multidimensional_raster (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional raster dataset.
      processing_band {String}:
          The image band name to use for segmenting the pixel value trajectories
          over time. Choose the band name that will best capture the changes in
          the feature you want to observe.If no band value is specified and the
          input is multiband imagery, the
          first band in the multiband image will be used.
      snapping_date {String}:
          The date used to identify a slice for each year in the input
          multidimensional dataset. The slice with the date closest to the
          snapping date will be used. This parameter is required if the input
          dataset contains sub-yearly data.The default is 06-30, or June 30,
          which is approximately midway
          through a calendar year.
      max_num_segments {Long}:
          The maximum number of segments to be fitted to the time series for
          each pixel. The default is 5.
      vertex_count_overshoot {Long}:
          The number of additional vertices beyond max_num_segments + 1 that can
          be used to fit the model during the initial stage of identifying
          vertices. Later in the modeling process, the number of additional
          vertices will be reduced to max_num_segments + 1. The default is 2.
      spike_threshold {Double}:
          The threshold to use for dampening spikes or anomalies in the pixel
          value trajectory. The value must range between 0 and 1 in which 1
          means no dampening. The default is 0.9.
      recovery_threshold {Double}:
          The recovery threshold value in years. If a segment has a recovery
          rate that is faster than 1/recovery threshold, the segment is
          discarded and not included in the time series model. The value must
          range between 0 and 1. The default is 0.25.
      prevent_one_year_recovery {Boolean}:
          Specifies whether segments that exhibit a one year recovery will be
          excluded.ALLOW_ONE_YEAR_RECOVERY-Segments that exhibit a one year
          recovery will
          not be excluded.PREVENT_ONE_YEAR_RECOVERY-Segments that exhibit a one
          year recovery
          will be excluded. This is the default.
      recovery_trend {Boolean}:
          Specifies whether the recovery has an increasing (positive)
          trend.INCREASING_TREND-The recovery has an increasing trend. This is
          the
          default.DECREASING_TREND-The recovery has a decreasing trend.
      min_num_observations {Long}:
          The minimum number of valid observations required to perform fitting.
          The number of years in the input multidimensional dataset must be
          equal to or greater than this value. The default is 6.
      best_model_proportion {Double}:
          The best model proportion value. During the model selection process,
          the tool will calculate the p-value for each model and identify a
          model that has the most vertices while maintaining the smallest (most
          significant) p-value based on this proportion value. A value of 1
          means the model has the lowest p-value but may not have a high number
          of vertices. The default is 1.25.
      pvalue_threshold {Double}:
          The p-value threshold for a model to be selected. After the vertices
          are detected in the initial stage of the model fitting, the tool will
          fit each segment and calculate the p-value to determine the
          significance of the model. On the next iteration, the model will
          decrease the number of segments by one and recalculate the p-value.
          This will continue and, if the p-value is smaller than the value
          specified in this parameter, the model will be selected and the tool
          will stop searching for a better model. If no such model is selected,
          the tool will select a model with a p-value smaller than the lowest
          p-value × best model proportion value. The default is 0.01.
      output_other_bands {Boolean}:
          Specifies whether other bands will be included in the segmentation
          process.INCLUDE_OTHER_BANDS-Other bands will be included. The
          segmentation and
          vertices information from the initial segmentation band specified in
          the processing_band parameter will also be fitted to the remaining
          bands in the multiband images. The model results will include the
          segmentation band first, then the remaining
          bands.EXCLUDE_OTHER_BANDS-Other bands will not be included. This is
          the
          default.

     OUTPUTS:
      out_multidimensional_raster (Raster Dataset):
          The output Cloud Raster Format (CRF) multidimensional raster
          dataset.The output change analysis raster containing model information
          from
          the LandTrendr analysis.

        """