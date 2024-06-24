# Generated documentation for module arcpy.ia.Functions


class NonMaximumSuppression(object):
    """
    Identifies duplicate features from the output of the Detect Objects Using Deep Learning tool as a postprocessing step and creates a new output with no duplicate features. The Detect Objects Using Deep Learning tool can return more than one bounding box or polygon for the same object, especially as a tiling side effect. If two features overlap more than a given maximum ratio, the feature with the lower confidence value will be removed.
    """

    @property
    def description(self) -> str:
        return """

        NonMaximumSuppression_ia(in_featureclass, confidence_score_field, out_featureclass, {class_value_field}, {max_overlap_ratio})

        Identifies duplicate features from the output of the Detect Objects
        Using Deep Learning tool as a postprocessing step and creates a new
        output with no duplicate features. The Detect Objects Using Deep
        Learning tool can return more than one bounding box or polygon for the
        same object, especially as a tiling side effect. If two features
        overlap more than a given maximum ratio, the feature with the lower
        confidence value will be removed.

     INPUTS:
      in_featureclass (Feature Class / Feature Layer):
          The input feature class or feature layer containing overlapping or
          duplicate features.
      confidence_score_field (Field):
          The field in the feature class that contains the confidence scores as
          output by the object detection method.
      class_value_field {Field}:
          The class value field in the input feature class. If not
          specified, the tool will use the standard class value fieldsand. If
          these fields do not exist, all features will be treated as the same
          object class. ClassvalueValue
      max_overlap_ratio {Double}:
          The maximum overlap ratio for two overlapping features. This is
          defined as the ratio of intersection area over union area. The default
          is 0.

     OUTPUTS:
      out_featureclass (Feature Class):
          The output feature class with the duplicate features removed.

        """