# Generated documentation for module arcpy.ba


class GenerateThresholdRingTradeArea(object):
    """
    Creates a feature class of ring trade areas that expand around point features until the threshold value is reached.
    """

    @property
    def description(self) -> str:
        return """

        GenerateThresholdRingTradeArea_ba(in_features, out_feature_class, threshold_variable, {threshold_values;threshold_values...}, {units}, {id_field}, {input_method}, {expression}, {minimum_step}, {target_percent_diff})

        Creates a feature class of ring trade areas that expand around point
        features until the threshold value is reached.

     INPUTS:
      in_features (Feature Layer):
          The input point feature layer.
      threshold_variable (String):
          The selected Business Analyst dataset variable to which the threshold
          value will be applied.Threshold variables must be numeric. No other
          statistic type is
          supported.
      threshold_values {Double}:
          The threshold variable value that will determine the size of the
          output rings. The rings will expand until they contain the threshold
          value of the selected variable.
      units {String}:
          The distance units that will be used with the threshold values.
      id_field {Field}:
          The ID that uniquely identifies each input point and is included in
          the output as an attribute.
      input_method {String}:
          Specifies the type of value that will be used for each drive
          time.VALUES-A constant value will be used (all trade areas will be the
          same
          size). This is the default.EXPRESSION-The values from a field or an
          expression will be used
          (trade areas can be different sizes).
      expression {SQL Expression}:
          A fields-based expression that will be used to calculate the radii.
      minimum_step {Double}:
          The minimum distance between one threshold area candidate and the next
          as the model approaches the threshold value to prevent infinite
          iterations.
      target_percent_diff {Double}:
          The maximum percentage difference between the target value and
          threshold value that will be used when determining the threshold drive
          time, for example, 5 percent. The default value is 5.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the threshold rings.

        """