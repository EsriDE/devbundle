# Generated documentation for module arcpy.na


class UpdateByGeometry(object):
    """
    Updates all the edge references in the turn feature class using the geometry of the turn features. This tool is useful when the IDs listed for the turn can no longer find the edges participating in the turn due to edits to the underlying edges.
    """

    @property
    def description(self) -> str:
        return """

        UpdateByGeometry_na(in_turn_features)

        Updates all the edge references in the turn feature class using the
        geometry of the turn features. This tool is useful when the IDs listed
        for the turn can no longer find the edges participating in the turn
        due to edits to the underlying edges.

     INPUTS:
      in_turn_features (Feature Layer):
          The turn feature class to be updated.

        """