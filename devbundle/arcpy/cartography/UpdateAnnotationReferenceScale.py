# Generated documentation for module arcpy.cartography


class UpdateAnnotationReferenceScale(object):
    """
    Updates the reference scale of an existing annotation or dimension feature class.
    """

    @property
    def description(self) -> str:
        return """

        UpdateAnnotationReferenceScale_cartography(in_anno_features, reference_scale)

        Updates the reference scale of an existing annotation or dimension
        feature class.

     INPUTS:
      in_anno_features (Annotation Layer / Dimension Layer):
          The input annotation or dimension features.
      reference_scale (Double):
          The feature class reference scale that will be updated.

        """