# Generated documentation for module arcpy.management


class CopyFeatures(object):
    """
    Copies features from the input feature class or layer to a new feature class.
    """

    @property
    def description(self) -> str:
        return """

        CopyFeatures_management(in_features, out_feature_class, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

        Copies features from the input feature class or layer to a new feature
        class.

     INPUTS:
      in_features (Feature Layer):
          The features to be copied.
      config_keyword {String}:
          Geodatabase configuration keyword to be applied if the output is a
          geodatabase.
      spatial_grid_1 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          is ignored.
      spatial_grid_2 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          is ignored.
      spatial_grid_3 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          is ignored.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class which will be created and to which the features will
          be copied.

        """