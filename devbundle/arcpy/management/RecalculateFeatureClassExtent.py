# Generated documentation for module arcpy.management


class RecalculateFeatureClassExtent(object):
    """
    Recalculates the xy, z, and m extent properties of a feature class based on the features in the feature class.
    """

    @property
    def description(self) -> str:
        return """

        RecalculateFeatureClassExtent_management(in_features, {store_extent})

        Recalculates the xy, z, and m extent properties of a feature class
        based on the features in the feature class.

     INPUTS:
      in_features (Feature Layer):
          The shapefile or geodatabase feature class that will be updated.
      store_extent {Boolean}:
          Specifies whether the extent will be stored for feature classes that
          are not registered. This parameter is only supported when the input
          feature class is an unregistered spatial table in a database or
          enterprise geodatabase.If the input feature class is updated
          frequently, you may choose not
          to store the recalculated extent value. If you choose to store the
          extent, the extent will not be recalculated each time the feature
          class is added to the map.STORE_EXTENT-The extent will be stored for
          the input feature
          class.DO_NOT_STORE_EXTENT-The extent will not be stored for the input
          feature class. This is the default.

        """