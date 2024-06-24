# Generated documentation for module arcpy.cartography


class AnnotateSelectedFeatures(object):
    """
    Creates annotation for the selected features of a layer. The labeling properties defined in the annotation class properties of the specified related annotation feature classes are used.
    """

    @property
    def description(self) -> str:
        return """

        AnnotateSelectedFeatures_cartography(in_map, in_layer, anno_layers;anno_layers..., {generate_unplaced})

        Creates annotation for the selected features of a layer. The labeling
        properties defined in the annotation class properties of the specified
        related annotation feature classes are used.

     INPUTS:
      in_map (Map):
          The input map.
      in_layer (Feature Layer):
          The layer for which the selected features will have annotation
          created.
      anno_layers (Value Table):
          The feature-linked annotation layers and the specified sublayers that
          will have annotation converted into them.
      generate_unplaced {Boolean}:
          Specifies whether to create unplaced annotation from unplaced
          labels.ONLY_PLACED-Annotation will only be created for features that
          are
          currently labeled. This is the default.GENERATE_UNPLACED-Unplaced
          annotation are stored in the annotation
          feature class. The status field for these annotation is set to
          Unplaced.

        """