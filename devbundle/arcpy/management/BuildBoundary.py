# Generated documentation for module arcpy.management


class BuildBoundary(object):
    """
    Updates the extent of the boundary when adding new raster datasets to a mosaic dataset that extend beyond its previous coverage.
    """

    @property
    def description(self) -> str:
        return """

        BuildBoundary_management(in_mosaic_dataset, {where_clause}, {append_to_existing}, {simplification_method})

        Updates the extent of the boundary when adding new raster datasets to
        a mosaic dataset that extend beyond its previous coverage.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          Select the mosaic dataset where you want to recompute the boundary.
      where_clause {SQL Expression}:
          An SQL query to compute a boundary for select raster datasets. Use
          this option in conjunction with setting the append_to_existing
          parameter to APPEND to save time when adding new raster datasets.
      append_to_existing {Boolean}:
          Set this to APPEND when adding new raster datasets to an existing
          mosaic dataset. Instead of calculating the entire boundary, APPEND
          will merge the boundary of the new raster datasets with the existing
          boundary.OVERWRITE-Recompute the boundary in its
          entirety.APPEND-Append the
          perimeter of footprints to the existing boundary.
          This can save time when adding additional raster data to the mosaic
          dataset, as the entire boundary will not be recalculated. If there are
          rasters selected, the boundary will be recalculated to include only
          the selected footprints. This is the default.
      simplification_method {String}:
          Specifies the simplification method that will be used to reduce the
          number of vertices, since a dense boundary can affect
          performance.Choose the simplification method to use to simplify the
          boundary.NONE-No simplification method will be used. This is the
          default.CONVEX_HULL-The minimum bounding geometry of the mosaic
          dataset will
          be used to simplify the boundary. If there are disconnected
          footprints, a minimum bounding geometry for each continuous group of
          footprints will be used to simplify the boundary.ENVELOPE-The envelope
          of the mosaic dataset will provide a simplified
          boundary. If there are disconnected footprints, an envelope for each
          continuous group of footprints will be used to simplify the boundary.

        """