# Generated documentation for module arcpy.management


class TransposeFields(object):
    """
    Switch data stored in fields or columns to rows in a new table or feature class.
    """

    @property
    def description(self) -> str:
        return """

        TransposeFields_management(in_table, in_field;in_field..., out_table, in_transposed_field_name, in_value_field_name, {attribute_fields;attribute_fields...})

        Switch data stored in fields or columns to rows in a new table or
        feature class.

     INPUTS:
      in_table (Table View):
          The input feature class or table containing data value fields to be
          transposed.
      in_field (Value Table):
          The fields or columns containing data values in the input table that
          need to be transposed. Depending on your needs, you can select
          multiple fields to be
          transposed. The value here defines what the field name will be in the
          output. When not specified, the value is the same as the field name by
          default. However, you can also specify your own value. For example, if
          the field names to be transposed are,, and so on, by default, the
          values for these fields in the output will be the same (,, and so
          forth). However, you can choose to specify your own values such as
          1991 and 1992. Pop1991Pop1992Pop1991Pop1992
      in_transposed_field_name (String):
          The name of the field that will be created to store field names of the
          transposed fields. Any valid field name can be used.
      in_value_field_name (String):
          The name of the field that will be created to store the corresponding
          values of the transposed fields. Any valid field name can be set, as
          long as it does not conflict with existing field names from the input
          table or feature class.
      attribute_fields {Field}:
          Additional attribute fields from the input table to be
          included in the output table. If you want to output a feature class,
          add thefield. Shape

     OUTPUTS:
      out_table (Table):
          The output feature class or table. The output will contain a
          transposed field, a value field, and any number of specified attribute
          fields that need to be inherited from the input table. By
          default the out_table is a table. The output will be a
          feature class when the in_table is a feature class and thefield is
          selected in the attribute_fields parameter. Shape

        """