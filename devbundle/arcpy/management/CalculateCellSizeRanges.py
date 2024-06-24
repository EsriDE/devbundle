# Generated documentation for module arcpy.management


class CalculateCellSizeRanges(object):
    """
    Computes the visibility levels of raster datasets in a mosaic dataset based on the spatial resolution.
    """

    @property
    def description(self) -> str:
        return """

        CalculateCellSizeRanges_management(in_mosaic_dataset, {where_clause}, {do_compute_min}, {do_compute_max}, {max_range_factor}, {cell_size_tolerance_factor}, {update_missing_only})

        Computes the visibility levels of raster datasets in a mosaic dataset
        based on the spatial resolution.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset to calculate the visibility levels for.
      where_clause {SQL Expression}:
          An SQL expression to select specific rasters in the mosaic dataset on
          which to calculate visibility levels. If no query is specified, all
          the mosaic dataset items will have their cell size ranges calculated.
      do_compute_min {Boolean}:
          Compute the minimum pixel size for each selected raster in the mosaic
          dataset.MIN_CELL_SIZES-Compute the minimum pixel size. This is the
          default.NO_MIN_CELL_SIZES-Do not compute the minimum pixel size.
      do_compute_max {Boolean}:
          Compute the maximum pixel size for each selected raster in the mosaic
          dataset.MAX_CELL_SIZES-Compute the maximum pixel size. This is the
          default.NO_MAX_CELL_SIZES-Do not compute the maximum pixel size.
      max_range_factor {Double}:
          Set a multiplication factor to apply to the native resolution. The
          default is 10, meaning that an image with a resolution of 30 meters
          will be visible at a scale appropriate for 300 meters. The
          relationship between cell size and scale is as follows:Cell Size =
          Scale * 0.0254 / 96Scale = Cell Size * 96 / 0.0254
      cell_size_tolerance_factor {Double}:
          Use this to group images with similar resolutions as having the same
          nominal resolution. For example 1 m imagery and 0.9 m imagery can be
          grouped together by setting this factor to 0.1, because they are
          within 10% of each other.
      update_missing_only {Boolean}:
          Calculate only the missing cell size range values.UPDATE_ALL-Calculate
          cell size minimum and maximum values for selected
          rasters within the mosaic dataset. This is the
          default.UPDATE_MISSING_ONLY-Calculate cell size minimum and maximum
          values
          only if they do not exist.

        """