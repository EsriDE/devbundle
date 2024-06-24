# Generated documentation for module arcpy.sa.Functions


class ExtractByPolygon(object):
    """
    Extracts the cells of a raster based on a polygon by specifying the polygon's vertices.
    """

    @property
    def description(self) -> str:
        return """

        ExtractByPolygon_sa(in_raster, polygons, {extraction_area})

        Extracts the cells of a raster based on a polygon by specifying the
        polygon's vertices.

     INPUTS:
      in_raster (Composite Geodataset):
          The input raster from which cells will be extracted.
      polygons (Point):
          A polygon (or polygons) that defines the area of the input raster to
          be extracted.Each polygon part is a list of vertices defined by Point
          classes. The
          points are specified as x,y coordinate pairs in the same map units as
          the input raster.The form of the object for a single polygon is as
          follows:         [point(x,y), point(x,y), ..., point(x,y), point(x,y]
          1122nn11Optionally, a group of multiple polygons can be specified by
          using a
          Polygon class to define a list of polygon parts. Note that in order to
          do this, all parts must be contiguous, and thus be encompassed by one
          single perimeter shape. The form of the object in this case would be
          in a contiguous list as follows:         [point(x,y), point(x,y), ...,
          point(x,y), point(x,y),
          point(x',y'), point(x',y'), ..., point(x',y'), point(x',y'), ...]
          1122nn111122nn11In all cases, the last coordinate for each polygon
          part should be the
          same as the first in order to close it.
      extraction_area {String}:
          Identifies whether to extract cells inside or outside the input
          polygon.INSIDE-The cells inside the input polygon should be selected
          and
          written to the output raster. All cells outside the polygon will
          receive NoData values on the output raster.OUTSIDE-The cells outside
          the input polygon should be selected and
          written to the output raster. All cells inside the polygon will
          receive NoData.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output raster containing the cell values extracted from the input
          raster.

        """