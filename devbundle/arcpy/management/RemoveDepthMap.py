# Generated documentation for module arcpy.management


class RemoveDepthMap(object):
    """
    Removes the depth map from a mosaic dataset. Other than the depth map removal, the tool will not update the mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        RemoveDepthMap_management(in_mosaic_dataset, {where_clause})

        Removes the depth map from a mosaic dataset. Other than the depth map
        removal, the tool will not update the mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The mosaic dataset that will have the depth map removed.
      where_clause {SQL Expression}:
          An SQL expression that will be used to select items in the mosaic
          dataset depth map to be removed. If not specified, all depth map
          content in the source raster's folder will be removed.

        """