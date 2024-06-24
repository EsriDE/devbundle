# Generated documentation for module arcpy.transit


class FeaturesToGTFSStops(object):
    """
    Converts a feature class to a GTFS stops.txt file for a GTFS public transit dataset.
    """

    @property
    def description(self) -> str:
        return """

        FeaturesToGTFSStops_transit(in_features, out_gtfs_stops_file)

        Converts a feature class to a GTFS stops.txt file for a GTFS public
        transit dataset.

     INPUTS:
      in_features (Feature Layer):
          A point feature class containing transit stop geometries and
          at least the minimum required GTFS stops.txt file fields exceptand.
          stop_latstop_lon

     OUTPUTS:
      out_gtfs_stops_file (File):
          The output stops.txt file.

        """