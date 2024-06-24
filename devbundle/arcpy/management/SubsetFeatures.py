# Generated documentation for module arcpy.management


class SubsetFeatures(object):
    """
    Divides the records of a feature class or table into two subsets: one subset to be used as training data, and one subset to be used as test features to compare and validate the output surface.
    """

    @property
    def description(self) -> str:
        return """

        SubsetFeatures_management(in_features, out_training_feature_class, {out_test_feature_class}, {size_of_training_dataset}, {subset_size_units})

        Divides the records of a feature class or table into two subsets: one
        subset to be used as training data, and one subset to be used as test
        features to compare and validate the output surface.

     INPUTS:
      in_features (Table View):
          The features or table from which subsets will be created.
      size_of_training_dataset {Double}:
          The size of the output training feature class, entered either as a
          percentage of the input features or as an absolute number of features.
      subset_size_units {Boolean}:
          Specifies whether the subset size value will be used as a percentage
          of the input features or as an absolute number of
          features.PERCENTAGE_OF_INPUT-The subset size will be used as a
          percentage of
          the input features that will be in the training
          dataset.ABSOLUTE_VALUE-The subset size will be used as the number of
          features
          that will be in the training dataset.

     OUTPUTS:
      out_training_feature_class (Feature Class / Table):
          The subset of training features that will be created.
      out_test_feature_class {Feature Class / Table}:
          The subset of test features that will be created.

        """