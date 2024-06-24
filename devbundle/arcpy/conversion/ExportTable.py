# Generated documentation for module arcpy.conversion


class ExportTable(object):
    """
    Exports the rows of a table or table view to a new table.
    """

    @property
    def description(self) -> str:
        return """

        ExportTable_conversion(in_table, out_table, {where_clause}, {use_field_alias_as_name}, {field_mapping}, {sort_field;sort_field...})

        Exports the rows of a table or table view to a new table.

     INPUTS:
      in_table (Table View / Raster Layer):
          The input table containing the rows to be exported to a new table.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of records. For more
          information on SQL syntax see the help topic SQL reference for query
          expressions used in ArcGIS.
      use_field_alias_as_name {Boolean}:
          Specifies whether the input's field names or field aliases will be
          used as the output field name.NOT_USE_ALIAS-The input's field names
          will be used as the output field
          names. This is the default.USE_ALIAS-The input's field aliases will be
          used as the output field
          names.
      field_mapping {Field Mappings}:
          The fields that will be transferred to the output dataset with their
          respective properties and source fields. By default, the output
          includes all fields from the input dataset.Use the field map to add,
          delete, rename, and reorder fields, as well
          as change other field properties.The field map can also be used to
          combine values from two or more
          input fields into a single output field.
      sort_field {Value Table}:
          The field or fields whose values will be used to reorder the input
          records and the direction the records will be sorted.ASCENDING-Records
          will be sorted from low value to high
          value.DESCENDING-Records will be sorted from high value to low value.

     OUTPUTS:
      out_table (Table):
          The output table containing the exported rows.If the output location
          is a folder, include an extension such as .csv,
          .txt, or .dbf to export the table to the respective format. If the
          output location is a geodatabase, do not specify an extension.

        """