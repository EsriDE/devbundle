# Generated documentation for module arcpy.transit


class GTFSToPublicTransitDataModel(object):
    """
    Converts one or more General Transit Feed Specification (GTFS) public transit datasets to a set of feature classes and tables that represent the transit stops, lines, and schedules in the format defined by the Network Analyst public transit data model.
    """

    @property
    def description(self) -> str:
        return """

        GTFSToPublicTransitDataModel_transit(in_gtfs_folders;in_gtfs_folders..., target_feature_dataset, {interpolate}, {append})

        Converts one or more General Transit Feed Specification (GTFS) public
        transit datasets to a set of feature classes and tables that represent
        the transit stops, lines, and schedules in the format defined by the
        Network Analyst public transit data model.

     INPUTS:
      in_gtfs_folders (Folder):
          One or more folders containing valid GTFS data. Each folder must
          contain the GTFS stops.txt, routes.txt, trips.txt, and stop_times.txt
          files and either the calendar.txt or calendar_dates.txt file, or both.
      target_feature_dataset (Feature Dataset):
          The feature dataset where the transit-enabled network dataset will be
          created. The Stops and LineVariantElements feature classes created by
          this tool will be placed in this feature dataset, and the output
          tables created by this tool will be placed in this feature dataset's
          parent geodatabase.The feature dataset can be in a file geodatabase or
          an enterprise
          geodatabase and can have any spatial reference. If the target feature
          dataset is in an enterprise geodatabase, it must not be versioned. Do
          not include the target feature dataset in a geodatabase with an
          existing feature dataset containing public transit data model feature
          classes.
      interpolate {Boolean}:
          Specifies whether blank values from theandfields in the GTFS
          stop_times.txt file will be interpolated when creating the public
          transit data model tables.
          arrival_timedeparture_timeINTERPOLATE-Blank values will be
          interpolated using simple linear
          interpolation. The original GTFS data will not be altered. If there
          are no blank values in the original data, no interpolation will
          occur.NO_INTERPOLATE-Blank values will not be interpolated. If blank
          values
          are found in the input GTFS data, the tool will issue a warning and
          will not process the GTFS dataset. This is the default.
      append {Boolean}:
          Specifies whether the input GTFS datasets will be appended to existing
          public transit data model feature classes and tables in the target
          feature dataset and its parent geodatabase.APPEND-Data will be
          appended to the existing feature classes and
          tables.NO_APPEND-Data will not be appended. Existing feature classes
          and
          tables will be overwritten. This is the default.

        """