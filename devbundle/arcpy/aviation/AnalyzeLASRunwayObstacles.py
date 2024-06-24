# Generated documentation for module arcpy.aviation


class AnalyzeLASRunwayObstacles(object):
    """
    Analyzes lidar data and obstruction identification surfaces (OIS) to determine if lidar points are penetrating.
    """

    @property
    def description(self) -> str:
        return """

        AnalyzeLASRunwayObstacles_aviation(in_ois_features, in_las_obstacles, {out_obstacle_feature_class}, {target_folder}, {out_las_obstacles}, {vertical_clearance}, {vertical_clearance_unit})

        Analyzes lidar data and obstruction identification surfaces (OIS) to
        determine if lidar points are penetrating.

     INPUTS:
      in_ois_features (Feature Layer):
          The input multipatch features representing one or more OIS. The
          feature class must be z-enabled.
      in_las_obstacles (LAS Dataset Layer):
          The input LAS dataset that contains 3D data points covering the area
          around an airport. The points represent a 3D view of natural and
          human-made objects that may pose a hazard to flight.
      vertical_clearance {Double}:
          If a LAS point height is above the OIS surface, that point will be
          captured. The height of an OIS surface above a given LAS point is
          temporarily lowered by the specified vertical clearance value. This
          decreases the distance between the height of the LAS point and the
          corresponding OIS surface, resulting in the likeliness that more
          points will be captured. Consequently, a larger collection of ground
          features, represented by the LAS points penetrating through the OIS
          surface, will be captured.
      vertical_clearance_unit {String}:
          The linear unit that will be used for the vertical
          clearance.KILOMETERS-The linear unit will be kilometers.METERS-The
          linear unit
          will be meters.DECIMETERS-The linear unit will be
          decimeters.CENTIMETERS-The linear unit will be
          centimeters.MILLIMETERS-The linear unit will be
          millimeters.NAUTICAL_MILES-The linear unit will be nautical
          miles.MILES-The linear unit will be miles.YARDS-The linear unit will
          be yards.FEET-The linear unit will be feet.INCHES-The linear unit will
          be inches.DECIMAL_DEGREES-The linear unit will be decimal
          degrees.POINTS-The linear unit will be points.UNKNOWN-The linear unit
          will be unknown.

     OUTPUTS:
      out_obstacle_feature_class {Feature Layer}:
          The output point features that represent lidar points in OIS features
          in which the height of the lidar point is greater than the height of
          the enclosing OIS feature at that point. This feature class is
          required output only if no output LAS dataset is requested.
      target_folder {Folder}:
          The folder to which .las files will be written. Each output file will
          have the same .las file version and point record format as the input
          file. This folder is required output only if no output feature class
          is requested.
      out_las_obstacles {LAS Dataset Layer}:
          The output LAS dataset referencing the newly created .las files. This
          LAS dataset is created only when the output folder is specified to
          generate the LAS output.

        """