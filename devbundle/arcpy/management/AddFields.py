# Generated documentation for module arcpy.management


class AddFields(object):
    """
    Adds new fields to a table, feature class, or raster.
    """

    @property
    def description(self) -> str:
        return """

        AddFields_management(in_table, {field_description;field_description...}, {template;template...})

        Adds new fields to a table, feature class, or raster.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The input table where the fields will be added. The fields will be
          added to the existing input table and will not create a new output
          table.Fields can be added to feature classes in geodatabases,
          shapefiles,
          coverages, stand-alone tables, raster catalogs, rasters with attribute
          tables, and layers.
      field_description {Value Table}:
          The fields and their properties that will be added to the input
          table.Field Name-The name of the field that will be added to the input
          table.Field Type-The type of the new field.Field Alias-The alternate
          name for the field. This is used to describe
          cryptic field names. This value only applies to geodatabases.Field
          Length-The length of the field being added. This sets the
          maximum number of allowable characters for each record of the field.
          This option is only applicable to fields of type text. The default
          length is 255.Default Value-The default value of the field.Field
          Domain-The geodatabase domain that will be assigned to the
          field.Available field types are as follows:SHORT-The field type will
          be short. Short fields support whole numbers
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
          strings consisting of 36 characters enclosed in curly
          brackets.RASTER-The field type will be raster. Raster fields can store
          raster
          data in or alongside the geodatabase. All ArcGIS software-supported
          raster dataset formats can be stored, but it is recommended that only
          small images be used.In the field_description parameter with optional
          parameters, use None
          as an empty place holder.
      template {Table View}:
          The feature classes or tables that will be used as a template to
          define the attribute fields to add.Fields from the inputs specified by
          this parameter will be added to
          the in_table value in addition to any fields specified by the
          field_description parameter.

        """