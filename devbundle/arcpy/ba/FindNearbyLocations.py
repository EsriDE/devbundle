# Generated documentation for module arcpy.ba


class FindNearbyLocations(object):
    """
    Identifies locations closest to the input features based on a selected distance type. The number of points in the output is defined by limiting the count or percentage of location points to return or by limiting the distance from the input points.
    """

    @property
    def description(self) -> str:
        return """

        FindNearbyLocations_ba(in_features, id_field, in_location_points, out_feature_class, {distance_type}, {units}, {distance_limit}, {number_limit}, {percent_limit}, {create_report}, {report_title}, {report_folder}, {report_format;report_format...}, {report_fields;report_fields...}, {travel_direction}, {time_of_day}, {time_zone}, {search_tolerance}, {location_name})

        Identifies locations closest to the input features based on a selected
        distance type. The number of points in the output is defined by
        limiting the count or percentage of location points to return or by
        limiting the distance from the input points.

     INPUTS:
      in_features (Feature Layer):
          The point layer to be measured to or from the in_location_points
          parameter value.
      id_field (Field):
          A field containing unique identifiers for each input feature.
      in_location_points (Feature Layer):
          The layer that will be used to generate the output with distance and
          direction attributes to or from the in_features parameter value.
      distance_type {String}:
          The calculated distance based on the method of travel. Straight Line
          is the default value.
      units {String}:
          The measurement units, in distance or time, that will be used when
          calculating nearby locations.
      distance_limit {Double}:
          The analysis extent measured in distance or time.
      number_limit {Long}:
          The numeric limit of the in_location_points value.
      percent_limit {Double}:
          The closest points, as a percentage of the points of the
          in_location_points value.
      create_report {Boolean}:
          Specifies whether an output report will be created.CREATE_REPORT-A
          report will be created.DO_NOT_CREATE_REPORT-A report
          will not be created. This is the
          default.
      report_title {String}:
          The title of the output report.
      report_folder {Folder}:
          The directory that will contain the output report.
      report_format {String}:
          The output report formats. The default value is InfographicHTML.
          Additional available formats are PDF, XLSX, S.XLSX, HTML, S.XML, ZIP,
          CVS, PAGX, and InfographicPDF.
      report_fields {Field}:
          The additional fields that will be added to the report.
      travel_direction {String}:
          Specifies whether travel times or distances will be measured from
          location points to input features or from input features to location
          points.TOWARD_STORES-The direction of travel will be from location
          points to
          input features. This is the default.AWAY_FROM_STORES-The direction of
          travel will be from input features
          to location points.
      time_of_day {Date}:
          The time at which travel will begin.
      time_zone {String}:
          Specifies the time zone that will be used for the time_of_day
          parameter.UTC-Coordinated universal time (UTC) will be used. Choose
          this option
          if you want the best location for a specific time, such as now, but
          aren't certain of the time zone in which the in_location_points value
          will be located.TIME_ZONE_AT_LOCATION-The time zone in which the
          in_location_points
          value is located will be used. If the travel direction is input
          features to location points, this is the time zone of the input
          features. If the travel direction is location points to input
          features, this is the time zone of the location points. This is the
          default.
      search_tolerance {Linear Unit}:
          The maximum distance that input points can be from the network. Points
          located beyond the search tolerance will be excluded from processing.
      location_name {Field}:
          A field from the input in_location_points parameter. This field
          contains the name or ID for each input point used in the Find Nearby
          Locations report.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output location point features.

        """