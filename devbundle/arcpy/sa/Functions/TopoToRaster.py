# Generated documentation for module arcpy.sa.Functions


class TopoToRaster(object):
    """
    Interpolates a hydrologically correct raster surface from point, line, and polygon data.
    """

    @property
    def description(self) -> str:
        return """

        TopoToRaster_sa(topo_input, {cell_size}, {extent}, {Margin}, {minimum_z_value}, {maximum_z_value}, {enforce}, {data_type}, {maximum_iterations}, {roughness_penalty}, {discrete_error_factor}, {vertical_standard_error}, {tolerance_1}, {tolerance_2}, {out_stream_features}, {out_sink_features}, {out_diagnostic_file}, {out_parameter_file}, {profile_penalty}, {out_residual_feature}, {out_stream_cliff_error_feature}, {out_contour_error_feature})

        Interpolates a hydrologically correct raster surface from point, line,
        and polygon data.

     INPUTS:
      topo_input (Topo Features):
          The Topo class specifies the input features containing the z-values to
          be interpolated into a surface raster.There are nine types of data
          accepted inputs to the Topo class:
          TopoPointElevation, TopoContour, TopoStream, TopoSink, TopoBoundary,
          TopoLake, TopoCliff, TopoExclusion, and TopoCoast.
          TopoPointElevation ([[inFeatures,{field}],...])         A
          point feature class representing surface elevations.The field stores
          the elevations of the points. TopoContour
          ([[inFeatures,{field}],...])         A line
          feature class that represents elevation contours.The field stores the
          elevations of the contour lines. TopoStream ([inFeatures,...])
          A line feature class of
          stream locations. All arcs must be oriented to
          point downstream. The feature class should only contain single arc
          streams. TopoSink ([[inFeatures,{field}],...])         A point
          feature
          class that represents known topographic depressions.
          Topo to Raster will not attempt to remove from the analysis any points
          explicitly identified as sinks.The field used should be one that
          stores the elevation of the
          legitimate sink. If NONE is selected, only the location of the sink is
          used. TopoBoundary ([inFeatures,...])         A boundary is a
          feature class containing a single polygon that
          represents the outer boundary of the output raster. Cells in the
          output raster outside this boundary will be NoData. This option can be
          used for clipping out water areas along coastlines before making the
          final output raster. TopoLake ([inFeatures,...])         A
          polygon feature class
          that specifies the location of lakes. All
          output raster cells within a lake will be assigned to the minimum
          elevation value of all cells along the shoreline. TopoCliff
          ([inFeatures,...])         A line feature class of
          the cliffs. The cliff line features must be
          oriented so that the left-hand side of the line is on the low side of
          the cliff and the right-hand side is the high side of the cliff.
          TopoExclusion ([inFeatures,...])         A polygon feature
          class of the areas in which the input data should be
          ignored. These polygons permit removal of elevation data from the
          interpolation process. This is typically used to remove elevation data
          associated with dam walls and bridges. This enables interpolation of
          the underlying valley with connected drainage structure.
          TopoCoast ([inFeatures,...])         A polygon feature class
          containing the outline of a coastal area.
          Cells in the final output raster that lie outside these polygons are
          set to a value that is less than the user-specified minimum height
          limit.The PointElevation, Contour, and Sink types of feature input can
          have
          a field specified that contains the z-values. There is no Field option
          for Boundary, Lake, Cliff, Coast, Exclusion, or Stream input types.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      extent {Extent}:
          Extent for the output raster dataset.Interpolation will occur out to
          the x and y limits, and cells outside
          that extent will be NoData. For best interpolation results along the
          edges of the output raster, the x and y limits should be smaller than
          the extent of the input data by at least 10 cells on each side.The
          default extent is the largest of all extents of the input feature
          data.MAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      Margin {Long}:
          Distance in cells to interpolate beyond the specified output extent
          and boundary.The value must be greater than or equal to 0 (zero). The
          default value
          is 20.If the Extent and TopoBoundary feature dataset are the same as
          the
          limit of the input data (the default), values interpolated along the
          edge of the DEM will not match well with adjacent DEM data. This is
          because they have been interpolated using one-half as much data as the
          points inside the raster, which are surrounded on all sides by input
          data. The option allows input data beyond these limits to be used in
          the interpolation.
      minimum_z_value {Double}:
          The minimum z-value to be used in the interpolation.The default is 20
          percent below the smallest of all the input values.
      maximum_z_value {Double}:
          The maximum z-value to be used in the interpolation.The default is 20
          percent above the largest of all input values.
      enforce {String}:
          The type of drainage enforcement to apply.The drainage enforcement
          option can be set to attempt to remove all
          sinks or depressions so a hydrologically correct DEM can be created.
          If sink points have been explicitly identified in the input feature
          data, these depressions will not be filled.ENFORCE-The algorithm will
          attempt to remove all sinks it encounters,
          whether they are real or spurious. This is the default.NO_ENFORCE-No
          sinks will be filled. ENFORCE_WITH_SINK-Points identified as
          sinks in Input feature
          data represent known topographic depressions and will not be altered.
          Any sink not identified in input feature data is considered spurious,
          and the algorithm will attempt to fill it. Having more than
          8,000 spurious sinks causes the tool to fail.
      data_type {String}:
          The dominant elevation data type of the input feature data.CONTOUR-The
          dominant type of input data will be elevation contours.
          This is the default.SPOT-The dominant type of input will be
          point.Specifying the relevant selection optimizes the search method
          used
          during the generation of streams and ridges.
      maximum_iterations {Long}:
          The maximum number of interpolation iterations.The number of
          iterations must be greater than zero. A default of 20 is
          normally adequate for both contour and line data.A value of 30 will
          clear fewer sinks. Rarely, higher values (45-50)
          may be useful to clear more sinks or to set more ridges and streams.
          Iteration ceases for each grid resolution when the maximum number of
          iterations has been reached.
      roughness_penalty {Double}:
          The integrated squared second derivative as a measure of roughness.The
          roughness penalty must be zero or greater. If the primary input
          data type is CONTOUR, the default is zero. If the primary data type is
          SPOT, the default is 0.5. Larger values are not normally recommended.
      discrete_error_factor {Double}:
          The discrete error factor is used to adjust the amount of smoothing
          when converting the input data to a raster.The value must be greater
          than zero. The normal range of adjustment is
          0.25 to 4, and the default is 1. A smaller value results in less data
          smoothing; a larger value causes greater smoothing.
      vertical_standard_error {Double}:
          The amount of random error in the z-values of the input data.The value
          must be zero or greater. The default is zero.The vertical standard
          error may be set to a small positive value if
          the data has significant random (non-systematic) vertical errors with
          uniform variance. In this case, set the vertical standard error to the
          standard deviation of these errors. For most elevation datasets, the
          vertical error should be set to zero, but it may be set to a small
          positive value to stabilize convergence when rasterizing point data
          with stream line data.
      tolerance_1 {Double}:
          This tolerance reflects the accuracy and density of the elevation
          points in relation to surface drainage.For point datasets, set the
          tolerance to the standard error of the
          data heights. For contour datasets, use one-half the average contour
          interval.The value must be zero or greater. The default is 2.5 if the
          data type
          is CONTOUR and zero if the data type is SPOT.
      tolerance_2 {Double}:
          This tolerance prevents drainage clearance through unrealistically
          high barriers.The value must be greater than zero. The default is 100
          if the data
          type is CONTOUR and 200 if the data type is SPOT.
      profile_penalty {Double}:
          The profile curvature roughness penalty is a locally adaptive penalty
          that can be used to partly replace total curvature.It can yield good
          results with high-quality contour data but can lead
          to instability in convergence with poor data. Set to 0.0 for no
          profile curvature (the default), set to 0.5 for moderate profile
          curvature, and set to 0.8 for maximum profile curvature. Values larger
          than 0.8 are not recommended and should not be used.

     OUTPUTS:
      out_surface_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point
          raster.
      out_stream_features {Feature Class}:
          The output line feature class of stream polyline features and ridge
          line features.The line features are created at the beginning of the
          interpolation
          process. It provides the general morphology of the surface for
          interpolation. It can be used to verify correct drainage and
          morphology by comparing known stream and ridge data.The polyline
          features are coded as follows:1. Input stream line not over cliff.2.
          Input stream line over cliff (waterfall).3. Drainage enforcement
          clearing a spurious sink.4. Stream line determined from contour
          corner.5. Ridge line determined from contour corner.6. Code not
          used.7. Data stream line side conditions.8. Code not used.9. Line
          indicating large elevation data clearance.
      out_sink_features {Feature Class}:
          The output point feature class of the remaining sink point
          features.These are the sinks that were not specified in the sink input
          feature
          data and were not cleared during drainage enforcement. Adjusting the
          values of the tolerances, tolerance_1 and tolerance_2, can reduce the
          number of remaining sinks. Remaining sinks often indicate errors in
          the input data that the drainage enforcement algorithm could not
          resolve. This can be an efficient way of detecting subtle elevation
          errors.
      out_diagnostic_file {File}:
          The output diagnostic file listing all inputs and parameters used and
          the number of sinks cleared at each resolution and iteration.
      out_parameter_file {File}:
          The output parameter file listing all inputs and parameters used,
          which can be used with Topo to Raster by File to run the interpolation
          again.
      out_residual_feature {Feature Class}:
          The output point feature class of all the large elevation residuals as
          scaled by the local discretisation error.All the scaled residuals
          larger than 10 should be inspected for
          possible errors in input elevation and stream data. Large-scaled
          residuals indicate conflicts between input elevation data and
          streamline data. These may also be associated with poor automatic
          drainage enforcements. These conflicts can be remedied by providing
          additional streamline and/or point elevation data after first checking
          and correcting errors in existing input data. Large unscaled residuals
          usually indicate input elevation errors.
      out_stream_cliff_error_feature {Feature Class}:
          The output point feature class of locations where possible stream and
          cliff errors occur.The locations where the streams have closed loops,
          distributaries, and
          streams over cliffs can be identified from the point feature class.
          Cliffs with neighboring cells that are inconsistent with the high and
          low sides of the cliff are also indicated. This can be a good
          indicator of cliffs with incorrect direction.Points are coded as
          follows:1. True circuit in data streamline network.2. Circuit in
          stream network as encoded on the out raster.3. Circuit in stream
          network via connecting lakes.4. Distributaries point.5. Stream over a
          cliff (waterfall).6. Points indicating multiple stream outflows from
          lakes.7. Code not used.8. Points beside cliffs with heights
          inconsistent with cliff
          direction.9. Code not used.10. Circular distributary removed.11.
          Distributary with no inflowing stream.12. Rasterized distributary in
          output cell different to where the data
          stream line distributary occurs.13. Error processing side
          conditions-an indicator of very complex
          streamline data.
      out_contour_error_feature {Feature Class}:
          The output point feature class of possible errors pertaining to the
          input contour data.Contours with bias in height exceeding five times
          the standard
          deviation of the contour values as represented on the output raster
          are reported to this feature class. Contours that join other contours
          with a different elevation are flagged in this feature class by the
          code 1; this is a sure sign of a contour label error.

        """