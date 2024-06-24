# Generated documentation for module arcpy.cartography


class GridIndexFeatures(object):
    """
    Creates a grid of rectangular polygon features that can be used as an index to specify pages in a spatial map series. A grid can be created that includes only polygon features that intersect another feature layer.
    """

    @property
    def description(self) -> str:
        return """

        GridIndexFeatures_cartography(out_feature_class, {in_features;in_features...}, {intersect_feature}, {use_page_unit}, {scale}, {polygon_width}, {polygon_height}, {origin_coord}, {number_rows}, {number_columns}, {starting_page_number}, {label_from_origin})

        Creates a grid of rectangular polygon features that can be used as an
        index to specify pages in a spatial map series. A grid can be created
        that includes only polygon features that intersect another feature
        layer.

     INPUTS:
      in_features {Feature Layer / Raster Layer}:
          The input features to be used to define the extent of the polygon grid
          that will be created.
      intersect_feature {Boolean}:
          Limits the output grid feature class to areas that intersect input
          feature layers or datasets. The intersection of input features will be
          used to create index features.INTERSECTFEATURE-Limits the output grid
          feature class to areas that
          intersect input feature layers or datasets. When input features are
          specified, this is the default.NO_INTERSECTFEATURE-An output grid
          feature class is created using
          specified coordinates, rows, and columns.
      use_page_unit {Boolean}:
          Specifies whether index polygon size input is in page
          units.USEPAGEUNIT-Index polygon height and width are calculated in
          page
          units.NO_USEPAGEUNIT-Index polygon height and width are calculated in
          map
          units. This is the default.
      scale {Long}:
          The map scale. The scale must be specified if the index polygon height
          and width are to be calculated in page units. If the tool is used
          outside an active ArcGIS Pro session, the default scale value is 1.
      polygon_width {Linear Unit}:
          The width of the index polygon specified in either map or page units.
          If page units are used, the default value is 1 inch. If map units are
          used, the default value is 1 degree.
      polygon_height {Linear Unit}:
          The height of the index polygon specified in either map or page units.
          If page units are used, the default value is 1 inch. If map units are
          used, the default value is 1 degree.
      origin_coord {Point}:
          The coordinate value for the lower left origin of the output grid
          feature class. If input features are specified, the default value is
          determined by the extent of the union of extents for these features.
          If there are no input features specified, the default coordinates are
          0 and 0.
      number_rows {Long}:
          The number of rows to create in the y direction from the point of
          origin. The default is 10.
      number_columns {Long}:
          The number of columns to create in the x direction from the point of
          origin. The default is 10.
      starting_page_number {Long}:
          Each grid index feature is assigned a sequential page number starting
          with a specified starting page number. The default is 1.
      label_from_origin {Boolean}:
          Specifies where page numbers (labels) begin.LABELFROMORIGIN-Page
          numbers (labels) begin with the polygon feature
          in the lower left corner of the output grid.NO_LABELFROMORIGIN-Page
          numbers (labels) begin with the polygon
          feature in the upper left corner of the output grid. This is the
          default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The resulting feature class of polygon index features.The coordinate
          system of the output feature class is determined in the
          following order:If a coordinate system is specified by the Output
          Coordinate System
          environment, the output feature class will use this coordinate
          system.If a coordinate system is not specified by the Output
          Coordinate
          System environment, the output feature class will use the coordinate
          system of the active map (ArcGIS Pro is open).If a coordinate system
          is not specified by the Output Coordinate
          System environment, and there is no active map (ArcGIS Pro is not
          open), the output feature class will use the coordinate system of the
          first input feature.If a coordinate system is not specified by the
          Output Coordinate
          System environment, there is no active map (ArcGIS Pro is not open),
          and there are no specified input features, the coordinate system of
          the output feature class will be unknown.

        """