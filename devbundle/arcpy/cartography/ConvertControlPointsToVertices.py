# Generated documentation for module arcpy.cartography


class ConvertControlPointsToVertices(object):
    """
    Converts control points in a line or polygon feature layer to vertices.
    """

    @property
    def description(self) -> str:
        return """

        ConvertControlPointsToVertices_cartography(in_features)

        Converts control points in a line or polygon feature layer to
        vertices.

     INPUTS:
      in_features (Feature Layer):
          The line or polygon input features containing control point geometry
          that will be converted to vertices.

        """