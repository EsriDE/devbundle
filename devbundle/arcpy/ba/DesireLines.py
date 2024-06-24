# Generated documentation for module arcpy.ba


class DesireLines(object):
    """
    Generates a series of lines from each customer to an associated store location. These lines are often called spider diagrams. The tool can also generate an optional Wind Rose report from the output.
    """

    @property
    def description(self) -> str:
        return """

        DesireLines_ba(in_stores_layer, in_customers_layer, out_feature_class, store_id_field, link_field, {distance_type}, {units}, {cutoff}, {travel_direction}, {time_of_day}, {time_zone}, {create_report}, {report_title}, {report_folder}, {report_format;report_format...})

        Generates a series of lines from each customer to an associated store
        location. These lines are often called spider diagrams. The tool can
        also generate an optional Wind Rose report from the output.

     INPUTS:
      in_stores_layer (Feature Layer):
          The input point layer representing store or facility locations.
      in_customers_layer (Feature Layer):
          The input point layer representing customers or patrons.
      store_id_field (Field):
          A unique ID field representing a store or facility location.
      link_field (Field):
          An ID field used to assign individual customers to stores.
      distance_type {String}:
          The method of travel that will be used for distance calculation.
          Straight Line is the default value.When using Portal for ArcGIS or
          local data sources, travel mode
          options are dynamically populated.
      units {String}:
          The type of distance- or time-measuring units that will be used when
          calculating minimal distance.
      cutoff {Double}:
          The distance beyond which customers will be considered outliers and
          excluded from consideration during desire line generation.
      travel_direction {String}:
          Specifies the direction of travel that will be used between stores and
          demand points.TOWARD_STORES-The direction of travel will be from
          demand points to
          stores. This is the default.AWAY_FROM_STORES-The direction of travel
          will be from stores to demand
          points.
      time_of_day {Date}:
          The time at which travel begins.
      time_zone {String}:
          Specifies the time zone that will be used for the time_of_day
          parameter.UTC-Coordinated universal time (UTC) will be used. Choose
          this option
          if you want to choose the best location for a specific time, such as
          now, but aren't certain in which time zone the stores or demand points
          are located.TIME_ZONE_AT_LOCATION-The time zone in which the stores or
          demand
          points are located will be used. If travel_direction is
          AWAY_FROM_STORES, this is the time zone of the stores. If
          travel_direction is TOWARD_STORES, this is the time zone of the demand
          points. This is the default.
      create_report {Boolean}:
          Specifies whether a Wind Rose report will be created.CREATE_REPORT-A
          report will be created.DO_NOT_CREATE_REPORT-A report
          will not be created. This is the
          default.
      report_title {String}:
          The title of the Wind Rose report.
      report_folder {Folder}:
          The output directory that will contain the Wind Rose report.
      report_format {String}:
          One or more output report formats. The default value is PDF.
          Additional available formats are XLSX, HTML, CSV, and PAGX.

     OUTPUTS:
      out_feature_class (Feature Class):
          The resultant feature class that will be added to thepane.
          Contents

        """