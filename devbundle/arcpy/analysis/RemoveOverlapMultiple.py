# Generated documentation for module arcpy.analysis


class RemoveOverlapMultiple(object):
    """
    Removes overlap between polygons contained in multiple input layers.
    """

    @property
    def description(self) -> str:
        return """

        RemoveOverlapMultiple_analysis(in_features;in_features..., out_feature_class, {method}, {join_attributes})

        Removes overlap between polygons contained in multiple input layers.

     INPUTS:
      in_features (Value Table):
          The input features containing the overlapping polygons.
      method {String}:
          Specifies how the overlap between polygons will be
          removed.CENTER_LINE-Overlap will be removed by creating a border that
          evenly
          distributes the overlapping area between polygons. This is the
          simplest method. This is the default.THIESSEN-Overlap will be removed
          using straight lines to divide the
          area of intersection. This method uses a series of geometric functions
          to create nonoverlapping trade areas.GRID-Overlap will be removed by
          creating a grid of parallel lines used
          to define a natural division between polygons.
      join_attributes {String}:
          Specifies the attributes of the input layers that will be transferred
          to the output.ALL-All attributes from the input features will be
          transferred to the
          output feature class. This is the default.NO_FID-All attributes from
          the input features, except the FID field,
          will be transferred to the output feature class.ONLY_FID-Only the FID
          field from the input features will be
          transferred to the output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the new polygon features.

        """