# Generated documentation for module arcpy.sa.Functions


class ZonalGeometryAsTable(object):
    """
    Calculates the geometry measures (area, perimeter, thickness, and the characteristics of an ellipse) for each zone in a dataset and reports the results as a table.
    """

    @property
    def description(self) -> str:
        return """

        ZonalGeometryAsTable_sa(in_zone_data, zone_field, out_table, {processing_cell_size})

        Calculates the geometry measures (area, perimeter, thickness, and the
        characteristics of an ellipse) for each zone in a dataset and reports
        the results as a table.

     INPUTS:
      in_zone_data (Composite Geodataset):
          The dataset that defines the zones.The zones can be defined by an
          integer raster or a feature layer.
      zone_field (Field):
          The field that contains the values that define each zone.It must be an
          integer field of the zone dataset.
      processing_cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.

     OUTPUTS:
      out_table (Table):
          Output table that will contain the summary of the values in each
          zone.The format of the table is determined by the output location and
          path.
          By default, the output will be a geodatabase table. If the path is not
          in a geodatabase, the format is determined by the extension. If the
          extension is .dbf, it will be in dBASE format. If no extension is
          provided, the output will be an INFO table. INFO tables are not
          supported as input in ArcGIS Pro and cannot be displayed

        """