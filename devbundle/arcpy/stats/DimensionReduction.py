# Generated documentation for module arcpy.stats


class DimensionReduction(object):
    """
    Reduces the number of dimensions of a set of continuous variables by aggregating the highest possible amount of variance into fewer components using Principal Component Analysis (PCA) or Reduced-Rank Linear Discriminant Analysis (LDA).
    """

    @property
    def description(self) -> str:
        return """

        DimensionReduction_stats(in_table, {output_data}, fields;fields..., {method}, {scale}, {categorical_field}, {min_variance}, {min_components}, {append_fields}, {output_eigenvalues_table}, {output_eigenvectors_table}, {number_of_permutations}, {append_to_input})

        Reduces the number of dimensions of a set of continuous variables by
        aggregating the highest possible amount of variance into fewer
        components using Principal Component Analysis (PCA) or Reduced-Rank
        Linear Discriminant Analysis (LDA).

     INPUTS:
      in_table (Table View):
          The table or features containing the fields with the dimension that
          will be reduced.
      fields (Field):
          The fields representing the data with the dimension that will be
          reduced.
      method {String}:
          Specifies the method that will be used to reduce the dimensions of the
          analysis fields.PCA-The analysis fields will be partitioned into
          components that each
          maintain the maximum proportion of the total variance. This is the
          default.LDA-The analysis fields will be partitioned into components
          that each
          maintain the maximum between-category separability of a categorical
          variable.
      scale {Boolean}:
          Specifies whether the values of each analysis will be scaled to have a
          variance equal to one. This scaling ensures that each analysis field
          is given equal priority in the components. Scaling also removes the
          effect of linear units; for example, the same data measured in meters
          and feet will result in equivalent components. The values of the
          analysis fields will be shifted to have mean zero for both
          options.SCALE_DATA-The values of each analysis field will be scaled to
          have a
          variance equal to one by dividing each value by the standard deviation
          of the analysis field. This is the default.NO_SCALE_DATA-The variance
          of each analysis field will not be scaled.
      categorical_field {Field}:
          The field representing the categorical variable for LDA. The
          components will maintain the maximum amount of information needed to
          classify each input record into these categories.
      min_variance {Double}:
          The minimum percent of total variance of the analysis fields
          that must be maintained in the components. The total variance depends
          on whether the analysis fields were scaled using theparameter(scale in
          Python). Scale Data
      min_components {Long}:
          The minimum number of components.
      append_fields {Boolean}:
          Specifies whether all fields from the input table or features will be
          copied and appended to the output table or feature class. The fields
          provided in the fields parameter will be copied to the output
          regardless of the value of this parameter.APPEND-All fields from the
          input table or features will be copied and
          appended to the output table or feature class.NO_APPEND-Only the
          analysis fields will be included in the output
          table or feature class. This is the default.
      number_of_permutations {Long}:
          The number of permutations that will be used when determining the
          optimal number of components. The default value is 0, which indicates
          that no permutation test will be performed. The provided value must be
          equal to 0, 99, 199, 499, or 999. If any other value is provided, 0
          will be used and no permutation test will be performed.
      append_to_input {Boolean}:
          Specifies whether the component fields will be appended to the input
          dataset or saved to an output table or feature class. If you append
          the fields to the input, the output coordinate system environment will
          be ignored.APPEND_TO_INPUT-The fields containing the components will
          be appended
          to the input features. This option modifies the input
          data.NEW_OUTPUT-An output table or feature class will be created
          containing
          the component fields. This is the default.

     OUTPUTS:
      output_data {Table}:
          The output table or feature class containing the resulting components
          of the dimension reduction.
      output_eigenvalues_table {Table}:
          The output table containing the eigenvalues of each component.
      output_eigenvectors_table {Table}:
          The output table containing the eigenvectors of each component.

        """