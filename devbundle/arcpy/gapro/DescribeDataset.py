# Generated documentation for module arcpy.gapro


class DescribeDataset(object):
    """
    Summarizes features into calculated field statistics, sample features, and extent boundaries.
    """

    @property
    def description(self) -> str:
        return """

        DescribeDataset_gapro(input_layer, output, {sample_features}, {sample_layer}, {extent_layer})

        Summarizes features into calculated field statistics, sample features,
        and extent boundaries.

     INPUTS:
      input_layer (Table View):
          The point, line, polygon, or tabular features to be described.
      sample_features {Long}:
          The number of features that will be included in the output sample
          layer. No sample is returned if you select 0 features or don't provide
          a number. By default, no sample layer is returned.

     OUTPUTS:
      output (Table):
          A new table with the summary information.
      sample_layer {Table / Feature Class}:
          A new feature class with a sample of the input data.
      extent_layer {Feature Class}:
          A new feature class with the spatial and temporal extent of the input
          data.

        """