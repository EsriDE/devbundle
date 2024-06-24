# Generated documentation for module arcpy.md


class BuildMultidimensionalInfo(object):
    """
    Generates multidimensional metadata in the mosaic dataset, including information regarding variables and dimensions.
    """

    @property
    def description(self) -> str:
        return """

        BuildMultidimensionalInfo_md(in_mosaic_dataset, {variable_field}, {dimension_fields;dimension_fields...}, {variable_desc_units;variable_desc_units...}, {delete_multidimensional_info})

        Generates multidimensional metadata in the mosaic dataset, including
        information regarding variables and dimensions.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The input multidimensional mosaic dataset.
      variable_field {String}:
          The field in the mosaic dataset that stores the variable names
          and is used to populate a new field named. If all rasters in the
          mosaic dataset represent the same variable, type the name of the
          variable, for example, Temperature. Variable        If thefield
          does not already exist, an existing field or
          string value must be specified. If thefield exists, the tool will
          update the multidimensional information only. VariableVariable
      dimension_fields {Value Table}:
          The fields in the mosaic dataset that store the dimension
          information and are used to populate a new field named.
          Dimensions        If thefield already exists, the tool will update the
          multidimensional information only. Dimensions
      variable_desc_units {Value Table}:
          Specify additional information about thefield. Variable
      delete_multidimensional_info {Boolean}:
          Specifies whether existing multidimensional information will be
          deleted.DELETE_MULTIDIMENSIONAL_INFO-If multidimensional information
          exists in
          the mosaic dataset, it will be
          deleted.NO_DELETE_MULTIDIMENSIONAL_INFO-If multidimensional
          information exists
          in the mosaic dataset, it will not be delete. This is the default.

        """