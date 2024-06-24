# Generated documentation for module arcpy.stpm


class SubsetSpaceTimeCube(object):
    """
    Subsets a space-time cube by spatial extent, space, or time.
    """

    @property
    def description(self) -> str:
        return """

        SubsetSpaceTimeCube_stpm(in_cube, out_cube, spatial_subset_method, temporal_subset_method, {in_subset_features}, {spatial_relationship}, {spatial_extent}, {in_spatial_cube}, {time_span_subset;time_span_subset...}, {remove_time_steps;remove_time_steps...}, {in_temporal_cube})

        Subsets a space-time cube by spatial extent, space, or time.

     INPUTS:
      in_cube (File):
          The space-time cube to be subset. Space-time cubes have an .nc file
          extension and are created using various tools in the Space Time
          Pattern Mining toolbox.
      spatial_subset_method (String):
          Specifies the method that will be used to spatially subset the input
          space-time cube. Any location in the input space-time cube that
          satisfies this spatial subset criteria will be included in the output
          space-time cube.FEATURES-A feature class with polygons, points, or
          lines will be used
          to subset the input space-time cube. The spatial_relationship
          parameter specifies how the feature layer will subset the space-time
          cube.EXTENT-The extent specified by the spatial_extent parameter will
          be
          used to subset the input space-time cube. The output space-time cube
          will include all the locations in the input space-time cube that
          intersect the extent.SPACE_TIME_CUBE-The locations of the space-time
          cube specified by the
          in_spatial_cube parameter will be used to subset a space-time cube.
          The spatial_relationship parameter specifies how this space-time cube
          will subset the input space-time cube.NONE-No spatial subset will be
          applied to the input space-time cube.
      temporal_subset_method (String):
          Specifies the method that will be used to temporally subset a space-
          time cube. Any time step in the input space-time cube that satisfies
          the temporal subset criteria will be included in the output space-time
          cube.USER_DEFINED-The temporal range specified by the start time or
          end
          time values in the time_span_subset parameter will be used to
          temporally subset the input space-time cube.NUMBER_OF_TIME_STEPS-A
          number of time steps from the start and the end
          of the input space-time cube will be used to temporally subset the
          space-time cube. The number of time steps to remove is specified by
          the from the start or from the end values in the remove_time_steps
          parameter.SPACE_TIME_CUBE-The temporal extent of the space-time cube
          specified
          by the in_temporal_cube parameter will be used to temporally subset
          the input space-time cube.NONE-No temporal subset will be applied to
          the input space-time cube.
      in_subset_features {Feature Layer}:
          A feature class that contains polygons, points, or lines to subset a
          space-time cube. The spatial relationship between the input subset
          features and the space-time cube is specified by the
          spatial_relationship parameter.
      spatial_relationship {String}:
          The spatial relationship that will be applied between the
          in_subset_features or in_spatial_cube parameter value and the input
          space-time cube to spatially subset the space-time cube. The available
          spatial relationship options will depend on the geometry of the input
          space-time cube and the input subset features or the input spatial
          subset cube.INTERSECT-The output space-time cube will include the
          locations in the
          input space-time cube that intersect the in_subset_features or
          in_spatial_cube parameter value. This is the default.CONTAINS-The
          output space-time cube will include the locations in the
          input space-time cube that contain the in_subset_features or
          in_spatial_cube parameter value.WITHIN-The output space-time cube will
          include the locations in the
          input space-time cube that are within the in_subset_features or
          in_spatial_cube parameter value.HAVE_THEIR_CENTER_IN-The output space-
          time cube will include the
          locations in the input space-time cube that have their center in the
          in_subset_features or in_spatial_cube parameter value.
      spatial_extent {Extent}:
          The spatial extent that will spatially subset the input space-time
          cube. The output space-time cube will include the locations in the
          input space-time cube that intersect the extent.
      in_spatial_cube {File}:
          A space-time cube that will spatially subset the input space-time
          cube. The spatial relationship between the input spatial subset cube
          and the space-time cube is specified by the spatial_relationship
          parameter.
      time_span_subset {Value Table}:
          The time interval to temporally subset the input space-time cube. Any
          time step that is within this time interval or that contains the start
          time or end time values will be included in the output space-time
          cube.
      remove_time_steps {Value Table}:
          The number of time steps from the start and the end of the input
          space-time cube that will be removed from the output space-time cube.
      in_temporal_cube {File}:
          A space-time cube that will temporally subset the input space-time
          cube. The temporal extent of the temporal subset cube defines the
          temporal extent of the output space-time cube. Any time step that is
          within the temporal extent of the input temporal subset cube or that
          contains the start time or end time of the temporal subset cube will
          be included in the output space-time cube.

     OUTPUTS:
      out_cube (File):
          The subset of the input space-time cube that meets the spatial and
          temporal criteria specified by the spatial_subset_method and
          temporal_subset_method parameters. The analysis variables stored in
          the input space-time cube will be excluded from the output space-time
          cube.

        """