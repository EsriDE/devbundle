# Generated documentation for module arcpy.management


class MakeFeatureLayer(object):
    """
    Creates a feature layer from a feature class or layer file. The layer that is created is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved.
    """

    @property
    def description(self) -> str:
        return """

        MakeFeatureLayer_management(in_features, out_layer, {where_clause}, {workspace}, {field_info})

        Creates a feature layer from a feature class or layer file. The layer
        that is created is temporary and will not persist after the session
        ends unless the layer is saved to disk or the map document is saved.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or layer from which the new layer will be
          made. Complex feature classes, such as annotation and dimensions, are
          not valid inputs.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features. For more
          information on SQL syntax see the help topic SQL reference for query
          expressions used in ArcGIS.If the input is a layer with an existing
          definition query and a where
          clause is specified with this parameter, both where clauses will be
          combined with an AND operator for the output layer. For example, if
          the input layer has a where clause of ID > 10 and this parameter is
          set to ID < 20, the resulting layer's where clause will be ID > 10 AND
          ID < 20.
      workspace {Workspace / Feature Dataset}:
          This parameter is not used.
      field_info {Field Info}:
          The fields from the input features that will be included in the output
          layer. You can remove input fields by making them not visible, and you
          can set numeric fields to have a ratio split policy. Renaming fields
          is not supported.

     OUTPUTS:
      out_layer (Feature Layer):
          The name of the feature layer to be created. The layer can be used as
          input to any geoprocessing tool that accepts a feature layer as input.

        """