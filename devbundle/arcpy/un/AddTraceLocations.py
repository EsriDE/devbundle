# Generated documentation for module arcpy.un


class AddTraceLocations(object):
    """
    Creates a feature class to be used as the starting points and barriers input for the Trace tool.
    """

    @property
    def description(self) -> str:
        return """

        AddTraceLocations_un(in_utility_network, out_feature_class, {load_selected_features}, {clear_trace_locations}, {trace_locations;trace_locations...}, {filter_barrier})

        Creates a feature class to be used as the starting points and barriers
        input for the Trace tool.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The input utility network where the trace locations will be added.
      load_selected_features {Boolean}:
          Specifies whether selected features in the active map will be loaded
          as trace locations.LOAD_SELECTED_FEATURES-Trace locations will be
          loaded based on the
          selection in the map.DO_NOT_LOAD_SELECTED_FEATURES-Trace locations
          will not be loaded based
          on the selection in the map. This is the default. However, trace
          locations can be loaded using the trace_locations parameter.
      clear_trace_locations {Boolean}:
          Specifies whether existing trace locations will be cleared from the
          output feature class.CLEAR_LOCATIONS-Existing trace locations will be
          cleared.KEEP_LOCATIONS-Existing trace locations will not be cleared;
          they will
          be kept. This is the default.
      trace_locations {Value Table}:
          The trace locations that will be added to the output feature class. If
          you are not using the load_selected_features parameter in an active
          map, you can use this parameter to specify the utility network
          features to add as trace locations by providing the required values in
          the value table. The trace locations properties are as follows:
          Layer
          Name-The layer or feature class participating in the utility
          network that contains a starting point or barrier location to be
          added. If there is an active map, only layers from the map are
          allowed; if not, this will be the feature class name.Global ID-The
          Global ID of the feature for the location that will be
          added.Terminal ID-The terminal ID of the feature for the location that
          will
          be added.Percent Along-The percent along value of the feature. For
          line
          features, the default value is 0.5.
      filter_barrier {Boolean}:
          Specifies whether the barriers for the trace locations will behave as
          filter barriers.FILTER_BARRIER-The barriers will behave as filter
          barriers. This is
          useful for subnetwork-based traces in which the barrier allows the
          subnetwork to be evaluated first and is then applied on a second
          traversal of the network features.TRAVERSABILITY_BARRIER-The barriers
          will behave as traversability
          barriers, which define the extent of subnetworks, and will be
          evaluated on the first pass. This is the default.This parameter
          requires ArcGIS Enterprise 10.8.1 or later.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing the trace locations. If you
          provide a new feature class name, a new output feature class will be
          created.To use an existing feature class that was previously created
          by this
          tool and append or overwrite the existing locations, provide the name
          of the existing feature class.

        """