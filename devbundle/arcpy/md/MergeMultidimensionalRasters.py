# Generated documentation for module arcpy.md


class MergeMultidimensionalRasters(object):
    """
    Combines multiple multidimensional raster datasets spatially or across variables and dimensions.
    """

    @property
    def description(self) -> str:
        return """

        MergeMultidimensionalRasters_md(in_multidimensional_rasters;in_multidimensional_rasters..., out_raster, {resolve_overlap_method})

        Combines multiple multidimensional raster datasets spatially or across
        variables and dimensions.

     INPUTS:
      in_multidimensional_rasters (Raster Layer / Mosaic Layer / Raster Dataset / Mosaic Dataset / Image Service / File):
          The input multidimensional rasters to be combined.
      resolve_overlap_method {String}:
          Specifies the method that will be used to resolve overlapping pixels
          in the combined datasets.FIRST-The pixel value in the overlapping
          areas will be the value from
          the first raster in the list of input rasters. This is the
          default.LAST-The pixel value in the overlapping areas will be the
          value from
          the last raster in the list of input rasters.MIN-The pixel value in
          the overlapping areas will be the minimum value
          of the overlapping pixels.MAX-The pixel value in the overlapping areas
          will be the maximum value
          of the overlapping pixels.MEAN-The pixel value in the overlapping
          areas will be the average of
          the overlapping pixels.SUM-The pixel value in the overlapping areas
          will be the total sum of
          the overlapping pixels.

     OUTPUTS:
      out_raster (Raster Dataset):
          The merged multidimensional raster dataset in Cloud Raster Format (a
          .crf file) or NetCDF format (an .nc file).

        """