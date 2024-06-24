# Generated documentation for module arcpy.cartography


class AlignMarkerToStrokeOrFill(object):
    """
    Aligns the marker symbol layers of a point feature class to the nearest stroke or fill symbol layers in a line or polygon feature class within a specified search distance.
    """

    @property
    def description(self) -> str:
        return """

        AlignMarkerToStrokeOrFill_cartography(in_point_features, in_line_or_polygon_features, search_distance, {marker_orientation})

        Aligns the marker symbol layers of a point feature class to the
        nearest stroke or fill symbol layers in a line or polygon feature
        class within a specified search distance.

     INPUTS:
      in_point_features (Layer):
          The input point feature layer containing point symbols to be
          aligned to nearby lines or polygons. Symbols are aligned by storing an
          angle in the attribute connected to the angle property of the marker
          symbol layer. This must be connected to a single field with no
          expression applied. If multiple marker symbol layers in the same point
          symbol have theproperty connected to the same field, thesetting must
          match in each of those marker layers. AngleRotate clockwise
      in_line_or_polygon_features (Layer):
          The input line or polygon feature layer to which the input point
          symbols will be aligned.
      search_distance (Linear Unit):
          The search distance from graphical marker edge to graphical stroke or
          fill edge. A distance greater than or equal to zero must be specified.
      marker_orientation {String}:
          Specifies how the marker symbol layer will be oriented relative to the
          stroke or fill symbol layer's edge.PERPENDICULAR-Marker symbol layers
          will be aligned perpendicularly to
          the stroke or fill edge. This is the default.PARALLEL-Marker symbol
          layers will be aligned parallel to the stroke
          or fill edge.

        """