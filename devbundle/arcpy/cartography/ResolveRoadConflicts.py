# Generated documentation for module arcpy.cartography


class ResolveRoadConflicts(object):
    """
    Resolves graphic conflicts among symbolized road features by adjusting portions of line segments.
    """

    @property
    def description(self) -> str:
        return """

        ResolveRoadConflicts_cartography(in_layers;in_layers..., hierarchy_field, {out_displacement_features})

        Resolves graphic conflicts among symbolized road features by adjusting
        portions of line segments.

     INPUTS:
      in_layers (Layer):
          The input feature layers containing symbolized road features that may
          be in conflict.
      hierarchy_field (String):
          The field that contains hierarchical ranking of feature importance in
          which 1 is very important and larger integers reflect decreasing
          importance. A value of 0 (zero) locks the feature to ensure that it is
          not moved. This field must be present and named the same for all input
          feature classes. The data type must be short or long integer.

     OUTPUTS:
      out_displacement_features {Feature Class}:
          The output polygon features containing the degree and direction of
          road displacement that will be used by the Propagate Displacement tool
          to preserve spatial relationships.

        """