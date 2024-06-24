# Generated documentation for module arcpy.maritime


class GenerateDepthAreas(object):
    """
    Creates depth area polygon features using a TIN to query depth information to find whether a closed contour is trending deeper or shallower.
    """

    @property
    def description(self) -> str:
        return """

        GenerateDepthAreas_maritime(in_tin, in_contours, contour_depth_field, depth_direction, target_workspace, min_depth, max_depth, {in_extent_polygon})

        Creates depth area polygon features using a TIN to query depth
        information to find whether a closed contour is trending deeper or
        shallower.

     INPUTS:
      in_tin (TIN Layer):
          The TIN surface from which the nodes will be queried to attribute the
          depth polygons. It is recommended that you use the same TIN surface
          that was used to generate the contours.
      in_contours (Feature Layer):
          The depth contours features.
      contour_depth_field (Field):
          The field that will store the depth value in the depth contours
          feature.
      depth_direction (String):
          Specifies whether the depth direction is positive upward or positive
          downward. The direction must be the same as that of the input TIN and
          contour features for the values of the minimum and maximum depth for
          the generated depth area polygons to be accurate.POSITIVE_UP-The input
          contour, maximum depth, and minimum depth values
          must be negative with drying heights as positive. This is the
          default.POSITIVE_DOWN-The input contour, maximum depth, and minimum
          depth
          values must be positive with drying heights as negative.
      target_workspace (Workspace):
          The geodatabase where the depth polygons will be written. The
          workspace is expected to be a nautical workspace with either the S-57
          or S-101 schema.
      min_depth (Double):
          A value used to populate the minimum depth of polygons shallower than
          the shallowest contour value.
      max_depth (Double):
          A value used to populate the maximum depth of polygons deeper than the
          deepest contour value.
      in_extent_polygon {Feature Layer}:
          The extent polygons within which the depth area polygons will be
          generated. If not specified, the TIN domain will be used.

        """