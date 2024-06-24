# Generated documentation for module arcpy.management


class CreateRandomPoints(object):
    """
    Creates a specified number of random point features. Random points can be generated in an extent window, inside polygon features, on point features, or along line features.
    """

    @property
    def description(self) -> str:
        return """

        CreateRandomPoints_management(out_path, out_name, {constraining_feature_class}, {constraining_extent}, {number_of_points_or_field}, {minimum_allowed_distance}, {create_multipoint_output}, {multipoint_size})

        Creates a specified number of random point features. Random points can
        be generated in an extent window, inside polygon features, on point
        features, or along line features.

     INPUTS:
      out_path (Workspace / Feature Dataset):
          The location or workspace in which the random points feature class
          will be created. This location or workspace must already exist.
      out_name (String):
          The name of the random points feature class to be created.
      constraining_feature_class {Feature Layer}:
          Random points will be generated inside or along the features in this
          feature class. The constraining feature class can be point,
          multipoint, line, or polygon. Points will be randomly placed inside
          polygon features, along line features, or at point feature locations.
          Each feature in this feature class will have the specified number of
          points generated inside it (for example, if you specify 100 points,
          and the constraining feature class has 5 features, 100 random points
          will be generated in each feature, totaling 500 points).
      constraining_extent {Extent / Feature Layer / Raster Layer}:
          Random points will be generated inside the extent. The constraining
          extent will only be used if no constraining feature class is
          specified.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      number_of_points_or_field {Long / Field}:
          The number of points to be randomly generated.The number of points can
          be specified as a long integer number or as a
          field from the constraining features containing numeric values for how
          many random points to place within each feature. The field option is
          only valid for polygon or line constraining features. If the number of
          points is supplied as a long integer number, each feature in the
          constraining feature class will have that number of random points
          generated inside or along it.
      minimum_allowed_distance {Linear Unit / Field}:
          The shortest distance allowed between any two randomly placed points.
          If a value of 1 Meter is specified, all random points will be farther
          than 1 meter away from the closest point.
      create_multipoint_output {Boolean}:
          Determines if the output feature class will be a multipart or single-
          part feature.POINT-The output will be geometry type point (each point
          is a separate
          feature). This is the default.MULTIPOINT-The output will be geometry
          type multipoint (all points are
          a single feature).
      multipoint_size {Long}:
          If create_multipoint_output is set to MULTIPOINT, specify the number
          of random points to be placed in each multipoint geometry. The default
          is 10.

        """