# Generated documentation for module arcpy.cartography


class SmoothSharedEdges(object):
    """
    Smooths the edges of the input features while maintaining the topological relationship with edges shared with other features.
    """

    @property
    def description(self) -> str:
        return """

        SmoothSharedEdges_cartography(in_features;in_features..., algorithm, tolerance, {shared_edge_features;shared_edge_features...}, {in_barriers;in_barriers...})

        Smooths the edges of the input features while maintaining the
        topological relationship with edges shared with other features.

     INPUTS:
      in_features (Feature Layer):
          The lines or polygons to be smoothed.
      algorithm (String):
          Specifies the smoothing algorithm.PAEK-Calculates a smoothed polygon
          that will not pass through the
          input polygon vertices. It is the acronym for Polynomial Approximation
          with Exponential Kernel. This is the default.BEZIER_INTERPOLATION-Fits
          Bezier curves between vertices. The
          resulting polygons pass through the vertices of the input polygons.
          This algorithm does not require a tolerance. Bezier curves will be
          approximated in the output.
      tolerance (Linear Unit):
          Determines the degree of smoothing. A unit can be specified; if no
          unit is specified, the unit of the input will be used. This is only
          used for the PAEK algorithm. The parameter will not appear on the tool
          dialog box when Bezier interpolation is selected and, in scripting, a
          value of 0 must be used.
      shared_edge_features {Feature Layer}:
          Line or polygon features that will be smoothed along edges shared with
          input features. Other edges are not smoothed.
      in_barriers {Feature Layer}:
          Point, line, or polygon features that act as barriers for smoothing.
          The smoothed features will not touch or cross barrier features.

        """