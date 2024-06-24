# Generated documentation for module arcpy.ia.Functions


class SummarizeCategoricalRaster(object):
    """
    Generates a table containing the pixel count for each class, in each slice of an input categorical raster.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeCategoricalRaster_ia(in_raster, out_table, {dimension}, {aoi}, {aoi_id_field})

        Generates a table containing the pixel count for each class, in each
        slice of an input categorical raster.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer / Image Service / String / Raster Dataset / Mosaic Dataset):
          The input multidimensional raster of integer type.
      dimension {String}:
          The input dimension to use for the summary. If there is more than one
          dimension and no value is specified, all slices will be summarized
          using all combinations of dimension values.
      aoi {Feature Layer}:
          The polygon feature layer containing the area or areas of interest to
          use when calculating the pixel count per category. If no area of
          interest is specified, the entire raster dataset will be included in
          the analysis.
      aoi_id_field {Field}:
          The field in the polygon feature layer that defines each area of
          interest. Text and integer fields are supported.

     OUTPUTS:
      out_table (Table):
          The output summary table. Geodatabase, database, text, Microsoft
          Excel, and comma-separated value (CSV) tables are supported.

        """