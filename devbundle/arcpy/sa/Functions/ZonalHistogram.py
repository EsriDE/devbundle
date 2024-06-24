# Generated documentation for module arcpy.sa.Functions


class ZonalHistogram(object):
    """
    Creates a table and a histogram graph that show the frequency distribution of cell values on the value input for each unique zone.
    """

    @property
    def description(self) -> str:
        return """

        ZonalHistogram_sa(in_zone_data, zone_field, in_value_raster, out_table, {out_graph}, {zones_as_rows})

        Creates a table and a histogram graph that show the frequency
        distribution of cell values on the value input for each unique zone.

     INPUTS:
      in_zone_data (Composite Geodataset):
          The dataset that defines the zones.The zones can be defined by an
          integer raster or a feature layer.
      zone_field (Field):
          The field that contains the values that define each zone.It can be an
          integer or a string field of the zone dataset.
      in_value_raster (Composite Geodataset):
          The raster that contains the values used to create the histogram.
      zones_as_rows {Boolean}:
          Specifies how the values from the input value raster will be
          represented in the output table.ZONES_AS_FIELDS-Zones will be
          represented as fields. This is the
          default.ZONES_AS_ROWS-Zones will be represented as rows.

     OUTPUTS:
      out_table (Table):
          The output table file.The format of the table is determined by the
          output location and path.
          By default, the output will be a geodatabase table if in a geodatabase
          workspace, and a dBASE table if in a file workspace.The optional graph
          output is created from the information in the
          table.
      out_graph {String}:
          The name of the output graph for display.

        """