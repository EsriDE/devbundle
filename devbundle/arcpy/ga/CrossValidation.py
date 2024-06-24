# Generated documentation for module arcpy.ga


class CrossValidation(object):
    """
    Removes one data location and predicts the associated data using the data at the rest of the locations. The primary use for this tool is to compare the predicted value to the observed value in order to obtain useful information about some of your model parameters.
    """

    @property
    def description(self) -> str:
        return """

        CrossValidation_ga(in_geostat_layer, {out_point_feature_class})

        Removes one data location and predicts the associated data using the
        data at the rest of the locations. The primary use for this tool is to
        compare the predicted value to the observed value in order to obtain
        useful information about some of your model parameters.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          The geostatistical layer to be analyzed.

     OUTPUTS:
      out_point_feature_class {Feature Class}:
          Stores the cross-validation statistics at each location in the
          geostatistical layer.

        """