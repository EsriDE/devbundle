# Generated documentation for module arcpy.management


class ClearPixelCache(object):
    """
    Clears the pixel cache associated with a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        ClearPixelCache_management(in_mosaic_dataset, {generated_before})

        Clears the pixel cache associated with a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The input mosaic dataset with the pixel cache to be deleted.
      generated_before {Date}:
          All cache generated before this date will be deleted.

        """