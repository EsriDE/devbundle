# Generated documentation for module arcpy.gapro


class UpdateBDCDatasetProperties(object):
    """
    Updates the properties of a multifile feature connection (MFC) dataset. This tool modifies field, geometry, time, and file settings for a specified MFC dataset.
    """

    @property
    def description(self) -> str:
        return """

        UpdateBDCDatasetProperties_gapro(bdc_dataset, {expression}, {field_properties;field_properties...}, {geometry_type}, {spatial_reference}, {geometry_format_type}, {geometry_field}, {x_field}, {y_field}, {z_field}, {time_type}, {time_zone}, {start_time_format;start_time_format...}, {end_time_format;end_time_format...}, {file_extension}, {field_delimiter}, {record_terminator}, {quote_character}, {has_header_row}, {encoding})

        Updates the properties of a multifile feature connection (MFC)
        dataset. This tool modifies field, geometry, time, and file settings
        for a specified MFC dataset.

     INPUTS:
      bdc_dataset (Table View):
          The MFC dataset that will be updated. The options for editing will
          differ depending on the source data (shapefile, delimited file, ORC,
          or parquet file).
      expression {SQL Expression}:
          An expression used to limit the features that will be used in the
          analysis.
      field_properties {Value Table}:
          Specifies the field names and properties that will be
          modified.SHORT-The field will be type short.LONG-The field will be
          type
          longDOUBLE-The field will be type double.FLOAT-The field will be type
          float.STRING-The field will be type string.DATE-The field will be type
          date.BLOB-The field will be type BLOB.BIG_INTEGER-The field will be
          type big integer.Specifies whether fields will be visible or
          hidden.TRUE-The fields will be visible and available for use in
          geoprocessing
          tools. This is the default.FALSE-The fields will be hidden and cannot
          be used as input to
          geoprocessing tools.
      geometry_type {String}:
          Specifies the type of geometry that will be used to spatially
          represent the dataset. The geometry cannot be modified for shapefile-
          sourced datasets.POINT-The geometry type will be point.LINE-The
          geometry type will be
          polyline.POLYGON-The geometry type will be polygon.NONE-No geometry
          type is specified.
      spatial_reference {String}:
          The WKID value or WKT string that will be used for the spatial
          reference of the dataset. The default is WKID 4326 (WGS84). The
          spatial reference cannot be modified for shapefile-sourced data.
      geometry_format_type {String}:
          Specifies how the geometry will be formatted. The geometry cannot be
          modified for shapefile-sourced data.XYZ-Two or more fields will
          represent x, y, and optionally z.WKT-The
          geometry will be represented by a single field in a well-known
          text field.WKB-The geometry will be represented by a single field in a
          well-known
          binary field.GEOJSON-The geometry will be represented by a single
          field in GeoJSON
          format.ESRIJSON-The geometry will be represented by a single field in
          EsriJSON format.ESRISHAPE-The geometry will be represented by a single
          field in
          EsriShape format.
      geometry_field {String}:
          A single field used to represent the geometry. This field is used when
          the geometry format is WKT, WKB, GeoJSON, EsriJSON, or EsriShape.
      x_field {String}:
          The field used to represent the x-location. If more than one field
          represents the x-location, modify the .mfc file manually.
      y_field {String}:
          The field used to represent the y-location. If more than one field
          represents the y-location, modify the .mfc file manually.
      z_field {String}:
          The field used to represent the z-location. If more than one field
          represents the z-location, modify the .mfc file manually.
      time_type {String}:
          Specifies the time type that will be used to temporally represent the
          dataset.INTERVAL-The time type will represent a duration of time with
          a start
          and end time.INSTANT-The time type will represent an instant in
          time.NONE-Time is not enabled.
      time_zone {String}:
          The time zone of the dataset.
      start_time_format {Value Table}:
          The fields used to define the start time and the time formatting.
      end_time_format {Value Table}:
          The fields used to define the end time and the time formatting.
      file_extension {String}:
          The file extension of the source dataset. The parameter value cannot
          be modified.
      field_delimiter {String}:
          The field delimiter used in the source dataset.
      record_terminator {String}:
          The record terminator used in the source dataset.
      quote_character {String}:
          The quote character used in the source dataset.
      has_header_row {Boolean}:
          Specifies whether the source dataset includes a header
          row.HAS_HEADER-The source dataset includes a header row.NO_HEADER-The
          source dataset does not include a header row.
      encoding {String}:
          The type of encoding used by the source dataset. UTF-8 is used by
          default.

        """