# Generated documentation for module arcpy.sa.Functions


class Rank(object):
    """
    Ranks on a cell-by-cell basis the values from a set of input rasters and determines which values are returned based on the value of the rank input raster.
    """

    @property
    def description(self) -> str:
        return """

        Rank_sa(in_rank_raster_or_constant, in_rasters;in_rasters..., {process_as_multiband})

        Ranks on a cell-by-cell basis the values from a set of input rasters
        and determines which values are returned based on the value of the
        rank input raster.

     INPUTS:
      in_rank_raster_or_constant (Composite Geodataset):
          The input raster that defines the rank position to be returned.A
          number can be used as an input; however, the cell size and extent
          must first be set in the environment.
      in_rasters (Composite Geodataset):
          The list of input rasters from which the cell value of the raster at
          the specified rank position will be obtained.For example, consider a
          particular location where the cell values in
          the three input rasters are 17, 8 and 11. The rank value for that
          location is defined as 3. The tool will first sort the input values.
          Since the rank value being requested is 3, the output value will be
          17.
      process_as_multiband {Boolean}:
          Specifies how the input multiband raster bands will be
          processed.SINGLE_BAND-Each band from a multiband raster input will be
          processed
          separately as a single band raster. This is the
          default.MULTI_BAND-Each multiband raster input will be processed as a
          multiband raster. The operation will be performed for each band from
          one input using the corresponding band number from the other inputs.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster.For each cell on the output raster, the values on
          the input rasters
          are sorted from lowest to highest, and the input rank raster's value
          is used to select which will be the output value.

        """