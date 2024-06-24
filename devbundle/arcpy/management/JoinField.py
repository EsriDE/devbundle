# Generated documentation for module arcpy.management


class JoinField(object):
    """
    Permanently joins the contents of a table to another table based on a common attribute field. The input table is updated to contain the fields from the join table. You can select which fields from the join table will be added to the input table.
    """

    @property
    def description(self) -> str:
        return """

        JoinField_management(in_data, in_field, join_table, join_field, {fields;fields...}, {fm_option}, {field_mapping}, {index_join_fields})

        Permanently joins the contents of a table to another table based on a
        common attribute field. The input table is updated to contain the
        fields from the join table. You can select which fields from the join
        table will be added to the input table.

     INPUTS:
      in_data (Table View / Raster Layer / Mosaic Layer):
          The table or feature class to which the join table will be joined.
      in_field (Field):
          The field in the input table on which the join will be based.
      join_table (Table View / Raster Layer / Mosaic Layer):
          The table that will be joined to the input table.
      join_field (Field):
          The field in the join table that contains the values on which the join
          will be based.
      fields {Field}:
          The fields from the join table that will be transferred to the input
          table based on a join between the input table and the join table.
      fm_option {String}:
          Specifies how joining fields and field types will be transferred to
          the output.NOT_USE_FM-Fields and field types from the joined table
          will be
          transferred to the output. This is the default.USE_FM-The transfer of
          fields and field types from the joined table to
          the output will be controlled by the field_mapping parameter.
      field_mapping {Field Mappings}:
          The fields that will be joined to the input table with their
          respective properties and source fields. All fields from the join
          table will be included by default.Use the field map to add, delete,
          rename, and reorder fields, as well
          as change other field properties.The field map can be used to combine
          values from two or more input
          fields into a single output field.In Python, use the FieldMappings
          class to define this parameter.
      index_join_fields {String}:
          Specifies whether attribute indexes will be added or replaced for the
          input field and join field.NO_INDEXES-Attribute indexes will not be
          added. This is the
          default.NEW_INDEXES-An attribute index will be added for any field
          that does
          not have an index. Existing attribute indexes will be
          retained.REPLACE_INDEXES-An attribute index will be added for any
          field that
          does not have an index. Existing attribute indexes will be replaced.

        """