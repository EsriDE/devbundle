# Generated documentation for module arcpy.sa.Functions


class TabulateArea(object):
    """
    Calculates cross-tabulated areas between two datasets and outputs a table.
    """

    @property
    def description(self) -> str:
        return """

        TabulateArea_sa(in_zone_data, zone_field, in_class_data, class_field, out_table, {processing_cell_size}, {classes_as_rows})

        Calculates cross-tabulated areas between two datasets and outputs a
        table.

     INPUTS:
      in_zone_data (Composite Geodataset):
          The dataset that defines the zones.The zones can be defined by an
          integer raster or a feature layer.
      zone_field (Field):
          The field that contains the values that define each zone.It can be an
          integer or a string field of the zone dataset.
      in_class_data (Composite Geodataset):
          The dataset that defines the classes that will have their area
          summarized within each zone.The class input can be an integer raster
          layer or a feature layer.
      class_field (Field):
          The field that holds the class values.It can be an integer or a string
          field of the input class data.
      processing_cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      classes_as_rows {Boolean}:
          Specifies how the values from the input class raster will be
          represented in the output table.CLASSES_AS_FIELDS-Classes will be
          represented as fields. This is the
          default.CLASSES_AS_ROWS-Classes will be represented as rows.

     OUTPUTS:
      out_table (Table):
          The output table that will contain the summary of the area of each
          class in each zone.The format of the table is determined by the output
          location and path.
          By default, the output will be a geodatabase table if in a geodatabase
          workspace, and a dBASE table if in a file workspace.

        """