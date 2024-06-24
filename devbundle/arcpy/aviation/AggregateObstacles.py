# Generated documentation for module arcpy.aviation


class AggregateObstacles(object):
    """
    Aggregates obstacle features within a given radius so that the highest obstacle in the group represents the entire group.
    """

    @property
    def description(self) -> str:
        return """

        AggregateObstacles_aviation(in_obstacle_features, height_field, height_field_units, elevation_field, elevation_field_units, elevation_interpretation, target_obstacle_group_features, target_obstacle_group_label, in_obstacle_assocation_table, {search_radius}, {height_threshold}, {builtup_areas_features}, {builtup_areas_height_threshold}, {obstacle_grouping_type}, {target_obstacle_group_polygon_features}, {minimum_polygon_area})

        Aggregates obstacle features within a given radius so that the highest
        obstacle in the group represents the entire group.

     INPUTS:
      in_obstacle_features (Feature Layer):
          The input obstacle features.
      height_field (String):
          The field containing the height of the obstacle features.
      height_field_units (String):
          Specifies the units that will be used for obstacle height.METERS-The
          obstacle height will be in meters.DECIMETERS-The obstacle
          height will be in decimeters.CENTIMETERS-The obstacle height will be
          in centimeters.MILLIMETERS-The obstacle height will be in
          millimeters.YARDS-The obstacle height will be in yards.FEET-The
          obstacle height will be in feet. This is the default.INCHES-The
          obstacle height will be in inches.
      elevation_field (String):
          The field containing the elevation of the obstacle features.
      elevation_field_units (String):
          Specifies the units that will be used for obstacle
          elevation.METERS-The obstacle elevation will be in
          meters.DECIMETERS-The
          obstacle elevation will be in decimeters.CENTIMETERS-The obstacle
          elevation will be in centimeters.MILLIMETERS-The obstacle elevation
          will be in millimeters.YARDS-The obstacle elevation will be in
          yards.FEET-The obstacle elevation will be in feet. This is the
          default.INCHES-The obstacle elevation will be in inches.
      elevation_interpretation (String):
          Specifies how obstacle elevations will be
          measured.ON_THE_GROUND-Elevation values will be measured using the
          AMSL
          elevation of the base of the obstacle. The height value will be added
          to the elevation value to determine the elevation of the top of the
          obstacle.ABOVE_THE_GROUND-Elevation values will be measured using the
          AMSL
          elevation of the top of the obstacle. This is the default.
      target_obstacle_group_features (Feature Layer):
          The output feature class to which aggregated obstacle features will be
          written.
      target_obstacle_group_label (String):
          The text describing the obstacle grouping. The text is used to
          identify obstacle groups for different chart specifications that may
          be created using different parameters.
      in_obstacle_assocation_table (Table View):
          A table that will be populated with information linking each obstacle
          group feature to the obstacles it represents.
      search_radius {Linear Unit}:
          The radius within which the obstacles will be grouped.
      height_threshold {Linear Unit}:
          The height threshold for an obstacle to be considered for grouping.
          Obstacles with a height value greater than or equal to this value will
          be considered.
      builtup_areas_features {Feature Layer}:
          Polygon features designating built-up areas. These represent areas
          where a different height threshold is required.
      builtup_areas_height_threshold {Linear Unit}:
          The height threshold for an obstacle within a built-up area polygon to
          be considered for grouping. Obstacles with a height value equal to or
          greater than this value will be considered.
      obstacle_grouping_type {String}:
          Specifies the geometry type of the obstacle groups that will be
          generated.TO_POINT-Obstacles will be generated as points. This is the
          default.TO_POLYGON-Obstacles will be generated as polygons.
      target_obstacle_group_polygon_features {Feature Layer}:
          The output polygon feature class to which aggregated obstacle features
          will be written.
      minimum_polygon_area {Areal Unit}:
          The minimum area of an output polygon before it collapses to a point
          feature.

        """