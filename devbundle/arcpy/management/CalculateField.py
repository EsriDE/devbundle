# Generated documentation for module arcpy.management


class CalculateField(object):
    """
    Calculates the values of a field for a feature class, feature layer, or raster.
    """

    @property
    def description(self) -> str:
        return """

        CalculateField_management(in_table, field, expression, {expression_type}, {code_block}, {field_type}, {enforce_domains})

        Calculates the values of a field for a feature class, feature layer,
        or raster.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The table containing the field that will be updated with the new
          calculation.
      field (Field):
          The field that will be updated with the new calculation.If a field
          with the specified name does not exist in the input table,
          it will be added.
      expression (SQL Expression):
          The simple calculation expression used to create a value that will
          populate the selected rows.
      expression_type {String}:
          Specifies the type of expression that will be used.PYTHON3-The Python
          expression type will be used.ARCADE-The Arcade
          expression type will be used.SQL-The SQL expression type will be
          used.VB-The VBScript expression type will be used.If the input is a
          feature service, the default expression type is SQL.
          For any other type of input, the default expression type is PYTHON3.To
          learn more about Python expressions, see Calculate Field Python
          examples.To learn more about Arcade expressions, see the ArcGIS Arcade
          guide.To learn more about SQL expressions, see Calculate field
          values.SQL expressions support faster calculations for feature
          services and
          enterprise geodatabases. Instead of performing calculations one
          feature or row at a time, a single request is sent to the server or
          database, resulting in significantly faster calculations.Only feature
          services and enterprise geodatabases support SQL
          expressions. For other formats, use Python or Arcade expressions.To
          learn more about VBScript expressions, see Calculate Field VBScript
          examples.
      code_block {String}:
          A block of code that will be used for complex Python or VBScript
          expressions.
      field_type {String}:
          Specifies the field type of the new field. This parameter is only used
          when the field name does not exist in the input table.If the field is
          of type text, the field will have a length of 512,
          unless the input is a shapefile or dBASE file, in which case the
          length will be 254. To adjust the length, use the Alter Field
          tool.SHORT-The field type will be short. Short fields support whole
          numbers
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
          small images be used.
      enforce_domains {Boolean}:
          Specifies whether field domain rules will be
          enforced.ENFORCE_DOMAINS-Field domain rules will be
          enforced.NO_ENFORCE_DOMAINS-Field domain rules will not be enforced.
          This is
          the default.

        """