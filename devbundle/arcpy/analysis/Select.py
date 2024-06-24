# Generated documentation for module arcpy.analysis


class Select(object):
    """
    Extracts features from an input feature class or input feature layer, typically using a select or Structured Query Language (SQL) expression, and stores them in an output feature class.
    """

    @property
    def description(self) -> str:
        return """

        Select_analysis(in_features, out_feature_class, {where_clause})

        Extracts features from an input feature class or input feature layer,
        typically using a select or Structured Query Language (SQL)
        expression, and stores them in an output feature class.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer from which features are selected.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more
          information about SQL syntax, see SQL reference for query expressions
          used in ArcGIS.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created. If no expression is used, it
          contains all input features.

        """