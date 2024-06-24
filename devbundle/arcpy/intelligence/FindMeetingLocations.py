# Generated documentation for module arcpy.intelligence


class FindMeetingLocations(object):
    """
    Identifies locations where multiple unique movement tracks have dwelled for a defined time period.
    """

    @property
    def description(self) -> str:
        return """

        FindMeetingLocations_intelligence(in_features, out_area_features, out_point_features, unique_name_field, {search_distance}, {minimum_loiter_time}, {temporal_relationship}, {min_meeting_duration}, {max_meeting_duration})

        Identifies locations where multiple unique movement tracks have
        dwelled for a defined time period.

     INPUTS:
      in_features (Feature Layer):
          The input movement track points that will be analyzed for possible
          meeting locations. This layer must be time enabled.
      unique_name_field (Field):
          The field containing the unique identifiers for movement track points.
      search_distance {Linear Unit}:
          The maximum distance a movement track can loiter before it is no
          longer considered part of a meeting. The default is 100 meters.
      minimum_loiter_time {Time Unit}:
          The minimum amount of time a movement track point can loiter in an
          area before it is considered to be dwelling. This helps identify
          possible meeting locations where multiple unique movement tracks are
          dwelling in the same time and space. The default is 10 minutes.
      temporal_relationship {String}:
          Specifies the time criteria that will be used to match
          features.OVERLAPS-When a target time interval starts and ends before
          the start
          and end of the join time interval, the target time will overlap the
          join time.INTERSECTS-When any part of a target time occurs at the same
          time as
          the join time, the target time will intersect the join time. This is
          the default.
      min_meeting_duration {Time Unit}:
          The minimum meeting duration that will be used for the meeting to be
          included in the output.
      max_meeting_duration {Time Unit}:
          The maximum meeting duration that will be used for the meeting to be
          included in the output.

     OUTPUTS:
      out_area_features (Feature Class):
          The output area features that represent the extent of the identified
          meeting location.
      out_point_features (Feature Class):
          The output point features that represent the centroid of the area of
          the individual meeting. Multiple meetings can occur at a given meeting
          location. This feature class contains all of the details regarding the
          individual meetings including participants, duration, and start and
          end times.

        """