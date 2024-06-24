# Generated documentation for module arcpy.management


class RemoveIndex(object):
    """
    Deletes an attribute index from an existing table, feature class, shapefile, or attributed relationship class.
    """

    @property
    def description(self) -> str:
        return """

        RemoveIndex_management(in_table, index_name;index_name...)

        Deletes an attribute index from an existing table, feature class,
        shapefile, or attributed relationship class.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The input containing the index or indexes that will be deleted. The
          input can be a table, a feature class, or an attributed relationship
          class.
      index_name (String):
          The name of the index or indexes that will be deleted.

        """