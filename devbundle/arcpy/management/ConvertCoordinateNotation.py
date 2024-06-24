# Generated documentation for module arcpy.management


class ConvertCoordinateNotation(object):
    """
    Converts coordinate notations contained in one or two fields from one notation format to another.
    """

    @property
    def description(self) -> str:
        return """

        ConvertCoordinateNotation_management(in_table, out_featureclass, x_field, y_field, input_coordinate_format, output_coordinate_format, {id_field}, {spatial_reference}, {in_coor_system}, {exclude_invalid_records})

        Converts coordinate notations contained in one or two fields from one
        notation format to another.

     INPUTS:
      in_table (Table View):
          The input table or text file. Point features are also valid.
      x_field (Field):
          A field from the input table containing the longitude value.For the
          input_coordinate_format parameter's DD_2, DD_NUMERIC, DDM_2,
          and DMS_2 options, this is the longitude field.For the DD_1, DDM_1,
          and DMS_1 options, this field contains both
          latitude and longitude values in a single string.For the GARS, GEOREF,
          GEOREF16, UTM_ZONES, UTM_BANDS, USNG, USNG16,
          MGRS, and MGRS16 options, this field contains an alphanumeric system
          of notation in a single text field.
      y_field (Field):
          A field from the input table containing the latitude value.For the
          input_coordinate_format parameter's DD_2, DD_NUMERIC, DDM_2,
          and DMS_2 options, this is the longitude field.This parameter is
          ignored when one of the single-string formats is
          chosen.
      input_coordinate_format (String):
          Specifies the coordinate format of the input fields.DD_1-Both
          longitude and latitude values are in a single field. Two
          values are separated by a space, a comma, or a slash.
          DD_2-Longitude and latitude values are in two separate
          fields. This is the default.DDM_1-Both longitude and latitude
          values are in a single field. Two
          values are separated by a space, a comma, or a slash.DDM_2-Longitude
          and latitude values are in two separate fields.DMS_1-Both longitude
          and latitude values are in a single field. Two
          values are separated by a space, a comma, or a slash.DMS_2-Longitude
          and latitude values are in two separate fields.GARS-Global Area
          Reference System. Based on latitude and longitude, it
          divides and subdivides the world into cells.GEOREF-World Geographic
          Reference System. A grid-based system that
          divides the world into 15-degree quadrangles and then subdivides into
          smaller quadrangles.GEOREF16-World Geographic Reference System in
          16-digit precision.UTM_ZONES-The letter N or S after the UTM zone
          number designates only
          North or South hemisphere.UTM_BANDS-The letter after the UTM zone
          number designates one of the
          20 latitude bands. N or S does not designate a hemisphere.USNG-United
          States National Grid. Almost exactly the same as MGRS but
          uses North American Datum 1983 (NAD83) as its datum.USNG16-United
          States National Grid in 16-digit higher precision.MGRS-Military Grid
          Reference System. Follows the UTM coordinates and
          divides the world into 6-degree longitude and 20 latitude bands, but
          MGRS then further subdivides the grid zones into smaller 100,000-meter
          grids. These 100,000-meter grids are then divided into 10,000-meter,
          1,000-meter, 100-meter, 10-meter, and 1-meter grids.MGRS16-Military
          Grid Reference System in 16-digit precision.SHAPE-Only available when
          a point feature layer is selected as input.
          The coordinates of each point are used to define the output format.DD,
          DDM, DMS, and UTM are also valid keywords; they can be used just
          by typing in (on dialog) or passing the value in scripting. However,
          keywords with underscore and a qualifier tell more about the field
          values.
      output_coordinate_format (String):
          Specifies the coordinate format to which the input notations will be
          converted.DD_1-Both longitude and latitude values are in a single
          field. Two
          values are separated by a space, a comma, or a slash.DD_2-Longitude
          and latitude values are in two separate fields.DD_NUMERIC-Longitude
          and latitude values are in two separate fields of
          type Double. Values in the West and South are denoted by a minus
          sign.DDM_1-Both longitude and latitude values are in a single field.
          Two
          values are separated by a space, a comma, or a slash.DDM_2-Longitude
          and latitude values are in two separate fields.DMS_1-Both longitude
          and latitude values are in a single field. Two
          values are separated by a space, a comma, or a slash.DMS_2-Longitude
          and latitude values are in two separate fields.GARS-Global Area
          Reference System. Based on latitude and longitude, it
          divides and subdivides the world into cells.GEOREF-World Geographic
          Reference System. A grid-based system that
          divides the world into 15-degree quadrangles and then subdivides into
          smaller quadrangles.GEOREF16-World Geographic Reference System in
          16-digit precision.UTM_ZONES-The letter N or S after the UTM zone
          number designates only
          North or South hemisphere.UTM_BANDS-The letter after the UTM zone
          number designates one of the
          20 latitude bands. N or S does not designate a hemisphere.USNG-United
          States National Grid. Almost exactly the same as MGRS but
          uses North American Datum 1983 (NAD83) as its datum.USNG16-United
          States National Grid in 16-digit higher precision.MGRS-Military Grid
          Reference System. Follows the UTM coordinates and
          divides the world into 6-degree longitude and 20 latitude bands, but
          MGRS then further subdivides the grid zones into smaller 100,000-meter
          grids. These 100,000-meter grids are then divided into 10,000-meter,
          1,000-meter, 100-meter, 10-meter, and 1-meter grids.MGRS16-Military
          Grid Reference System in 16-digit precision.DD, DDM, DMS, and UTM are
          also valid keywords; they can be used just
          by typing in (on dialog) or passing the value in scripting. However,
          keywords with underscore and a qualifier tell more about the field
          values.
      id_field {Field}:
          This parameter is ignored, as all fields are transferred to output
          table.
      spatial_reference {Spatial Reference}:
          The spatial reference of the output feature class. The default is
          GCS_WGS_1984.The tool projects the output to the spatial reference
          specified. If
          the input and output coordinate systems are in a different datum, a
          default transformation will be used based on the coordinate systems of
          the input and the output and the extent of the data.
      in_coor_system {Coordinate System}:
          The spatial reference of the input data. If the input spatial
          reference cannot be obtained from the input table, a default of
          GCS_WGS_1984 will be used.
      exclude_invalid_records {Boolean}:
          Specifies whether to exclude records with invalid
          notation.EXCLUDE_INVALID-Invalid records will be excluded and only
          valid
          records will be converted to points in the output. This is the
          default.INCLUDE_INVALID-Valid records will be converted to points in
          the
          output and invalid records will be included as null geometry.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output point feature class. The attribute table will contain all
          fields of the input table along with the fields containing converted
          values in the output format.

        """