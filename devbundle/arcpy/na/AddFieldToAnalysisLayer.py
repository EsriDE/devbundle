# Generated documentation for module arcpy.na


class AddFieldToAnalysisLayer(object):
    """
    Adds a field to a sublayer of a network analysis layer.
    """

    @property
    def description(self) -> str:
        return """

        AddFieldToAnalysisLayer_na(in_network_analysis_layer, sub_layer, field_name, field_type, {field_precision}, {field_scale}, {field_length}, {field_alias}, {field_is_nullable})

        Adds a field to a sublayer of a network analysis layer.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          The network analysis layer to which the new field will be added.
      sub_layer (String):
          The sublayer of the network analysis layer to which the new field will
          be added.
      field_name (String):
          The name of the field that will be added to the specified sublayer of
          the network analysis layer.
      field_type (String):
          Specifies the field type that will be used in the creation of the new
          field.LONG-The field type will be long. Long fields support whole
          numbers
          between -2,147,483,648 and 2,147,483,647.TEXT-The field type will be
          text. Text fields support a string of
          characters.FLOAT-The field type will be float. Float fields support
          fractional
          numbers between -3.4E38 and 1.2E38.DOUBLE-The field type will be
          double. Double fields support fractional
          numbers between -2.2E308 and 1.8E308.SHORT-The field type will be
          short. Short fields support whole numbers
          between -32,768 and 32,767.DATE-The field type will be date. Date
          fields support date and time
          values.BLOB-The field type will be BLOB. BLOB fields support data
          stored as a
          long sequence of binary numbers. You need a custom loader or viewer or
          a third-party application to load items into a BLOB field or view the
          contents of a BLOB field.GUID-The field type will be GUID. GUID fields
          store registry-style
          strings consisting of 36 characters enclosed in curly brackets.
          BIGINTEGER-The field type will be big integer. Big integer
          fields support whole numbers between -(2) and 2.
          5353TIMEONLY-The field type will be time only. Time only fields
          support
          time values with no date values.DATEONLY-The field type will be date
          only. Date only fields support
          date values with no time values.TIMESTAMPOFFSET-The field type will be
          timestamp offset. Timestamp
          offset fields support a date, time, and offset from a UTC value.
      field_precision {Long}:
          Field Precision
      field_scale {Long}:
          Field Scale
      field_length {Long}:
          The length of the field. This sets the maximum number of allowable
          characters for each record of the field. If no field length is
          provided, a length of 255 will be used.The field length applies only
          to text fields.
      field_alias {String}:
          The alternate name for the field. This name is used to describe
          cryptic field names. This parameter only applies to geodatabases.
      field_is_nullable {Boolean}:
          Specifies whether the field can contain null values. Null values are
          different from zero or empty fields and are only supported for fields
          in a geodatabase.NULLABLE-The field can contain null values. This is
          the
          default.NON_NULLABLE-The field cannot contain null values.

        """