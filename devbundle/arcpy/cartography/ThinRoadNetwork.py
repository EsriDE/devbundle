# Generated documentation for module arcpy.cartography


class ThinRoadNetwork(object):
    """
    Generates a simplified road network that retains connectivity and general character for display at a smaller scale.
    """

    @property
    def description(self) -> str:
        return """

        ThinRoadNetwork_cartography(in_features;in_features..., minimum_length, invisibility_field, hierarchy_field)

        Generates a simplified road network that retains connectivity and
        general character for display at a smaller scale.

     INPUTS:
      in_features (Feature Layer):
          The input linear roads that will be thinned to create a simplified
          collection for display at smaller scales.
      minimum_length (Linear Unit):
          An indication of the shortest road segment that is sensible to display
          at the output scale. This controls the resolution, or density, of the
          resulting road collection. If the units are in points, millimeters,
          centimeters, or inches, the value is considered in page units and the
          reference scale is taken into account.
      invisibility_field (String):
          The field that stores the results of the tool. Features that
          participate in the resulting simplified road collection have a value
          of 0 (zero). Those that are extraneous have a value of 1. A layer
          definition query can be used to display the resulting road collection.
          This field must be present and named the same for each input feature
          class. The data type must be short or long integer.
      hierarchy_field (String):
          The field that contains hierarchical ranking of feature importance in
          which 1 is very important and larger integers reflect decreasing
          importance. A value of 0 forces the feature to remain visible in the
          output collection. This field must be present and named the same for
          each input feature class. The data type must be short or long integer.
          Hierarchy values equal to NULL are not accepted and will produce an
          error.

        """