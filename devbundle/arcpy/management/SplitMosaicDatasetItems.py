# Generated documentation for module arcpy.management


class SplitMosaicDatasetItems(object):
    """
    Splits mosaic dataset items that were merged together using Merge Mosaic Dataset Items.
    """

    @property
    def description(self) -> str:
        return """

        SplitMosaicDatasetItems_management(in_mosaic_dataset, {where_clause})

        Splits mosaic dataset items that were merged together using Merge
        Mosaic Dataset Items.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset containing the items to split.
      where_clause {SQL Expression}:
          An SQL expression to select items to split.If the query does not
          contain any previously merged items, the tool
          will return an error.

        """