# Generated documentation for module arcpy.ia.Functions


class MultidimensionalRasterCorrelation(object):
    """
    Analyzes correlations between two variables in one or two multidimensional rasters.
    """

    @property
    def description(self) -> str:
        return """

        MultidimensionalRasterCorrelation_ia(in_mdim_raster1, in_mdim_raster2, {dimension1}, {variable1}, {dimension2}, {variable2}, {corr_method}, {lag}, {calculate_xcorr}, {calculate_pvalue}, {out_max_corr_raster})

        Analyzes correlations between two variables in one or two
        multidimensional rasters.

     INPUTS:
      in_mdim_raster1 (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The input multidimensional raster dataset.The first multidimensional
          raster in any supported format.
      in_mdim_raster2 (Raster Dataset / Mosaic Dataset / Raster Layer / Mosaic Layer / Image Service):
          The second multidimensional raster that will be correlated with the
          first input. The length of the dimension used in the calculation must
          be greater than 2. Autocorrelation will be calculated if the
          in_mdim_raster1 parameter value is the same as the in_mdim_raster2
          parameter value. Autocorrelation refers to the degree of correlation
          of the same variables between two successive time intervals.
      dimension1 {String}:
          A dimension name in the first dataset, along which the pixel array is
          defined. When the input has two nonspatial dimensions, a dimension
          must be specified. The length of the dimension used in the calculation
          must be greater than 2.
      variable1 {String}:
          A variable name from the first input raster.
      dimension2 {String}:
          A dimension name in the second dataset. The length of the dimension
          used in the calculation must be greater than 2.
      variable2 {String}:
          A variable name from the second input raster.
      corr_method {String}:
          Specifies the correlation calculation method that will be
          used.PEARSON-The correlation method will be Pearson. This is the
          default.SPEARMAN-The correlation method will be Spearman.KENDALL-The
          correlation method will be Kendall.
      lag {Long}:
          Calculate a correlation value by shifting the pixel array by the step
          specified, from 0 to dimension/2, depending on the time lag. The
          default is 0.
      calculate_xcorr {Boolean}:
          Specifies whether the cross correlation will be computed at lags.When
          ALL_CROSS_CORRELATION is specified, the correlations will be
          calculated at each lag within a range defined by the lag value. For
          example, if the lag value is 2, correlations of -2, -1, 0, 1, and 2
          will be calculated and stored as bands in the output
          raster.ALL_CROSS_CORRELATION-The cross correlation will be computed
          at
          lags.NO_CROSS_CORRELATION-The cross correlation will not be computed
          at
          lags. This is the default.
      calculate_pvalue {Boolean}:
          Specifies whether the p-value will be computed at lags. P-value is a
          confidence value that describes how well the two variables are
          correlated.CALCULATE_P_VALUE-The p-value will be computed at lags.
          The output
          will include additional bands storing the p-values.NO_P_VALUE-The
          p-value will not be computed at lags. This is the
          default.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster dataset. When the lag parameter value is not 0, a
          cross correlation at each lag will be calculated and stored as bands
          in the output.
      out_max_corr_raster {Raster Dataset}:
          A 2-band raster with maximum correlation values and the lags at which
          the maximum correlations occur. The raster will be created when the
          calculate_xcorr parameter is specified as ALL_CROSS_CORRELATION.

        """