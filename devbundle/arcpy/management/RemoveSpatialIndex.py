# Generated documentation for module arcpy.management


class RemoveSpatialIndex(object):
    """
    Deletes the spatial index from a shapefile or file geodatabase, mobile geodatabase, or an enterprise geodatabase feature class.
    """

    @property
    def description(self) -> str:
        return """

        RemoveSpatialIndex_management(in_features)

        Deletes the spatial index from a shapefile or file geodatabase, mobile
        geodatabase, or an enterprise geodatabase feature class.

     INPUTS:
      in_features (Feature Layer / Mosaic Layer):
          The shapefile or file geodatabase, mobile geodatabase, or an
          enterprise geodatabase feature class from which a spatial index will
          be removed.

        """