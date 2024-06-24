# Generated documentation for module arcpy.locref


class GenerateIntersections(object):
    """
    Generates new intersections and updates existing intersections.
    """

    @property
    def description(self) -> str:
        return """

        GenerateIntersections_locref(in_intersection_feature_class, {in_network_layer}, {start_date}, {edited_by_current_user})

        Generates new intersections and updates existing intersections.

     INPUTS:
      in_intersection_feature_class (Feature Layer):
          The input LRS intersection feature class or layer.
      in_network_layer {Feature Layer}:
          The input LRS Network feature class or layer.
      start_date {Date}:
          Filters routes that have been edited after a certain date so that
          intersections can be generated.
      edited_by_current_user {Boolean}:
          Specifies whether intersections will be generated only for routes
          edited and locked by the current user.CURRENT_USER-Intersections will
          be generated only for routes edited by
          the current user. This is the default.ALL_USERS-Intersections will be
          generated for all edited routes.

        """