# Generated documentation for module arcpy.stats


class ConvertSSPopup(object):
    """
    Prepares interactive pop-up charts for web display by saving them as image attachments to a feature class.
    """

    @property
    def description(self) -> str:
        return """

        ConvertSSPopup_stats(in_features, out_feature_class, {img_width}, {img_height}, {rotate_x_axis_labels})

        Prepares interactive pop-up charts for web display by saving them as
        image attachments to a feature class.

     INPUTS:
      in_features (Feature Layer):
          The feature class that contains thefield with the HTML code to
          create a pop-up chart. The feature class must have a 32 bit ObjectID -
          64 bit Object IDs are not supported. HTML_CHART
      img_width {Long}:
          The width, in pixels, of each image attachment.
      img_height {Long}:
          The height, in pixels, of each image attachment.
      rotate_x_axis_labels {Boolean}:
          Specifies whether the x-axis labels will be rotated.ROTATE-The x-axis
          labels will be rotated 20 degrees.NO_ROTATE-The
          x-axis labels will not be rotated. This is the default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class that will contain the pop-up chart of each
          feature saved as an image attachment.

        """