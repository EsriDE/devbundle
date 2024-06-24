# Generated documentation for module arcpy.management


class MergeMosaicDatasetItems(object):
    """
    Groups multiple items in a mosaic dataset together as one item.
    """

    @property
    def description(self) -> str:
        return """

        MergeMosaicDatasetItems_management(in_mosaic_dataset, {where_clause}, {block_field}, {max_rows_per_merged_items})

        Groups multiple items in a mosaic dataset together as one item.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that has the items that you want to merge.
      where_clause {SQL Expression}:
          An SQL expression to select specific rasters to merge in the mosaic
          dataset.
      block_field {Field}:
          The field in the attribute table that you want to use to group images.
          Only date, numeric, and string fields can be specified as Block
          fields.
      max_rows_per_merged_items {Long}:
          Limits the number of items to merge. If the maximum is exceeded, the
          tool will create multiple merged items. The default is 1,000 rows.

        """