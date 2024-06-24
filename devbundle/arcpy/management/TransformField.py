# Generated documentation for module arcpy.management


class TransformField(object):
    """
    Transforms continuous values in one or more fields by applying mathematical functions to each value and changing the shape of the distribution. The transformation methods in the tool include log, square root, Box-Cox, multiplicative inverse, square, exponential, and inverse Box-Cox.
    """

    @property
    def description(self) -> str:
        return """

        TransformField_management(in_table, fields;fields..., {method}, {power}, {shift})

        Transforms continuous values in one or more fields by applying
        mathematical functions to each value and changing the shape of the
        distribution. The transformation methods in the tool include log,
        square root, Box-Cox, multiplicative inverse, square, exponential, and
        inverse Box-Cox.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The input table or feature class containing the fields to be
          transformed. The newly transformed fields are added to the input
          table.
      fields (Value Table):
          The fields containing the values to be transformed. For each field, an
          output field name can be specified. If no output field name is
          provided, the tool creates an output field name using the field name
          and transformation method.
      method {String}:
          Specifies the method that will be used to transform the values
          contained in the specified fields.INVX-The multiplicative inverse
          (1/x) method will be applied to the
          original value (x) in the selected fields.SQRT-The square root method
          will be applied to the original value in
          the selected fields.LOG-The natural logarithmic function, log(x), will
          be applied to the
          original value (x) in the selected fields.BOX-COX-The Box-Cox power
          function will be applied to normally
          distribute the original values in the selected fields. This is the
          default.INV_BOX-COX-The inverse of the Box-Cox transformation will be
          applied
          to the original values in the selected fields.INV_SQRT-The square
          method will be applied to the original values in
          the selected fields. This transformation is the inverse of square
          root.INV_LOG-The exponential function, exp(x), will be applied to the
          original value (x) in the selected fields. This transformation is the
          inverse of log.
      power {Double}:
          The power parameter ( λ) of the Box-Cox and inverse Box-Cox
          transformations. For the Box-Cox transformation, if no value is
          provided, an optimal value will be determined using maximum likelihood
          estimation (MLE). For the inverse Box-Cox transformation, a value must
          be provided. 1
      shift {Double}:
          The value that will be used to shift the data (a constant value is
          added). No shift is applied if 0 is specified.For log, Box-Cox, and
          square root transformations, a default shift
          value will be added before the transformation if there are negative or
          zero values.For exponential (inverse log), inverse Box-Cox, and square
          (inverse
          square root) transformations, no shift is applied by default. If a
          shift value is provided, the value is subtracted after the
          transformation is applied. This allows you to use the same shift value
          for transformations and their associated inverses.

        """