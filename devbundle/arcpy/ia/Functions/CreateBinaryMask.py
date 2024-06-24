# Generated documentation for module arcpy.ia.Functions


class CreateBinaryMask(object):
    """
    Converts an input raster dataset to a binary raster. Pixels are labeled as either mask or background based on user-defined values.
    """

    @property
    def description(self) -> str:
        return """

        CreateBinaryMask_ia(in_raster, {background_value}, {flood_fill}, {expand_background}, {expand_mask}, {min_region_size}, {background_nodata})

        Converts an input raster dataset to a binary raster. Pixels are
        labeled as either mask or background based on user-defined values.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String / Raster Dataset / Mosaic Dataset):
          The input raster dataset. If the input is multiband, the first band
          will be used by default.
      background_value {Double}:
          The background value for the output raster. The default value is 0.
      flood_fill {Boolean}:
          Specifies how background pixel values will be
          determined.FLOOD_FILL-Background pixel values will be determined by
          the flood
          fill operation, which fills the connected pixels from the image
          boundary to the mask boundary. Pixels inside the mask will not be
          converted to background regardless of their
          value.NO_FLOOD_FILL-Background pixel values will be determined by the
          specified background value. This is the default.
      expand_background {Long}:
          The number of pixels that will be used to expand or shrink the
          background. Negative values will shrink the background.
      expand_mask {Long}:
          The number of pixels that will be used to expand or shrink the mask.
          Negative values will shrink the mask.
      min_region_size {Long}:
          The number of connected pixels that will be used to define a mask
          region. Mask regions that are smaller than this size will be
          classified as background.
      background_nodata {Boolean}:
          Specifies whether the background value will be set to
          NoData.BACKGROUND_NODATA-The background value will be set to
          NoData.BACKGROUND_DATA-The background value will not be set to NoData.
          This
          is the default.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output binary raster dataset. Supported formats are TIFF, CRF, and
          PNG.

        """