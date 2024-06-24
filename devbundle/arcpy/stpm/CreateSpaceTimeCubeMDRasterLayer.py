# Generated documentation for module arcpy.stpm


class CreateSpaceTimeCubeMDRasterLayer(object):
    """
    Creates a space-time cube from a multidimensional raster layer and structures the data into space-time bins for efficient space-time analysis and visualization.
    """

    @property
    def description(self) -> str:
        return """

        CreateSpaceTimeCubeMDRasterLayer_stpm(in_md_raster, output_cube, {fill_empty_bins})

        Creates a space-time cube from a multidimensional raster layer and
        structures the data into space-time bins for efficient space-time
        analysis and visualization.

     INPUTS:
      in_md_raster (Raster Layer):
          The input multidimensional raster layer that will be converted to a
          space-time cube.
      fill_empty_bins {String}:
          Specifies how missing values in the output space-time cube will be
          filled. Each space-time bin in the output must have a value, so you
          must specify how to fill in values for raster cells with NoData
          values.ZEROS-Empty bins with be filled with zeros. This is the
          default.SPATIAL_NEIGHBORS-Empty bins will be filled with the average
          value of
          spatial neighbors.SPACE_TIME_NEIGHBORS-Empty bins will be filled with
          the average value
          of space-time neighbors.TEMPORAL_TREND-Empty bins will be filled using
          an interpolated
          univariate spline algorithm.

     OUTPUTS:
      output_cube (File):
          The output netCDF data cube that will be created.

        """