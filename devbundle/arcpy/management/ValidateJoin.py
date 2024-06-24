# Generated documentation for module arcpy.management


class ValidateJoin(object):
    """
    Validates a join between two layers or tables to determine if the layers or tables have valid field names and Object ID fields, if the join produces matching records, if the join is a one-to-one or one-to- many join, and other properties of the join.
    """

    @property
    def description(self) -> str:
        return """

        ValidateJoin_management(in_layer_or_view, in_field, join_table, join_field, {output_msg})

        Validates a join between two layers or tables to determine if the
        layers or tables have valid field names and Object ID fields, if the
        join produces matching records, if the join is a one-to-one or one-to-
        many join, and other properties of the join.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Mosaic Layer):
          The layer or table view with the join to the join table that will be
          validated.
      in_field (Field):
          The field in the input layer or table view on which the join will be
          based.
      join_table (Table View / Raster Layer / Mosaic Layer):
          The table or table view with the join to the input layer or table view
          that will be validated.
      join_field (Field):
          The field in the join table that contains the values on which the join
          will be based.

     OUTPUTS:
      output_msg {Table}:
          The output table containing the validation messages in a tabular form.

        """