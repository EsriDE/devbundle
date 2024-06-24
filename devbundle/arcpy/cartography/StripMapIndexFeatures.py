# Generated documentation for module arcpy.cartography


class StripMapIndexFeatures(object):
    """
    Creates a series of rectangular polygons, or index features, that follow a single linear feature or a group of linear features. These index features can be used with spatial map series to define pages in a strip map or a set of maps that follow a linear feature. The resulting index features contain attributes that can be used to rotate and orient the map on the page and determine which index features, or pages, are next to the current page (to the left and right or to the top and bottom).
    """

    @property
    def description(self) -> str:
        return """

        StripMapIndexFeatures_cartography(in_features, out_feature_class, {use_page_unit}, {scale}, {length_along_line}, {length_perpendicular_to_line}, {page_orientation}, {overlap_percentage}, {starting_page_number}, {direction_type})

        Creates a series of rectangular polygons, or index features, that
        follow a single linear feature or a group of linear features. These
        index features can be used with spatial map series to define pages in
        a strip map or a set of maps that follow a linear feature. The
        resulting index features contain attributes that can be used to rotate
        and orient the map on the page and determine which index features, or
        pages, are next to the current page (to the left and right or to the
        top and bottom).

     INPUTS:
      in_features (Feature Layer):
          The input polyline features defining the path of the strip map index
          features.
      use_page_unit {Boolean}:
          Specifies whether index feature size input is in page
          units.USEPAGEUNIT-Index polygon height and width are calculated in
          page
          units.NO_USEPAGEUNIT-Index polygon height and width are calculated in
          map
          units. This is the default.
      scale {Long}:
          Map scale must be specified if index feature lengths (along the line
          and perpendicular to the line) are to be calculated in page units. If
          you're using ArcGIS Pro, the default value will be the scale of the
          active data frame; otherwise, the default will be 1.
      length_along_line {Linear Unit}:
          The length of the polygon index feature along the input line feature
          specified in either map or page units. The default value is determined
          by the spatial reference of the input line feature or features. This
          value will be 1/100 of the input feature class extent along the x
          axis.
      length_perpendicular_to_line {Linear Unit}:
          The length of the polygon index feature perpendicular to the input
          line feature specified in either map or page units. The default value
          is determined by the spatial reference of the input line feature or
          features. This value will be one-half the number used for the length
          along the line.
      page_orientation {String}:
          Specifies the orientation of the input line features on the layout
          page.VERTICAL-The direction of the strip map series on the page is top
          to
          bottom.HORIZONTAL-The direction of the strip map series on the page is
          left
          to right. This is the default.
      overlap_percentage {Double}:
          The approximate percentage of geographic overlap between an individual
          map page and its adjoining pages in the series. The default is 10.
      starting_page_number {Long}:
          The page number of the starting page. Each grid index feature is
          assigned a sequential page number beginning with the specified
          starting page number. The default is 1.
      direction_type {String}:
          Specifies the initial direction of the strip maps.WE_NS-If the line's
          directional trend is West to East, the starting
          point will be at the westernmost end of the line, or if the line's
          direction trend is North to South, the starting point will be at the
          northernmost end of the line. This is the default.WE_SN-If the line's
          directional trend is West to East, the starting
          point will be at the westernmost end of the line, or if the line's
          direction trend is South to North, the starting point will be at the
          southernmost end of the line.EW_NS-If the line's directional trend is
          East to West, the starting
          point will be at the easternmost end of the line, or if the line's
          direction trend is North to South, the starting point will be at the
          northernmost end of the line.EW_SN-If the line's directional trend is
          East to West, the starting
          point will be at the easternmost end of the line, or if the line's
          direction trend is South to North, the starting point will be at the
          southernmost end of the line.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class of polygon index features.

        """