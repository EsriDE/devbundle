# Generated documentation for module arcpy.management


class StandardizeField(object):
    """
    Standardizes values in fields by converting them to values that follow a specified scale. Standardization methods include z-score, minimum- maximum, absolute maximum, and robust standardization.
    """

    @property
    def description(self) -> str:
        return """

        StandardizeField_management(in_table, fields;fields..., {method}, {min_value}, {max_value})

        Standardizes values in fields by converting them to values that follow
        a specified scale. Standardization methods include z-score, minimum-
        maximum, absolute maximum, and robust standardization.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The table containing the field with the values to be standardized.
      fields (Value Table):
          The fields containing the values to be standardized. For each field,
          an output field name can be specified. If an output field name is not
          provided, the tool will create an output field name using the field
          name and selected method.
      method {String}:
          Specifies the method to use to standardize the values contained in the
          specified fields.Z-SCORE-The standard score, which is the number of
          standard deviations
          above or below the mean, is used. The calculation is the Z-Score
          formula, which calculates the difference between the value and the
          mean of the values in the column, divided by the standard deviation of
          the values in the column. This is the default.MIN-MAX-The values are
          converted to a scale between the user-specified
          minimum and maximum values.MAXABS-Each value in the column is divided
          by the maximum absolute
          value in the column.ROBUST-A robust variant of the Z-Score formula is
          used to standardize
          the values in the specified fields. This variant uses median and
          interquartile range in place of mean and standard deviation.
      min_value {Double}:
          The value used by the MIN-MAX method of the method parameter to
          specify the minimum value in the scale of the provided output values.
      max_value {Double}:
          The value used by the MIN-MAX method of the method parameter to
          specify the maximum value in the scale of the provided output values.

        """