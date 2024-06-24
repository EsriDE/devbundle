# Generated documentation for module arcpy.management


class AlterField(object):
    """
    Renames fields and field aliases or alters field properties.
    """

    @property
    def description(self) -> str:
        return """

        AlterField_management(in_table, field, {new_field_name}, {new_field_alias}, {field_type}, {field_length}, {field_is_nullable}, {clear_field_alias})

        Renames fields and field aliases or alters field properties.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The input geodatabase table or feature class that contains the field
          that will be altered.
      field (Field):
          The name of the field that will be altered. If the field is a required
          field, only the field alias will be altered.
      new_field_name {String}:
          The new name for the field.
      new_field_alias {String}:
          The new field alias for the field.
      field_type {String}:
          Specifies the new field type for the field. This parameter is only
          applicable if the input table is empty (does not contain
          records).SHORT-The field type will be short. Short fields support
          whole numbers
          between -32,768 and 32,767.LONG-The field type will be long. Long
          fields support whole numbers
          between -2,147,483,648 and 2,147,483,647. BIGINTEGER-The field
          type will be big integer. Big integer
          fields support whole numbers between -(2) and 2. 5353FLOAT-The
          field type will be float. Float fields support fractional
          numbers between -3.4E38 and 1.2E38.DOUBLE-The field type will be
          double. Double fields support fractional
          numbers between -2.2E308 and 1.8E308.TEXT-The field type will be text.
          Text fields support a string of
          characters.DATE-The field type will be date. Date fields support date
          and time
          values.DATEONLY-The field type will be date only. Date only fields
          support
          date values with no time values.TIMEONLY-The field type will be time
          only. Time only fields support
          time values with no date values.TIMESTAMPOFFSET-The field type will be
          timestamp offset. Timestamp
          offset fields support a date, time, and offset from a UTC
          value.BLOB-The field type will be BLOB. BLOB fields support data
          stored as a
          long sequence of binary numbers. You need a custom loader or viewer or
          a third-party application to load items into a BLOB field or view the
          contents of a BLOB field.GUID-The field type will be GUID. GUID fields
          store registry-style
          strings consisting of 36 characters enclosed in curly brackets.RASTER-
          The field type will be raster. Raster fields can store raster
          data in or alongside the geodatabase. All ArcGIS software-supported
          raster dataset formats can be stored, but it is recommended that only
          small images be used.
      field_length {Long}:
          The new length of the field. This sets the maximum number of allowable
          characters for each record of the field. This parameter is only
          applicable to fields of type TEXT or BLOB. If the table is empty, the
          field length can be increased or decreased. If the table is not empty,
          the length can only be increased from the current value.
      field_is_nullable {Boolean}:
          Specifies whether the field can contain null values. Null values are
          only supported for fields in a geodatabase. This parameter is only
          applicable if the input table is empty (does not contain
          records).NULLABLE-The field can contain null values. This is the
          default.NON_NULLABLE-The field cannot contain null values.
      clear_field_alias {Boolean}:
          Specifies whether the alias for the input field will be cleared. The
          new_field_alias parameter must be empty to clear the alias of the
          field.CLEAR_ALIAS-The field alias will be cleared (set to
          null).DO_NOT_CLEAR-The field alias will not be cleared. This is the
          default.

        """