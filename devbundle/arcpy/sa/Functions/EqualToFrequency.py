# Generated documentation for module arcpy.sa.Functions


class EqualToFrequency(object):
    """
    Evaluates on a cell-by-cell basis the number of times the values in a set of rasters are equal to another raster.
    """

    @property
    def description(self) -> str:
        return """

        EqualToFrequency_sa(in_value_raster, in_rasters;in_rasters..., {process_as_multiband})

        Evaluates on a cell-by-cell basis the number of times the values in a
        set of rasters are equal to another raster.

     INPUTS:
      in_value_raster (Composite Geodataset):
          For each cell location in the input value raster, the number of
          occurrences (frequency) where a raster in the input list has an equal
          value is counted.
      in_rasters (Composite Geodataset):
          The list of rasters that will be compared to the value raster.
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
          The output raster.For each cell in the output raster, the value
          represents the number of
          times that the corresponding cells in the list of rasters are the same
          as the value raster.

        """