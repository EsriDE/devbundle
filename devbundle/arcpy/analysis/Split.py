# Generated documentation for module arcpy.analysis


class Split(object):
    """
    Splits an input with overlaying features to create a subset of output feature classes.
    """

    @property
    def description(self) -> str:
        return """

        Split_analysis(in_features, split_features, split_field, out_workspace, {cluster_tolerance})

        Splits an input with overlaying features to create a subset of output
        feature classes.

     INPUTS:
      in_features (Feature Layer):
          The features to be split.
      split_features (Feature Layer):
          Polygon features containing a tabular field whose unique values are
          used to split the input features and provide the output feature
          classes' names.
      split_field (Field):
          The character field used to split the input features. This field's
          values identify the split features used to create each output feature
          class. The split field's unique values provide the names of the output
          feature classes.
      out_workspace (Workspace / Feature Dataset):
          The existing workspace where the output feature classes are stored.
      cluster_tolerance {Linear Unit}:
          The minimum distance separating all feature coordinates (nodes and
          vertices) as well as the distance a coordinate can move in x or y (or
          both). Set the value higher for data that has less coordinate accuracy
          and lower for datasets with extremely high accuracy.Changing this
          parameter's value may cause failure or unexpected
          results. It is recommended that you do not modify this parameter. It
          has been removed from view on the tool dialog box. By default, the
          input feature class's spatial reference x,y tolerance property is
          used.

        """