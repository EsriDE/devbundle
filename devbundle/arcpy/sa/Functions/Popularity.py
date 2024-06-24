# Generated documentation for module arcpy.sa.Functions


class Popularity(object):
    """
    Determines the value in an argument list that is at a certain level of popularity on a cell-by-cell basis. The particular level of popularity (the number of occurrences of each value) is specified by the first argument.
    """

    @property
    def description(self) -> str:
        return """

        Popularity_sa(in_popularity_raster_or_constant, in_rasters;in_rasters..., {process_as_multiband})

        Determines the value in an argument list that is at a certain level of
        popularity on a cell-by-cell basis. The particular level of popularity
        (the number of occurrences of each value) is specified by the first
        argument.

     INPUTS:
      in_popularity_raster_or_constant (Composite Geodataset):
          The input raster that defines the popularity position to be returned.A
          number can be used as an input; however, the cell size and extent
          must first be set in the environment.
      in_rasters (Composite Geodataset):
          The list of input rasters used to evaluate the popularity of the
          values for each cell location.
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
          The output raster.Each cell on the output raster represents the value
          from the same
          location of input rasters that meets the input popularity value.

        """