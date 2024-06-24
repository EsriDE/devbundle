# Generated documentation for module arcpy.management


class AddField(object):
    """
    Adds a new field to a table or the table of a feature class or feature layer, as well as to rasters with attribute tables.
    """

    @property
    def description(self) -> str:
        return """

        AddField_management(in_table, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable}, {field_is_required}, {field_domain})

        Adds a new field to a table or the table of a feature class or feature
        layer, as well as to rasters with attribute tables.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The input table where the specified field will be added. The field
          will be added to the existing input table and will not create a new
          output table.Fields can be added to feature classes in geodatabases,
          shapefiles,
          coverages, stand-alone tables, raster catalogs, rasters with attribute
          tables, and layers.
      field_name (String):
          The name of the field that will be added to the input table.
      field_type (String):
          Specifies the field type of the new field.SHORT-The field type will be
          short. Short fields support whole numbers
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
          values.DATEHIGHPRECISION-The field type will be high precision date.
          High
          precision date fields support date and time values with millisecond
          time.DATEONLY-The field type will be date only. Date only fields
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
          small images be used.Although the Field object's type property values
          are not an exact
          match for the keywords used by the Add Field tool's field_type
          parameter, all of the Field object's type values can be used as input
          to this parameter. The different field types are mapped as follows:
          Integer to LONG, String to TEXT, and SmallInteger to SHORT.
      field_precision {Long}:
          The number of digits that can be stored in the field. All digits are
          counted regardless of which side of the decimal they are on.This
          parameter is only applicable to numeric field types.If the input table
          is in a file geodatabase, the field precision value
          will be ignored.
      field_scale {Long}:
          The number of decimal places stored in a field.This parameter is only
          applicable to fields of type float or double.If the input table is in
          a file geodatabase, the field scale value
          will be ignored.
      field_length {Long}:
          The length of the field. This sets the maximum number of allowable
          characters for each record of the field. If no field length is
          provided, a length of 255 will be used.This parameter is only
          applicable to fields of type text.
      field_alias {String}:
          The alternate name for the field. This name is used to describe
          cryptic field names. This parameter only applies to geodatabases.
      field_is_nullable {Boolean}:
          Specifies whether the field can contain null values. Null values are
          different from zero or empty fields and are only supported for fields
          in a geodatabase.NULLABLE-The field can contain null values. This is
          the
          default.NON_NULLABLE-The field cannot contain null values.
      field_is_required {Boolean}:
          Specifies whether the field being created is a required field for the
          table. Required fields are only supported in a
          geodatabase.NON_REQUIRED-The field is not a required field. This is
          the
          default.REQUIRED-The field is a required field. Required fields are
          permanent
          and cannot be deleted.
      field_domain {String}:
          Constrains the values allowed in any particular attribute for a table,
          feature class, or subtype in a geodatabase. You must specify the name
          of an existing domain for it to be applied to the field.

        """