# Generated documentation for module arcpy.management


class ExportMosaicDatasetPaths(object):
    """
    Creates a table of the file path for each item in a mosaic dataset. You can specify whether the table contains all the file paths or just the ones that are broken.
    """

    @property
    def description(self) -> str:
        return """

        ExportMosaicDatasetPaths_management(in_mosaic_dataset, out_table, {where_clause}, {export_mode}, {types_of_paths;types_of_paths...})

        Creates a table of the file path for each item in a mosaic dataset.
        You can specify whether the table contains all the file paths or just
        the ones that are broken.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset containing the file paths to export.
      where_clause {SQL Expression}:
          An SQL expression to select specific rasters for export.
      export_mode {String}:
          Populate the table with either all of the paths, or only the broken
          paths.ALL-Export all paths to the table. This is the
          default.BROKEN-Export
          only broken paths to the table.
      types_of_paths {String}:
          Choose to export file paths from only the source raster, only the
          cache, or both. The default is to export all path types.RASTER-Export
          file paths from rasters.ITEM_CACHE-Export file paths
          from item cache.

     OUTPUTS:
      out_table (Table):
          The table to create. The table can be a geodatabase table or a .dbf
          file. Thefield in the output table is derived from the OID of
          the
          row in the original mosaic dataset table. SourceOID

        """