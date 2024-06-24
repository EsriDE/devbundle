# Generated documentation for module arcpy.aviation


class GenerateChangeoverPoints(object):
    """
    Creates changeover points along routes.
    """

    @property
    def description(self) -> str:
        return """

        GenerateChangeoverPoints_aviation(in_features, target_changeover_features, distance_source_type)

        Creates changeover points along routes.

     INPUTS:
      in_features (Feature Layer):
          The input feature class of routes on which changeover points are
          based. It must contain polyline features.
      target_changeover_features (Feature Layer):
          The point feature class that contains the changeover points. After
          running the tool, new changeover points are added and existing
          changeover points are updated.
      distance_source_type (String):
          Specifies the source of the changeover distance value.ROUTE-The
          changeover distances are stored in the source line
          layer.POINT-The changeover distances are stored in the target point
          layer.

        """