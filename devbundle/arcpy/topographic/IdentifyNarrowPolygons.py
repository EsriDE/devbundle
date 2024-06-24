# Generated documentation for module arcpy.topographic


class IdentifyNarrowPolygons(object):
    """
    Splits a polygon based on its width and classifies each portion as narrow or wide based on its width and length.
    """

    @property
    def description(self) -> str:
        return """

        IdentifyNarrowPolygons_topographic(in_features, out_feature_class, min_width, min_length, {taper_length}, {connecting_features;connecting_features...})

        Splits a polygon based on its width and classifies each portion as
        narrow or wide based on its width and length.

     INPUTS:
      in_features (Feature Layer):
          The features to be split.
      min_width (Linear Unit):
          The width used to split and classify polygons as narrow or
          wide. Polygons will be split at any location where the edge-to-edge
          distance is equal to the. Minimum Width
      min_length (Linear Unit):
          The length used to classify the split polygons as short or long.
      taper_length {Linear Unit}:
          The distance the end of the split feature will extend to provide a
          more natural break.
      connecting_features {Feature Layer}:
          The features that will be used to refine the tapering of wide areas.
          The polygons will be tapered toward the touch point or the shared
          boundary of a connecting feature.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the results.

        """