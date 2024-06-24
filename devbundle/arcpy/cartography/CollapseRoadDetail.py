# Generated documentation for module arcpy.cartography


class CollapseRoadDetail(object):
    """
    Collapses small, open configurations of road segments that interrupt the general trend of a road network, such as traffic circles, and replaces them with a simplified depiction.
    """

    @property
    def description(self) -> str:
        return """

        CollapseRoadDetail_cartography(in_features, collapse_distance, output_feature_class, {locking_field})

        Collapses small, open configurations of road segments that interrupt
        the general trend of a road network, such as traffic circles, and
        replaces them with a simplified depiction.

     INPUTS:
      in_features (Feature Layer):
          The input features containing small enclosed road details, such as
          traffic circles, to be collapsed.
      collapse_distance (Linear Unit):
          The diameter of, or distance across, the road detail that will be
          considered for collapse.
      locking_field {Field}:
          The field that contains locking information for the features. The data
          type must be short or long integer. A value of 1 indicates that a
          feature will not be collapsed.

     OUTPUTS:
      output_feature_class (Feature Class):
          The output feature class containing the collapsed features-features
          that were modified to accommodate the collapse-and all unaffected
          features.

        """