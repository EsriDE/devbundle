# Generated documentation for module arcpy.management


class SelectLayerByLocation(object):
    """
    Selects features based on a spatial relationship to features in another dataset or the same dataset.
    """

    @property
    def description(self) -> str:
        return """

        SelectLayerByLocation_management(in_layer;in_layer..., {overlap_type}, {select_features}, {search_distance}, {selection_type}, {invert_spatial_relationship})

        Selects features based on a spatial relationship to features in
        another dataset or the same dataset.

     INPUTS:
      in_layer (Feature Layer / Raster Layer / Mosaic Layer):
          The features that will be evaluated using the select_features
          parameter values. The selection will be applied to these features.
      overlap_type {String}:
          Specifies the spatial relationship that will be
          evaluated.INTERSECT-The features in the input layer will be selected
          if they
          intersect a selecting feature. This is the default.INTERSECT_3D-The
          features in the input layer will be selected if they
          intersect a selecting feature in three-dimensional space (x, y, and
          z). INTERSECT_DBMS-The features in the input layer will be
          selected if they intersect a selecting feature. This option
          applies to enterprise geodatabases only. The selection
          will be processed in the enterprise geodatabase DBMS rather than on
          the client when all requirements are met (see usage notes).This option
          may provide better performance than performing the
          selection on the client.WITHIN_A_DISTANCE-The features in the input
          layer will be selected if
          they are within the specified distance (using Euclidean distance) of a
          selecting feature. Use the search_distance parameter to specify the
          distance.WITHIN_A_DISTANCE_3D-The features in the input layer will be
          selected
          if they are within a specified distance of a selecting feature in
          three-dimensional space. Use the search_distance parameter to specify
          the distance.WITHIN_A_DISTANCE_GEODESIC-This spatial relationship is
          the same as
          WITHIN_A_DISTANCE except that geodesic distance is used rather than
          planar distance. Distance between features will be calculated using a
          geodesic formula that takes into account the curvature of the spheroid
          and correctly handles data near and across the dateline and poles.
          Choose this option if the data covers a large geographic extent or the
          coordinate system of the inputs is unsuitable for distance
          calculations. Use the search_distance parameter to specify the
          distance.CONTAINS-The features in the input layer will be selected if
          they
          contain a selecting feature.COMPLETELY_CONTAINS-The features in the
          input layer will be selected
          if they completely contain a selecting feature.
          CONTAINS_CLEMENTINI-This spatial relationship produces the
          same results as the CONTAINS option except that if the selecting
          feature is entirely on the boundary of the input feature (no part is
          properly inside or outside), the feature will not be selected.
          Clementini defines the boundary polygon as the line separating inside
          and outside, the boundary of a line is defined as its end points, and
          the boundary of a point is always empty.WITHIN-The features in the
          input layer will be selected if they are
          within a selecting feature.COMPLETELY_WITHIN-The features in the input
          layer will be selected if
          they are completely within or contained by a selecting feature.
          WITHIN_CLEMENTINI-The result will be identical to the WITHIN
          option result except that if the entirety of the feature in the input
          layer is on the boundary of the feature in the selecting layer, the
          feature will not be selected. Clementini defines the boundary
          polygon as the line separating inside
          and outside, the boundary of a line is defined as its end points, and
          the boundary of a point is always empty.ARE_IDENTICAL_TO-The features
          in the input layer will be selected if
          they are identical (in geometry) to a selecting
          feature.BOUNDARY_TOUCHES-The features in the input layer will be
          selected if
          they have a boundary that touches a selecting feature. When the input
          features are lines or polygons, the boundary of the input feature can
          only touch the boundary of the selecting feature, and no part of the
          input feature can cross the boundary of the selecting
          feature.SHARE_A_LINE_SEGMENT_WITH-The features in the input layer will
          be
          selected if they share a line segment with a selecting feature. The
          input and selecting features must be line or
          polygon.CROSSED_BY_THE_OUTLINE_OF-The features in the input layer will
          be
          selected if they are crossed by the outline of a selecting feature.
          The input and selecting features must be lines or polygons. If
          polygons are used for the input or selecting layer, the polygon's
          boundary (line) will be used. Lines that cross at a point will be
          selected; lines that share a line segment will not be
          selected.HAVE_THEIR_CENTER_IN-The features in the input layer will be
          selected
          if their center falls within a selecting feature. The center of the
          feature is calculated as follows: for polygon and multipoint, the
          geometry's centroid is used; for line input, the geometry's midpoint
          is used.
      select_features {Feature Layer}:
          The features in theparameter will be selected based on their
          relationship to the features from this layer or feature class.
          Input Features
      search_distance {Linear Unit}:
          The distance that will be searched. This parameter is only valid if
          the overlap_type parameter is set to WITHIN_A_DISTANCE,
          WITHIN_A_DISTANCE_GEODESIC, WITHIN_A_DISTANCE_3D, INTERSECT,
          INTERSECT_3D, HAVE_THEIR_CENTER_IN, or CONTAINS.If the
          WITHIN_A_DISTANCE_GEODESIC option is selected, use a linear
          unit such as kilometers or miles.
      selection_type {String}:
          Specifies how the selection will be applied to the input and how it
          will be combined with an existing selection. This tool does not
          include an option to clear an existing selection; use the Select Layer
          By Attribute tool with the selection_type parameter set to
          CLEAR_SELECTION to do that.NEW_SELECTION-The resulting selection will
          replace any existing
          selection. This is the default.ADD_TO_SELECTION-The resulting
          selection will be added to an existing
          selection. If no selection exists, this is the same as the
          NEW_SELECTION option.REMOVE_FROM_SELECTION-The resulting selection
          will be removed from an
          existing selection. If no selection exists, the operation will have no
          effect.SUBSET_SELECTION-The resulting selection will be combined with
          the
          existing selection. Only records that are common to both will remain
          selected. SWITCH_SELECTION-The selection will be switched. All
          records
          that were selected will be removed from the selection, and all records
          that were not selected will be added to the selection. The
          select_features and overlap_type parameters are ignored when this
          option is specified.
      invert_spatial_relationship {Boolean}:
          Specifies whether the spatial relationship evaluation result or the
          opposite result will be used. For example, this parameter can be used
          to get a list of features that do not intersect or are not within a
          given distance of features in another dataset.NOT_INVERT-The
          evaluation result will be used. This is the
          default.INVERT-The opposite of the evaluation result will be used. If
          the
          selection_type parameter is set, the reversal of the selection will
          occur before it is combined with existing selections.

        """