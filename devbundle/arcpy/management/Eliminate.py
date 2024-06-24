# Generated documentation for module arcpy.management


class Eliminate(object):
    """
    Eliminates polygons by merging them with neighboring polygons that have the largest area or the longest shared border. Eliminate is often used to remove small sliver polygons that are the result of overlay operations, such as those performed by Intersect and Union tools.
    """

    @property
    def description(self) -> str:
        return """

        Eliminate_management(in_features, out_feature_class, {selection}, {ex_where_clause}, {ex_features})

        Eliminates polygons by merging them with neighboring polygons that
        have the largest area or the longest shared border. Eliminate is often
        used to remove small sliver polygons that are the result of overlay
        operations, such as those performed by Intersect and Union tools.

     INPUTS:
      in_features (Feature Layer):
          The layer with the polygons that will be merged with neighboring
          polygons.
      selection {Boolean}:
          Specifies whether the selected polygon will be merged with a polygon
          with the longest shared border or the largest area.LENGTH-The selected
          polygon will be merged with the neighboring
          polygon with the longest shared border. This is the default.AREA-The
          selected polygon will be merged with the neighboring polygon
          with the largest area.
      ex_where_clause {SQL Expression}:
          An SQL expression that will be used to identify features that will not
          be altered. For more information on SQL syntax, see the SQL reference
          for elements used in query expressions help topic.
      ex_features {Feature Layer}:
          An input polyline or polygon feature class or layer that defines
          polygon boundaries, or portions thereof, that will not be eliminated.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class to be created.

        """