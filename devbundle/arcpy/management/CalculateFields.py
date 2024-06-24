# Generated documentation for module arcpy.management


class CalculateFields(object):
    """
    Calculates the values of two or more fields for a feature class, feature layer, or raster.
    """

    @property
    def description(self) -> str:
        return """

        CalculateFields_management(in_table, expression_type, fields;fields..., {code_block}, {enforce_domains})

        Calculates the values of two or more fields for a feature class,
        feature layer, or raster.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The table containing the fields that will be updated with the new
          calculations.
      expression_type (String):
          Specifies the type of expression that will be used.PYTHON3-The Python
          expression type will be used.ARCADE-The Arcade
          expression type will be used.SQL-The SQL expression type will be
          used.VB-The VBScript expression type will be used.If the input is a
          feature service, the default expression type is SQL.
          For any other type of input, the default expression type is PYTHON3.To
          learn more about Python expressions, see Calculate Field Python
          examples.To learn more about Arcade expressions, see the ArcGIS Arcade
          guide.To learn more about SQL expressions, see Calculate field
          values.To learn more about VBScript expressions, see Calculate Field
          VBScript
          examples.
      fields (Value Table):
          The fields that will be calculated, their expressions, and a where
          clause.The optional SQL expression will be used to select a subset of
          records. Only records that match this where clause will be calculated.
          If the where clause is left blank, all records will be calculated. For
          more information about SQL syntax, see SQL reference for query
          expressions used in ArcGIS.
      code_block {String}:
          A block of code that will be used for complex expressions.A function
          cannot be used to return multiple values.
      enforce_domains {Boolean}:
          Specifies whether field domain rules will be
          enforced.ENFORCE_DOMAINS-Field domain rules will be
          enforced.NO_ENFORCE_DOMAINS-Field domain rules will not be enforced.
          This is
          the default.

        """