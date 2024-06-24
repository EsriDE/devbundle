# Generated documentation for module arcpy.ia.Functions


class InList(object):
    """
    Determines which values from the first input are contained in a set of other inputs, on a cell-by-cell basis.
    """

    @property
    def description(self) -> str:
        return """

        InList_ia(in_raster_or_constant, in_raster_or_constants;in_raster_or_constants..., {process_as_multiband})

        Determines which values from the first input are contained in a set of
        other inputs, on a cell-by-cell basis.

     INPUTS:
      in_raster_or_constant (Composite Geodataset):
          The input that defines the value that will be looked for in a list of
          rasters on a cell-by-cell basis.A number can be used as an input for
          this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
      in_raster_or_constants (Composite Geodataset):
          A list of input rasters that the first input will be evaluated
          against. For each location, if the cell value from the first input
          exists in any of the other rasters, that value will be assigned to the
          output raster. If the value does not exist in any of the other
          rasters, the output value at that location will be NoData.A number can
          be used as an input for this parameter, provided a raster
          is specified for the other parameter. To specify a number for both
          inputs, the cell size and extent must first be set in the environment.
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
          The output raster.

        """