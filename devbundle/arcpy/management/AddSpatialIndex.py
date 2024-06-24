# Generated documentation for module arcpy.management


class AddSpatialIndex(object):
    """
    Adds a spatial index to a shapefile, file geodatabase, mobile geodatabase, or enterprise geodatabase feature class. Use this tool to either add a spatial index to a shapefile or feature class that does not already have one or to re-create an existing spatial index.
    """

    @property
    def description(self) -> str:
        return """

        AddSpatialIndex_management(in_features, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

        Adds a spatial index to a shapefile, file geodatabase, mobile
        geodatabase, or enterprise geodatabase feature class. Use this tool
        to either add a spatial index to a shapefile or feature class that
        does not already have one or to re-create an existing spatial index.

     INPUTS:
      in_features (Feature Layer / Mosaic Layer):
          An enterprise geodatabase feature class, file geodatabase feature
          class, mobile geodatabase feature class, or shapefile to which a
          spatial index is to be added or rebuilt.
      spatial_grid_1 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          will be ignored.
      spatial_grid_2 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          will be ignored.
      spatial_grid_3 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          will be ignored.

        """