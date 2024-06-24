# Generated documentation for module arcpy.management


class MakeQueryTable(object):
    """
    Applies an SQL query to a database, and the results are represented in either a layer or table view. The query can be used to join several tables or return a subset of fields or rows from the original data in the database.
    """

    @property
    def description(self) -> str:
        return """

        MakeQueryTable_management(in_table;in_table..., out_table, in_key_field_option, {in_key_field;in_key_field...}, {in_field;in_field...}, {where_clause})

        Applies an SQL query to a database, and the results are represented in
        either a layer or table view. The query can be used to join several
        tables or return a subset of fields or rows from the original data in
        the database.

     INPUTS:
      in_table (Table View / Raster Layer):
          The name of the table or tables to be used in the query. If several
          tables are listed, the where_clause parameter can be used to define
          how they will be joined.The input table can be from a geodatabase or a
          database connection.
      in_key_field_option (String):
          Specifies how anfield will be generated (if at all) for the
          query. Layers and table views in ArcGIS require anfield. Anfield is an
          integer field that uniquely identifies rows in the data being used.
          Object IDObject IDObject IDUSE_KEY_FIELDS-Specified fields in the
          in_key_field parameter will be
          used to uniquely identify a row in the output table. This can be a
          single field or multiple fields, which, when combined, uniquely
          identify a row in the output table. If no fields are specified in the
          key fields list, the ADD VIRTUAL_KEY_FIELD option will be applied.
          ADD_VIRTUAL_KEY_FIELD-If no key fields have been specified,
          anfield that uniquely identifies each row in the output table will be
          generated. Object ID         NO_KEY_FIELD-
          Nofield will be generated.
          Selections will not be supported
          for the table view. Object ID           If there is an
          existingfield, it will be used even if this
          option is chosen. Object ID
      in_key_field {Field}:
          A field or combination of fields that will be used to uniquely
          identify a row in the query. This parameter is used only when the
          in_key_field_option parameter is set to USE_KEY_FIELDS.
      in_field {Value Table}:
          The fields that will be included in the layer or table view.
          If an alias is set for a field, this is the name that appears. If no
          fields are specified, all fields from all tables are included. If
          afield is added to the field list, the result is a layer; otherwise it
          is a table view. Shape
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of records.

     OUTPUTS:
      out_table (Table View / Raster Layer):
          The name of the layer or table view that will be created.

        """