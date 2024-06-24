# Generated documentation for module arcpy.geoanalytics


class FindHotSpots(object):
    """
    Given a set of features, identifies statistically significant hot spots and cold spots using the Getis-Ord Gi* statistic.
    """

    @property
    def description(self) -> str:
        return """

        FindHotSpots_geoanalytics(point_layer, output_name, {bin_size}, {neighborhood_size}, {time_step_interval}, {time_step_alignment}, {time_step_reference}, {data_store})

        Given a set of features, identifies statistically significant hot
        spots and cold spots using the Getis-Ord Gi* statistic.

     INPUTS:
      point_layer (Feature Set):
          The point feature class for which hot spot analysis will be performed.
      output_name (String):
          The name of the output layer with the z-score and p-value results.
      bin_size {Linear Unit}:
          The distance interval that represents the bin size and units into
          which the point_layer will be aggregated. The distance interval must
          be a linear unit.
      neighborhood_size {Linear Unit}:
          The spatial extent of the analysis neighborhood. This value determines
          which features are analyzed together to assess local clustering.
      time_step_interval {Time Unit}:
          The interval that will be used for the time step. This parameter is
          only used if time is enabled for point_layer.
      time_step_alignment {String}:
          Specifies how time steps will be aligned. This parameter is only
          available if the input points are time enabled and represent an
          instant in time.END_TIME-Time steps will align to the last time event
          and aggregate
          back in time.START_TIME-Time steps will align to the first time event
          and aggregate
          forward in time. This is the default. REFERENCE_TIME-Time
          steps will align to a specified date or
          time. If all points in the input features have a time stamp larger
          than the specified reference time (or it falls exactly on the start
          time of the input features), the time-step interval will begin with
          that reference time and aggregate forward in time (as occurs with
          thealignment). If all points in the input features have a time stamp
          smaller than the specified reference time (or it falls exactly on the
          end time of the input features), the time-step interval will end with
          that reference time and aggregate backward in time (as occurs with
          thealignment). If the specified reference time is in the middle of the
          time extent of the data, a time-step interval will be created ending
          with the reference time provided (as occurs with thealignment);
          additional intervals will be created both before and after the
          reference time until the full time extent of the data is covered.
          Start timeEnd timeEnd time
      time_step_reference {Date}:
          The time that will be used to align the time steps and time intervals.
          This parameter is only used if time is enabled for point_layer.
      data_store {String}:
          Specifies the ArcGIS Data Store where the output will be saved. The
          default is SPATIOTEMPORAL_DATA_STORE. All results stored in a
          spatiotemporal big data store will be stored in WGS84. Results stored
          in a relational data store will maintain their coordinate
          system.SPATIOTEMPORAL_DATA_STORE-Output will be stored in a
          spatiotemporal
          big data store. This is the default.RELATIONAL_DATA_STORE-Output will
          be stored in a relational data
          store.

        """