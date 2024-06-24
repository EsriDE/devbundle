# Generated documentation for module arcpy.sa.Functions


class RemoveRasterSegmentTilingArtifacts(object):
    """
    Corrects segments or objects cut by tile boundaries during the segmentation process performed as a raster function. This tool is helpful for some regional processes, such as image segmentation, that have inconsistencies near image tile boundaries.
    """

    @property
    def description(self) -> str:
        return """

        RemoveRasterSegmentTilingArtifacts_sa(in_segmented_raster, {tileSizeX}, {tileSizeY})

        Corrects segments or objects cut by tile boundaries during the
        segmentation process performed as a raster function. This tool is
        helpful for some regional processes, such as image segmentation, that
        have inconsistencies near image tile boundaries.

     INPUTS:
      in_segmented_raster (Raster Dataset / Mosaic Dataset / Mosaic Layer / Raster Layer / Image Service / String):
          Select the segmented raster with the tiling artifacts that you want to
          remove.
      tileSizeX {Long}:
          Specify the tile width from Segment Mean Shift. If left blank, the
          default is 512 pixels.
      tileSizeY {Long}:
          Specify the tile height from Segment Mean Shift. If left blank, the
          default is 512 pixels.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          The path and name of the segmented raster from which you are removing
          tiling artifacts.

        """