# Generated documentation for module arcpy.management


class DeleteMosaicDataset(object):
    """
    Deletes a mosaic dataset, its overviews, and its item cache from disk.
    """

    @property
    def description(self) -> str:
        return """

        DeleteMosaicDataset_management(in_mosaic_dataset, {delete_overview_images}, {delete_item_cache})

        Deletes a mosaic dataset, its overviews, and its item cache from disk.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to delete.
      delete_overview_images {Boolean}:
          Delete all overviews associated with the mosaic
          dataset.DELETE_OVERVIEW_IMAGES-Delete the overviews associated with
          the mosaic
          dataset. This is the default.NO_DELETE_OVERVIEW_IMAGES-Do not delete
          the overviews.
      delete_item_cache {Boolean}:
          Delete the item cache associated with the mosaic
          dataset.DELETE_ITEM_CACHE-Delete the item cache associated with the
          mosaic
          dataset. This is the default.NO_DELETE_ITEM_CACHE-Do not delete the
          item cache.

        """