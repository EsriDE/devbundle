# Generated documentation for module arcpy.intelligence


class GenerateObstacleFeatures(object):
    """
    Converts features with a height field to a 3D obstacle feature and an obstacle restriction buffer for use in evaluating helicopter landing zones.
    """

    @property
    def description(self) -> str:
        return """

        GenerateObstacleFeatures_intelligence(in_features, height_field, out_obstacle_features, out_obstacle_buffers, {clip_features})

        Converts features with a height field to a 3D obstacle feature and an
        obstacle restriction buffer for use in evaluating helicopter landing
        zones.

     INPUTS:
      in_features (Feature Layer):
          The input source features used to create obstacle features.
      height_field (Field):
          A field from the in_features parameter containing height values. The
          field type can be numeric or text. If a text field is used, the field
          values must be numeric.
      clip_features {Feature Layer}:
          An area to clip the out_obstacle_features. Only features within the
          clip_features will be processed.

     OUTPUTS:
      out_obstacle_features (Feature Class):
          The output 3D obstacle features.
      out_obstacle_buffers (Feature Class):
          The output obstacle buffer features

        """