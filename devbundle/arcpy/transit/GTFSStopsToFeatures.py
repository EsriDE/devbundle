# Generated documentation for module arcpy.transit


class GTFSStopsToFeatures(object):
    """
    Converts a GTFS stops.txt file from a GTFS public transit dataset to a feature class of public transit stops.
    """

    @property
    def description(self) -> str:
        return """

        GTFSStopsToFeatures_transit(in_gtfs_stops_file, out_feature_class)

        Converts a GTFS stops.txt file from a GTFS public transit dataset to a
        feature class of public transit stops.

     INPUTS:
      in_gtfs_stops_file (File):
          A valid stops.txt file from a GTFS dataset.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class.

        """