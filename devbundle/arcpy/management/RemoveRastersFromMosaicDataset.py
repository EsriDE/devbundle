# Generated documentation for module arcpy.management


class RemoveRastersFromMosaicDataset(object):
    """
    Removes selected rasters from a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        RemoveRastersFromMosaicDataset_management(in_mosaic_dataset, {where_clause}, {update_boundary}, {mark_overviews_items}, {delete_overview_images}, {delete_item_cache}, {remove_items}, {update_cellsize_ranges})

        Removes selected rasters from a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset containing the rasters that will be removed.
      where_clause {SQL Expression}:
          An SQL expression to select the raster datasets that will be removed
          from the mosaic dataset.You must specify a selection or a query;
          otherwise, the tool will not
          run. To delete all the records from the mosaic dataset, specify a
          query that selects all the rasters, such as "OBJECTID>=0".
      update_boundary {Boolean}:
          Specifies whether the boundary polygon of the mosaic dataset will be
          updated. By default, the boundary merges all the footprint polygons to
          create a single boundary representing the extent of the valid
          pixels.UPDATE_BOUNDARY-The boundary polygon of the mosaic dataset will
          be
          updated. This is the default.NO_BOUNDARY-The boundary polygon of the
          mosaic dataset will not be
          updated.
      mark_overviews_items {Boolean}:
          Specifies whether affected overviews will be identified.When the
          rasters in a mosaic dataset have been removed, overviews
          created using those rasters may no longer be accurate. Use this
          parameter to identify affected overviews so they can be updated or
          removed if they are no longer needed.MARK_OVERVIEW_ITEMS-The affected
          overviews will be identified. This is
          the default.NO_MARK_OVERVIEW_ITEMS-The affected overviews will not be
          identified.
      delete_overview_images {Boolean}:
          Specifies whether the overviews associated with the selected rasters
          will be removed.DELETE_OVERVIEW_IMAGES-The overviews associated with
          the selected
          rasters will be deleted. This is the
          default.NO_DELETE_OVERVIEW_IMAGES-The overviews associated with the
          selected
          rasters will not be deleted.
      delete_item_cache {Boolean}:
          Specifies whether the cache that is based on any source raster dataset
          that will be removed from the mosaic dataset will also be
          removed.DELETE_ITEM_CACHE-The cache that is based on any source raster
          dataset
          that will be removed from the mosaic dataset will also be removed.
          This is the default.NO_DELETE_ITEM_CACHE-The cache will not be removed
          and will remain a
          part of the mosaic dataset.
      remove_items {Boolean}:
          Specifies whether mosaic dataset items will be
          removed.REMOVE_MOSAICDATASET_ITEMS-Mosaic dataset items will be
          removed. This
          is the default.NO_REMOVE_MOSAICDATASET_ITEMS-Mosaic dataset items will
          not be
          removed.
      update_cellsize_ranges {Boolean}:
          Specifies whether the cell size ranges for the mosaic dataset will be
          updated.UPDATE_CELL_SIZES-The cell size ranges for the mosaic dataset
          will be
          updated. Use this if you are removing all of the imagery at a specific
          cell size. This is the default.NO_CELL_SIZES-The cell size ranges for
          the mosaic dataset will not be
          updated.

        """