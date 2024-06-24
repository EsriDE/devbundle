# Generated documentation for module arcpy.management


class CalculateStatistics(object):
    """
    Calculates statistics for a raster dataset or a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        CalculateStatistics_management(in_raster_dataset, {x_skip_factor}, {y_skip_factor}, {ignore_values;ignore_values...}, {skip_existing}, {area_of_interest})

        Calculates statistics for a raster dataset or a mosaic dataset.

     INPUTS:
      in_raster_dataset (Mosaic Dataset / Mosaic Layer / Raster Layer / Raster Dataset):
          The input raster dataset or mosaic dataset.
      x_skip_factor {Long}:
          The number of horizontal pixels between samples.A skip factor controls
          the portion of the raster that is used when
          calculating the statistics. The input value indicates the horizontal
          or vertical skip factor, where a value of 1 will use each pixel and a
          value of 2 will use every second pixel. The skip factor can only range
          from 1 to the number of columns/rows in the raster.The value must be
          greater than zero and less than or equal to the
          number of columns in the raster. The default is 1 or the last skip
          factor used.The skip factors for raster datasets stored in a file
          geodatabase or
          an enterprise geodatabase are different. First, if the x and y skip
          factors are different, the smaller skip factor will be used for both
          the x and y skip factors. Second, the skip factor is related to the
          pyramid level that most closely fits the skip factor chosen. If the
          skip factor value is not equal to the number of pixels in a pyramid
          layer, the number is rounded down to the next pyramid level, and those
          statistics are used.
      y_skip_factor {Long}:
          The number of vertical pixels between samples.A skip factor controls
          the portion of the raster that is used when
          calculating the statistics. The input value indicates the horizontal
          or vertical skip factor, where a value of 1 will use each pixel and a
          value of 2 will use every second pixel. The skip factor can only range
          from 1 to the number of columns/rows in the raster.The value must be
          greater than zero and less than or equal to the
          number of rows in the raster. The default is 1 or the last y skip
          factor used.The skip factors for raster datasets stored in a file
          geodatabase or
          an enterprise geodatabase are different. First, if the x and y skip
          factors are different, the smaller skip factor will be used for both
          the x and y skip factors. Second, the skip factor is related to the
          pyramid level that most closely fits the skip factor chosen. If the
          skip factor value is not equal to the number of pixels in a pyramid
          layer, the number is rounded down to the next pyramid level, and those
          statistics are used.
      ignore_values {Long}:
          The pixel values that are not to be included in the statistics
          calculation.The default is no value or the last ignore value used.
      skip_existing {Boolean}:
          Specifies whether statistics will be calculated only when they are
          missing or will be regenerated even if they exist.OVERWRITE-Statistics
          will be calculated even if they already exist,
          and existing statistics will be overwritten. This is the
          default.SKIP_EXISTING-Statistics will only be calculated if they do
          not
          already exist.
      area_of_interest {Feature Set}:
          The feature class that represents the area in the dataset that will be
          used to calculate statistics, so they are not generated from the
          entire dataset.

        """