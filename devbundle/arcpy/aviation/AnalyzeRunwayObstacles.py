# Generated documentation for module arcpy.aviation


class AnalyzeRunwayObstacles(object):
    """
    Analyzes obstacle data and obstruction identification surfaces (OIS) to determine if obstacles are penetrating.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeRunwayObstacles_aviation(input_ois_features, input_obstacle_features, out_feature_class, {height_field}, {unit_field}, {height_option}, {elevation_option}, {elevation_field}, {elevation_field_unit}, {in_dems;in_dems...})

        Analyzes obstacle data and obstruction identification surfaces (OIS)
        to determine if obstacles are penetrating.

     INPUTS:
      input_ois_features (Feature Layer):
          The multipatch features with defined Airport schema. The feature class
          must be z-enabled.
      input_obstacle_features (Feature Layer):
          The input obstacle features that will be analyzed. The feature class
          must be z-enabled.
      height_field {String}:
          The field containing the height of the obstacle features. The
          default value is. Feature GeometryFEATURE_GEOMETRY-The field
          containing the height of the obstacle
          features.
      unit_field {String}:
          Specifies the linear unit that will be used for obstacle height. This
          parameter is enabled if the height_option parameter is set to
          RELATIVE_HEIGHT.KILOMETERS-The linear unit will be
          kilometers.METERS-The linear unit
          will be meters.DECIMETERS-The linear unit will be
          decimeters.CENTIMETERS-The linear unit will be
          centimeters.MILLIMETERS-The linear unit will be
          millimeters.NAUTICAL_MILES-The linear unit will be nautical
          miles.MILES-The linear unit will be miles.YARDS-The linear unit will
          be yards.FEET-The linear unit will be feet.INCHES-The linear unit will
          be inches.DECIMAL_DEGREES-The linear unit will be decimal
          degrees.POINTS-The linear unit will be points.UNKNOWN-The linear unit
          will be unknown.
      height_option {String}:
          Specifies how obstacle height values will be
          interpreted.ABSOLUTE_HEIGHT-Obstacle heights will be measured from
          sea level.
          This is the default.RELATIVE_HEIGHT-Obstacle heights will be measured
          from ground level.
      elevation_option {String}:
          Specifies how obstacle base elevation heights will be identified. This
          parameter is enabled if the height_option parameter is set to
          RELATIVE_HEIGHT.ELEVATION_FIELD-Base elevation heights will be
          derived from a numeric
          field of the obstacle feature class. This is the
          default.ELEVATION_DEM-Base elevation heights will be derived from one
          or more
          DEMs.
      elevation_field {String}:
          The field containing base elevation heights of the obstacle
          features.This parameter is enabled if the height_option parameter is
          set to
          RELATIVE_HEIGHT and the elevation_option parameter is set to
          ELEVATION_FIELD. The default is the first numeric field in the
          obstacle feature class.
      elevation_field_unit {String}:
          Specifies the linear unit that will be used for the base elevation
          values. This parameter is enabled if the height_option parameter is
          set to RELATIVE_HEIGHT and the elevation_option parameter is set to
          ELEVATION_FIELD.KILOMETERS-The linear unit will be
          kilometers.METERS-The linear unit
          will be meters. This is the default.DECIMETERS-The linear unit will be
          decimeters.CENTIMETERS-The linear unit will be
          centimeters.MILLIMETERS-The linear unit will be
          millimeters.NAUTICAL_MILES-The linear unit will be nautical
          miles.MILES-The linear unit will be miles.YARDS-The linear unit will
          be yards.FEET-The linear unit will be feet.INCHES-The linear unit will
          be inches.DECIMAL_DEGREES-The linear unit will be decimal
          degrees.POINTS-The linear unit will be points.UNKNOWN-The linear unit
          will be unknown.
      in_dems {Raster Layer}:
          The DEMs covering the obstacles that will be used to derive base
          elevation values. This parameter is enabled if the height_option
          parameter is set to RELATIVE_HEIGHT and the elevation_option parameter
          is set to ELEVATION_DEM.

     OUTPUTS:
      out_feature_class (Feature Class):
          A feature class containing one point for each obstacle feature that
          falls within the area covered by the input OIS. If the geometry type
          of the input obstacle feature is a polyline or polygon, a multipoint
          feature class will be created.

        """