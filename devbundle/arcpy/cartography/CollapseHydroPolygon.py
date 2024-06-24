# Generated documentation for module arcpy.cartography


class CollapseHydroPolygon(object):
    """
    Collapses or partially collapses hydro polygons to a centerline based on a collapse width.
    """

    @property
    def description(self) -> str:
        return """

        CollapseHydroPolygon_cartography(in_features;in_features..., out_line_feature_class, {merge_adjacent_input_polygons}, {connecting_features;connecting_features...}, {collapse_width}, {collapse_width_tolerance}, {minimum_length}, {taper_length_percentage}, {out_poly_feature_class})

        Collapses or partially collapses hydro polygons to a centerline based
        on a collapse width.

     INPUTS:
      in_features (Feature Layer):
          One or more feature layers containing hydro polygons.
      merge_adjacent_input_polygons {Boolean}:
          Specifies whether adjacent input polygons will be merged before
          calculating the centerlines.MERGE_ADJACENT-Input hydro polygons will
          be merged before calculating
          the centerlines. This is the default.NO_MERGE-Centerlines will be
          calculated from input hydro polygons that
          are not merged.
      connecting_features {Feature Layer}:
          Input hydro line features that connect to the input hydro polygons to
          be collapsed. Line features will be created to maintain these
          connections.
      collapse_width {Linear Unit}:
          The threshold width of an input hydro polygon to be considered for
          collapse. All polygons below the specified width will be collapsed.
          The default value is 0, which will collapse all features.
      collapse_width_tolerance {Double}:
          A percentage tolerance within which features will be analyzed and the
          surrounding context will be considered when determining whether to
          collapse a feature. This is to minimize oscillations within the
          collapse. The default value is 20 percent. This parameter is applied
          only when the collapse_width parameter value is specified.
      minimum_length {Linear Unit}:
          The minimum length required for a polygon to be retained in the output
          polygon feature class. The minimum length is based on the length of
          the centerline created for the polygon. If the centerline of a polygon
          is longer than the collapse width but shorter than the minimum length,
          the polygon will not be included in the output polygon feature class.
          The default value is 0. This parameter is applied only when the
          collapse_width parameter value is specified.
      taper_length_percentage {Double}:
          The length that connections between polygons in the output polygon
          feature class and the output line feature class will be tapered. This
          parameter specifies the length of the tapering as a percentage of the
          width at the connection location. A taper length percentage value of 0
          will result in no tapering. The default value is 50. This parameter is
          applied only when the collapse_width parameter value is specified.

     OUTPUTS:
      out_line_feature_class (Feature Class):
          The line feature class containing the centerlines of the
          collapsed polygons. It contains centerlines of all input polygons
          including those that are not collapsed. This feature class has
          aattribute that specifies whether the centerline feature represents a
          collapsed polygon. COLLAPSED
      out_poly_feature_class {Feature Class}:
          The polygon feature class containing the portions of the input hydro
          polygons that are not collapsed. This parameter is applied only when
          the collapse_width parameter value is specified.

        """