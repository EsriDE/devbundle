# Generated documentation for module arcpy.management


class MakeRasterLayer(object):
    """
    Creates a raster layer from an input raster dataset or layer file. The layer created by the tool is temporary and will not persist after the session ends unless the layer is saved to disk or the map document is saved.
    """

    @property
    def description(self) -> str:
        return """

        MakeRasterLayer_management(in_raster, out_rasterlayer, {where_clause}, {envelope}, {band_index;band_index...})

        Creates a raster layer from an input raster dataset or layer file. The
        layer created by the tool is temporary and will not persist after the
        session ends unless the layer is saved to disk or the map document is
        saved.

     INPUTS:
      in_raster (Composite Geodataset):
          The path and name of the input raster dataset.You can use a raster
          layer from a GeoPackage as the input. To
          reference a raster within a GeoPackage, type the name of the path,
          followed by the name of the GeoPackage and the name of the raster. For
          example, c:\data\sample.gpkg\raster_tile would be your input raster,
          where sample.gpkg is the name of the GeoPackage and raster_tile is the
          raster dataset within the package.
      where_clause {SQL Expression}:
          Define a query using SQL.
      envelope {Extent}:
          The output extent can be specified by defining the four coordinates or
          by using the extent of an existing layer.MAXOF-The maximum extent of
          all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      band_index {Value Table}:
          The bands that will be exported for the layer. If no bands are
          specified, all the bands will be used in the output.

     OUTPUTS:
      out_rasterlayer (Raster Layer):
          The name of the layer to create.

        """