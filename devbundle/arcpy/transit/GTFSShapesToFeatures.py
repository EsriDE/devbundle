# Generated documentation for module arcpy.transit


class GTFSShapesToFeatures(object):
    """
    Converts a GTFS shapes.txt file from a GTFS public transit dataset to a polyline feature class showing the physical paths taken by vehicles in the public transit system.
    """

    @property
    def description(self) -> str:
        return """

        GTFSShapesToFeatures_transit(in_gtfs_shapes_file, out_feature_class)

        Converts a GTFS shapes.txt file from a GTFS public transit dataset to
        a polyline feature class showing the physical paths taken by vehicles
        in the public transit system.

     INPUTS:
      in_gtfs_shapes_file (File):
          A valid shapes.txt file from a GTFS dataset.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class.

        """