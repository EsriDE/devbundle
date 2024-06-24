# Generated documentation for module arcpy.ia.Functions


class InterpolateFromSpatiotemporalPoints(object):
    """
    Interpolates temporal point data into a multidimensional raster.
    """

    @property
    def description(self) -> str:
        return """

        InterpolateFromSpatiotemporalPoints_ia(in_dataset, variable_field, time_field, temporal_aggregation, cell_size, interpolation_method)

        Interpolates temporal point data into a multidimensional raster.

     INPUTS:
      in_dataset (Mosaic Dataset / Mosaic Layer / Feature Layer / Trajectory Layer):
          The input point layer, trajectory layer, or trajectory dataset.
      variable_field (String):
          A field containing variable values.
      time_field (String):
          A field containing time values.
      temporal_aggregation (String):
          Specifies the temporal aggregation of the output multidimensional
          raster. The interpolation algorithm uses all available data within
          these time periods to calculate the output slice.DAILY-The data values
          will be aggregated into daily time steps. This
          is the default.WEEKLY-The data values will be aggregated into weekly
          time steps.MONTHLY-The data values will be aggregated into monthly
          time steps.QUARTERLY-The data values will be aggregated into quarterly
          time
          steps.YEARLY-The data values will be aggregated into yearly time
          steps.
      cell_size (Double):
          The output cell size. By default, the cell size will be the shorter of
          the width or the height of the input point feature extent, divided by
          250.
      interpolation_method (String):
          Specifies the interpolation method that will be used.IDW-Inverse
          distance weighted interpolation will be
          used.TRIANGULATION-Triangulation interpolation will be used.MEAN-Mean
          interpolation will be used.MEDIAN-Median interpolation will be
          used.NATURAL_NEIGHBOR-Natural neighbor interpolation will be
          used.NEAREST_NEIGHBOR-Nearest neighbor interpolation will be
          used.QUADRATIC-Quadratic interpolation will be used.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output multidimensional raster dataset.

        """