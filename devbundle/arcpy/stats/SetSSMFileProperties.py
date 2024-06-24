# Generated documentation for module arcpy.stats


class SetSSMFileProperties(object):
    """
    Adds descriptions and units to the variables stored in a spatial statistics model file.
    """

    @property
    def description(self) -> str:
        return """

        SetSSMFileProperties_stats(input_model, {variable_predict;variable_predict...}, {explanatory_variables;explanatory_variables...}, {distance_features;distance_features...}, {explanatory_rasters;explanatory_rasters...})

        Adds descriptions and units to the variables stored in a spatial
        statistics model file.

     INPUTS:
      input_model (File):
          The spatial statistics model file.
      variable_predict {Value Table}:
          The name, description, and unit of the variable that will be predicted
          at new locations.
      explanatory_variables {Value Table}:
          The name, description, and unit of the explanatory variables that will
          be used to train the input model.
      distance_features {Value Table}:
          The name, description, and unit of the explanatory training distance
          features that will be used to train the input model.
      explanatory_rasters {Value Table}:
          The name, description, and unit of the explanatory training rasters
          that will be used to train the input model.

        """