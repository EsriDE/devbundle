# Generated documentation for module arcpy.cartography


class CreateUnderpass(object):
    """
    Creates bridge parapets and polygon masks at line intersections to indicate underpasses.
    """

    @property
    def description(self) -> str:
        return """

        CreateUnderpass_cartography(in_above_features, in_below_features, margin_along, margin_across, out_underpass_feature_class, out_mask_relationship_class, {where_clause}, {out_decoration_feature_class}, {wing_type}, {wing_tick_length})

        Creates bridge parapets and polygon masks at line intersections to
        indicate underpasses.

     INPUTS:
      in_above_features (Layer):
          The input line feature layer containing lines that intersect-and will
          be symbolized as passing above-lines in the in_below_features
          parameter value.
      in_below_features (Layer):
          The input line feature layer containing lines that intersect-and will
          be symbolized as passing below-lines in the in_above_features
          parameter value. These features will be masked by the polygons created
          in the out_underpass_feature_class parameter value.
      margin_along (Linear Unit):
          The length of the mask polygons along the in_above_features parameter
          value, which is the distance in page units that the mask will extend
          beyond the width of the stroke symbol of the in_below_features
          parameter value. This parameter value must be greater than or equal to
          zero. Choose a page unit (points, millimeters, and so on) for the
          margin; the default is points.
      margin_across (Linear Unit):
          The width of the mask polygons across the in_above_features parameter
          value, which is the distance in page units that the mask will extend
          beyond the width of the stroke symbol of the in_above_features
          parameter value. This parameter value must be greater than or equal to
          zero. Choose a page unit (points, millimeters, and so on) for the
          margin; the default is points.
      where_clause {SQL Expression}:
          An SQL expression used to select a subset of features from the
          in_above_features parameter value.Use quotation marks for field names,
          for example, "MY_FIELD".See SQL reference for query expressions used
          in ArcGIS for more
          information about SQL syntax.
      wing_type {String}:
          Specifies the wing style that will be used for the parapet
          features.ANGLED-The wing tick of the parapet will be angled between
          the
          in_above_features parameter value and the in_below_features parameter
          value. This is the default.PARALLEL-The wing tick of the underpass
          wing will be parallel to the
          in_below_features parameter value.NONE-No wing ticks will be created
          on the parapets.
      wing_tick_length {Linear Unit}:
          The length of the parapet wings in page units. The length must be
          greater than or equal to zero; the default length is 1. Choose a page
          unit (points, millimeters, and so on) for the length; the default is
          points. This parameter does not apply when the wing_type parameter is
          set to NONE.

     OUTPUTS:
      out_underpass_feature_class (Feature Class):
          The output feature class that will be created to store polygons to
          mask the in_below_features parameter value.
      out_mask_relationship_class (Relationship Class):
          The output relationship class that will be created to store links
          between underpass mask polygons and the lines of the in_below_features
          parameter value.
      out_decoration_feature_class {Feature Class}:
          The output line feature class that will be created to store parapet
          features.

        """