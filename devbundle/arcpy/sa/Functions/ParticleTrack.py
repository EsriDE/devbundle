# Generated documentation for module arcpy.sa.Functions


class ParticleTrack(object):
    """
    Calculates the path of a particle through a velocity field, returning an ASCII file of particle tracking data and, optionally, a feature class of track information.
    """

    @property
    def description(self) -> str:
        return """

        ParticleTrack_sa(in_direction_raster, in_magnitude_raster, source_point, out_track_file, {step_length}, {tracking_time}, {out_track_polyline_features})

        Calculates the path of a particle through a velocity field, returning
        an ASCII file of particle tracking data and, optionally, a feature
        class of track information.

     INPUTS:
      in_direction_raster (Composite Geodataset):
          An input raster where each cell value represents the direction of the
          seepage velocity vector (average linear velocity) at the center of the
          cell.Directions are expressed in compass coordinates, in degrees
          clockwise
          from north. This can be created by the Darcy Flow tool.Direction
          values must be floating point.
      in_magnitude_raster (Composite Geodataset):
          An input raster where each cell value represents the magnitude of the
          seepage velocity vector (average linear velocity) at the center of the
          cell.Units are length/time. This can be created by the Darcy Flow
          tool.
      source_point (Point):
          A Python Point class object denotes the location of the source point,
          in map units, from which to begin the particle tracking.The form of
          the object is:point(x,y)
      step_length {Double}:
          The step length to be used for calculating the particle track.The
          default is one-half the cell size. Units are length.
      tracking_time {Double}:
          Maximum elapsed time for particle tracking.The algorithm will follow
          the track until either this time is met or
          the particle migrates off the raster or into a depression.The default
          value is infinity. Units are time.

     OUTPUTS:
      out_track_file (File):
          The output ASCII text file that contains the particle tracking data.
      out_track_polyline_features {Feature Class}:
          The optional output line feature class containing the particle
          track.This feature class contains a series of arcs with attributes for
          position, local velocity direction and magnitude, and cumulative
          length and time of travel along the path.

        """