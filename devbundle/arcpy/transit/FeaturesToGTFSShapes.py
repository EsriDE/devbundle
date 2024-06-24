# Generated documentation for module arcpy.transit


class FeaturesToGTFSShapes(object):
    """
    Creates a shapes.txt file for a GTFS public transit dataset based on route line representations created by the Generate Shapes Features From GTFS tool.
    """

    @property
    def description(self) -> str:
        return """

        FeaturesToGTFSShapes_transit(in_shape_lines, in_shape_stops, in_gtfs_trips, in_gtfs_stop_times, out_gtfs_shapes, out_gtfs_stop_times, {distance_units})

        Creates a shapes.txt file for a GTFS public transit dataset based on
        route line representations created by the Generate Shapes Features
        From GTFS tool.

     INPUTS:
      in_shape_lines (Feature Layer):
          A line feature class representing the GTFS shapes created by
          running the Generate Shapes Features From GTFS tool. The feature class
          must contain afield with values corresponding to thefield values in
          the other tool inputs. shape_idshape_id
      in_shape_stops (Feature Layer):
          A point feature class representing the GTFS stops associated with each
          shape created by running the Generate Shapes Features From GTFS tool.
          If a transit stop is used by multiple shapes, the stop should be
          duplicated in this feature class for each shape that uses it.
          The feature class must contain afield with values
          corresponding to thefield values in the other tool inputs. It must
          also contain afield with values corresponding to those in thecolumn of
          the input GTFS stop_times.txt file.
          shape_idshape_idstop_idshape_id
      in_gtfs_trips (File):
          The updated GTFS trips.txt file created by running the
          Generate Shapes Features From GTFS tool. This file must have thecolumn
          with values corresponding to those in thefields in the other tool
          inputs. shape_idshape_id
      in_gtfs_stop_times (File):
          The original stop_times.txt file from the GTFS dataset that was used
          when running the Generate Shapes Features From GTFS tool.
      distance_units {String}:
          Specifies the distance units to use when populating thefield
          in the output GTFS files. shape_dist_traveledMILES-The unit is
          miles. This is the default.METERS-The unit is
          metersKILOMETERS-The unit is kilometers

     OUTPUTS:
      out_gtfs_shapes (File):
          The output GTFS shapes.txt file.
      out_gtfs_stop_times (File):
          The output GTFS stop_times.txt file This file will contain
          thefield with values derived from the new shapes.
          shape_dist_traveled

        """