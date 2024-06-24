# Generated documentation for module arcpy.conversion


class RasterToPolygon(object):
    """
    Converts a raster dataset to polygon features.
    """

    @property
    def description(self) -> str:
        return """

        RasterToPolygon_conversion(in_raster, out_polygon_features, {simplify}, {raster_field}, {create_multipart_features}, {max_vertices_per_feature})

        Converts a raster dataset to polygon features.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster dataset.The raster must be integer type.
      simplify {Boolean}:
          Determines if the output polygons will be smoothed into simpler shapes
          or conform to the input raster's cell edges.SIMPLIFY-The polygons will
          be smoothed into simpler shapes. The
          smoothing is done in such a way that the polygons contain a minimum
          number of segments while remaining as close as possible to the
          original raster cell edges. This is the default.NO_SIMPLIFY-The edge
          of the polygons will conform exactly to the input
          raster's cell edges. With this option, converting the resulting
          polygon feature class back to a raster would produce a raster the same
          as the original.
      raster_field {Field}:
          The field used to assign values from the cells in the input raster to
          the polygons in the output dataset.It can be an integer or a string
          field.
      create_multipart_features {Boolean}:
          Specifies whether the output polygons will consist of single-part or
          multipart features.MULTIPLE_OUTER_PART-Specifies that multipart
          features will be created
          based on polygons that have the same value.SINGLE_OUTER_PART-Specifies
          that individual features will be created
          for each polygon. This is the default.
      max_vertices_per_feature {Long}:
          The vertex limit used to subdivide a polygon into smaller polygons.
          This parameter produces similar output as created by the Dice tool.If
          left empty, the output polygons will not be split. The default is
          empty.

     OUTPUTS:
      out_polygon_features (Feature Class):
          The output feature class that will contain the converted polygons.

        """