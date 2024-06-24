# Generated documentation for module arcpy.ga


class ExtractValuesToTable(object):
    """
    Extracts cell values from a set of rasters to a table, based on a point or polygon feature class.
    """

    @property
    def description(self) -> str:
        return """

        ExtractValuesToTable_ga(in_features, in_rasters;in_rasters..., out_table, {out_raster_names_table}, {add_warning_field})

        Extracts cell values from a set of rasters to a table, based on a
        point or polygon feature class.

     INPUTS:
      in_features (Feature Layer):
          The points or polygon features to be created.
      in_rasters (Raster Layer / Mosaic Layer):
          The rasters must all have the same extent, coordinate system, and cell
          size.
      add_warning_field {Boolean}:
          Records if input features are partially or completely covered by the
          Input rasters.ADD_WARNING_FIELD-Warning field is added to the output
          table and
          populated with a P when a feature is partially covered by raster
          values.DO_NOT_ADD_WARNING_FIELD-Warning field is not added to the
          output
          table.

     OUTPUTS:
      out_table (Table):
          The output table contains a record for each point and each raster that
          has data. If polygon features are input, they are converted to points
          that coincide with the raster cell centers.
      out_raster_names_table {Table}:
          Saves the names of the Input rasters to disc.

        """