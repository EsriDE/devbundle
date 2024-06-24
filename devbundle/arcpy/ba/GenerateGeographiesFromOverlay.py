# Generated documentation for module arcpy.ba


class GenerateGeographiesFromOverlay(object):
    """
    Generates trade areas from the features of an input standard geography level that has a specified spatial relationship with the input.
    """

    @property
    def description(self) -> str:
        return """

        GenerateGeographiesFromOverlay_ba(geography_level, in_features, id_field, out_feature_class, {overlap_type}, {ratios})

        Generates trade areas from the features of an input standard geography
        level that has a specified spatial relationship with the input.

     INPUTS:
      geography_level (String):
          The geography level that will be used to define the trade area.
      in_features (Feature Layer):
          The features used to extract the standard geography level features by
          the specified spatial relationship. It can be either all features from
          the layer or only those selected once a selection is available.
      id_field (Field):
          The field used to identify the input_features parameter-for example,
          the IDs of drive time polygons.
      overlap_type {String}:
          Specifies how the subgeography will be selected from the boundary
          layer.INTERSECT-If any of the subgeography features touch or intersect
          the
          boundary layer, they will be included in the output layer. This is the
          default.CENTROID_WITHIN-If the centroids of any of the subgeography
          features
          are contained within the boundary layer, they will be included in the
          output layer.COMPLETELY_WITHIN-Only the features of the subgeography
          layer that are
          completely contained within the boundary layer will be included in the
          output layer.
      ratios {String}:
          Specifies the ratios to be calculated.NO_RATIOS-No ratios will be
          implemented. This is the
          default.AREA_ONLY-Only the ratios within the portion (area) of the
          standard
          geography level that intersects an input feature will be
          implemented.ALL_RATIOS-All available ratios will be implemented. This
          option is
          not available when using online data.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature containing the trade area.

        """