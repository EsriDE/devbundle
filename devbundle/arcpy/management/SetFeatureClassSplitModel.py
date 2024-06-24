# Generated documentation for module arcpy.management


class SetFeatureClassSplitModel(object):
    """
    Defines the behavior of a split operation on a feature class.
    """

    @property
    def description(self) -> str:
        return """

        SetFeatureClassSplitModel_management(in_feature_class, {split_model})

        Defines the behavior of a split operation on a feature class.

     INPUTS:
      in_feature_class (Polygon|Polyline):
          The feature class on which the split model will be set.
      split_model {String}:
          Specifies the split model that will be applied to the input feature
          class.DELETE_INSERT_INSERT-The original feature will be deleted, and
          both
          parts of the split feature will be inserted as new features with two
          new rows in the table.UPDATE_INSERT-The original feature will be
          updated, becoming the
          largest feature, and the smaller feature will be inserted as a new row
          in the table. This is the default.

        """