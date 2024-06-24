# Generated documentation for module arcpy.sa.Functions


class TopoToRasterByFile(object):
    """
    Interpolates a hydrologically correct raster surface from point, line, and polygon data using parameters specified in a file.
    """

    @property
    def description(self) -> str:
        return """

        TopoToRasterByFile_sa(in_parameter_file, {out_stream_features}, {out_sink_features}, {out_residual_feature}, {out_stream_cliff_error_feature}, {out_contour_error_feature})

        Interpolates a hydrologically correct raster surface from point, line,
        and polygon data using parameters specified in a file.

     INPUTS:
      in_parameter_file (File):
          The input ASCII text file containing the inputs and parameters to use
          for the interpolation.The file is typically created from a previous
          run of Topo to Raster
          with the optional output parameter file specified.In order to test the
          outcome of changing the parameters, it is easier
          to make edits to this file and rerun the interpolation than to
          correctly issue the Topo to Raster tool each time.

     OUTPUTS:
      out_surface_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point
          raster.
      out_stream_features {Feature Class}:
          Output feature class of stream polyline features.The polyline features
          are coded as follows:1. Input stream line not over cliff.2. Input
          stream line over cliff (waterfall).3. Drainage enforcement clearing a
          spurious sink.4. Stream line determined from contour corner.5. Ridge
          line determined from contour corner.6. Code not used.7. Data stream
          line side conditions.8. Code not used.9. Line indicating large
          elevation data clearance.
      out_sink_features {Feature Class}:
          Output feature class of remaining sink point features.
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