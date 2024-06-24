# Generated documentation for module arcpy.management


class SynchronizeMosaicDataset(object):
    """
    Synchronizes a mosaic dataset to keep it up to date. In addition to syncing data, you can update overviews if the underlying imagery has been changed, generate new overviews and cache, and restore the original configuration of mosaic dataset items. You can also remove paths to source data with this tool. To repair paths, use the Repair Mosaic Dataset Paths tool.
    """

    @property
    def description(self) -> str:
        return """

        SynchronizeMosaicDataset_management(in_mosaic_dataset, {where_clause}, {new_items}, {sync_only_stale}, {update_cellsize_ranges}, {update_boundary}, {update_overviews}, {build_pyramids}, {calculate_statistics}, {build_thumbnails}, {build_item_cache}, {rebuild_raster}, {update_fields}, {fields_to_update;fields_to_update...}, {existing_items}, {broken_items}, {skip_existing_items}, {refresh_aggregate_info}, {estimate_statistics})

        Synchronizes a mosaic dataset to keep it up to date. In addition to
        syncing data, you can update overviews if the underlying imagery has
        been changed, generate new overviews and cache, and restore the
        original configuration of mosaic dataset items. You can also remove
        paths to source data with this tool. To repair paths, use the Repair
        Mosaic Dataset Paths tool.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that will be synchronized.
      where_clause {SQL Expression}:
          An SQL expression to select which mosaic dataset items will be
          synchronized. If an expression is not provided, all dataset items will
          be updated.
      new_items {Boolean}:
          Specifies whether new items will be included when synchronizing as
          well as the options to use to update the new items.If you use this
          option, the item's workspace will be searched for new
          data. When data is added to the mosaic dataset, it will use the same
          raster type as the other items in the same workspace.NO_NEW_ITEMS-No
          new items will be added when synchronizing. This is
          the default.UPDATE_WITH_NEW_ITEMS-The mosaic dataset will be updated
          with new
          items in the workspaces. Optionally, the existing items can be
          modified by setting the skip_existing_items parameter to
          OVERWRITE_EXISTING_ITEMS.
      sync_only_stale {Boolean}:
          Specifies whether mosaic dataset items will be updated only when the
          underlying raster datasets have been modified due to synchronizing.
          For example, building pyramids or updating the georeferencing of
          rasters will affect how the overviews are rendered.SYNC_STALE-Only the
          items of the underlying raster datasets that have
          been modified will be updated. This is the default.SYNC_ALL-All of the
          items in the mosaic dataset will be updated.
      update_cellsize_ranges {Boolean}:
          Specifies whether cell size ranges for the mosaic dataset will be
          recalculated.UPDATE_CELL_SIZES-The cell size ranges for the entire
          mosaic dataset
          will be recalculated, but only for items that have an invalid
          visibility. This is the default.NO_CELL_SIZES-No cell size ranges will
          be recalculated.
      update_boundary {Boolean}:
          Specifies whether the boundary that shows the full extent of the
          mosaic dataset will be rebuilt. Choose UPDATE_BOUNDARY if syncing will
          change the extent of the mosaic dataset.UPDATE_BOUNDARY-The boundary
          will be rebuilt after the mosaic dataset
          is synchronized. This is the default.NO_BOUNDARY-The boundary will
          not be rebuilt.
      update_overviews {Boolean}:
          Specifies whether obsolete overviews will be updated. The overview
          becomes obsolete if any underlying rasters have been modified due to
          synchronizing.NO_OVERVIEWS-The overviews will not be updated. This is
          the
          default.UPDATE_OVERVIEWS-The affected overviews will be updated after
          the
          mosaic dataset is synchronized.
      build_pyramids {Boolean}:
          Specifies whether pyramids will be built for the specified mosaic
          dataset items. Pyramids can be built for each raster item in the
          mosaic dataset. Pyramids can improve the speed at which each raster is
          displayed.NO_PYRAMIDS-Pyramids will not be built. This is the
          default.BUILD_PYRAMIDS-Pyramids will be built for all the mosaic
          raster items
          that were updated due to synchronization.Pyramids will not be built
          for items that were added due to
          synchronization.
      calculate_statistics {Boolean}:
          Specifies whether statistics will be calculated for the specified
          mosaic dataset items. Statistics are required for a mosaic dataset
          when performing certain tasks, such as applying a contrast
          stretch.NO_STATISTICS-Statistics will not be calculated. This is the
          default.CALCULATE_STATISTICS-Statistics will be calculated for the
          mosaic
          dataset items that were updated due to synchronization.Statistics will
          not be calculated for items that were added due to
          synchronization.
      build_thumbnails {Boolean}:
          Specifies whether thumbnails will be built for the specified mosaic
          dataset items. Thumbnails are small, highly resampled images that can
          be created for each raster item in the mosaic definition. Thumbnails
          can be accessed when the mosaic dataset is accessed as an image
          service and will display as part of the item
          description.NO_THUMBNAILS-Thumbnails will not be built or updated.
          This is the
          default.BUILD_THUMBNAILS-Thumbnails will be built or updated for all
          the
          raster items that were updated due to synchronization.Thumbnails will
          not be built for items that were added due to
          synchronization.
      build_item_cache {Boolean}:
          Choose whether to build a cache for the specified mosaic dataset
          items. A cache can be built when you've added data using the LAS,
          Terrain, or LAS dataset raster types.NO_ITEM_CACHE-A cache will not be
          built or updated. This is the
          default.BUILD_ITEM_CACHE-A cache will be built or updated for all the
          raster
          items that were updated due to synchronization.A cache will not be
          built for items that were added due to
          synchronization.
      rebuild_raster {Boolean}:
          Specifies whether the raster items will be rebuilt from the data
          source using the original raster type.REBUILD_RASTER-The rasters will
          be rebuilt from the source data. Any
          changes that you have performed on selected items in the mosaic
          dataset will be lost. This is the default.NO_RASTER-The rasters will
          not be rebuilt. Other primary fields will
          be reset if the update_fields parameter is set to UPDATE_FIELDS.This
          only affects items that will be synchronized. This parameter is
          not applicable if the new_items parameter is set to
          UPDATE_WITH_NEW_ITEMS.
      update_fields {Boolean}:
          Specifies whether the fields in the table will be updated. This only
          affects items that will be synchronized.UPDATE_FIELDS-The fields will
          be updated from the source files. This
          is the default.NO_FIELDS-The fields in the table will not be updated
          from the source.If you update the fields, you can control which fields
          are updated
          using the fields_to_update parameter. If you made edits to some of the
          fields, you can remove them using the fields_to_update parameter.
      fields_to_update {String}:
          The fields that will be updated.This parameter is only valid if the
          update_fields parameter is set to
          UPDATE_FIELDS.If you made edits to some of the fields, make sure they
          are not
          listed. Thefield can be refreshed, even if REBUILD_RASTER is
          not
          specified. However, if REBUILD_RASTER is specified, thefield will be
          rebuilt, even if the fields_to_update parameter value is not
          specified. RASTERRASTER
      existing_items {Boolean}:
          Specifies whether existing items in the mosaic dataset will be
          updated.If you use this parameter, choose which existing parameters to
          update:
          sync_only_stale, build_pyramids, calculate_statistics,
          build_thumbnails, build_item_cache, update_fields, or
          fields_to_update.UPDATE_EXISTING_ITEMS-The existing items will be
          updated with the
          parameters you chose to update. This is the
          default.IGNORE_EXISTING_ITEMS-The existing items will not be updated.
      broken_items {Boolean}:
          Specifies whether items with broken links will be removed.Ensure that
          all network connections are working properly. This tool
          will remove any items that cannot be
          accessed.IGNORE_BROKEN_ITEMS-Items with broken links will not be
          removed from
          the mosaic dataset. This is the default.REMOVE_BROKEN_ITEMS-Items with
          broken links will be removed from the
          mosaic dataset.
      skip_existing_items {Boolean}:
          Specifies whether existing mosaic dataset items will be skipped or
          updated with the modified files from disk. To use this parameter, the
          new_items parameter must be set to
          UPDATE_WITH_NEW_ITEMS.SKIP_EXISTING_ITEMS-While adding new mosaic
          dataset items, existing
          mosaic dataset items will be skipped; they will not be updated. This
          is the default.OVERWRITE_EXISTING_ITEMS-While adding new mosaic
          dataset items,
          existing mosaic dataset items that correspond to modified files on
          disk will be updated.
      refresh_aggregate_info {Boolean}:
          Specifies whether data that may have been removed from the mosaic
          dataset will be included. To use this parameter, the existing_items
          parameter must be set to IGNORE_EXISTING_ITEMS.NO_REFRESH_INFO-When
          synchronizing, rasters that may have been removed
          from the mosaic dataset will be excluded. This is the
          default.REFRESH_INFO-When synchronizing, rasters that may have been
          removed
          from the mosaic dataset will be included.
      estimate_statistics {Boolean}:
          Specifies whether statistics on the mosaic dataset will be
          estimated.NO_STATISTICS-When synchronizing, statistics on the mosaic
          dataset
          will not be estimated. This is the default.ESTIMATE_STATISTICS-When
          synchronizing, statistics on the mosaic
          dataset will be estimated.

        """