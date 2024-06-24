# Generated documentation for module arcpy.cartography


class SimplifySharedEdges(object):
    """
    Simplifies the edges of input features while maintaining the topological relationship with edges shared with other features.
    """

    @property
    def description(self) -> str:
        return """

        SimplifySharedEdges_cartography(in_features;in_features..., algorithm, tolerance, {shared_edge_features;shared_edge_features...}, {minimum_area}, {in_barriers;in_barriers...})

        Simplifies the edges of input features while maintaining the
        topological relationship with edges shared with other features.

     INPUTS:
      in_features (Feature Layer):
          The lines or polygons to be simplified.
      algorithm (String):
          Specifies the simplification algorithm.POINT_REMOVE-Retains critical
          points that preserve the essential shape
          of a polygon outline and removes all other points (Douglas-Peucker).
          This is the default.BEND_SIMPLIFY-Retains the critical bends and
          removes extraneous bends
          from a line (Wang-Müller).WEIGHTED_AREA-Retains vertices that form
          triangles of effective area
          that have been weighted by triangle shape (Zhou-Jones).EFFECTIVE_AREA-
          Retains vertices that form triangles of effective area
          (Visvalingam-Whyatt).
      tolerance (Linear Unit):
          Determines the degree of simplification. If a unit is not specified,
          the units of the input will be used.For the POINT_REMOVE algorithm,
          the tolerance is the maximum allowable
          perpendicular distance between each vertex and the new line
          created.For the BEND_SIMPLIFY algorithm, the tolerance is the diameter
          of a
          circle that approximates a significant bend.For the WEIGHTED_AREA
          algorithm, the square of the tolerance is the
          area of a significant triangle defined by three adjacent vertices. The
          further a triangle deviates from equilateral, the higher weight it is
          given, and the less likely it is to be removed.For the EFFECTIVE_AREA
          algorithm, the square of the tolerance is the
          area of a significant triangle defined by three adjacent vertices.
      shared_edge_features {Feature Layer}:
          Line or polygon features that will be simplified along edges shared
          with input features. Other edges are not simplified.
      minimum_area {Areal Unit}:
          The minimum area for a polygon to be retained. The default value is
          zero, which will retain all polygons. A unit can be specified; if no
          unit is specified, the unit of the input will be used. This parameter
          is available only when at least one of the inputs is a polygon feature
          class.
      in_barriers {Feature Layer}:
          Point, line, or polygon features that act as barriers for the
          simplification. The simplified features will not touch or cross
          barrier features.

        """