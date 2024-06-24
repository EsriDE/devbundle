# Generated documentation for module arcpy.conversion


class LasDatasetToRaster(object):
    """
    Creates a raster using elevation, intensity, or RGB values stored in the lidar points referenced by the LAS dataset.
    """

    @property
    def description(self) -> str:
        return """

        LasDatasetToRaster_conversion(in_las_dataset, out_raster, {value_field}, {interpolation_type}, {data_type}, {sampling_type}, {sampling_value}, {z_factor})

        Creates a raster using elevation, intensity, or RGB values stored in
        the lidar points referenced by the LAS dataset.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset that will be processed.
      value_field {String}:
          The lidar data that will be used to generate the raster
          output.ELEVATION-Elevation from the lidar files will be used to create
          the
          raster. This is the default.INTENSITY-Intensity information from the
          lidar files will be used to
          create the raster.RGB-RGB values from the lidar points will be used to
          create 3-band
          imagery.
      interpolation_type {Interpolate}:
          The interpolation technique that will be used to determine the cell
          values of the output raster. The binning approach provides afor
          determining each output
          cell using the points that fall within its extent, along with ato
          determine the value of cells that do not contain any LAS points.
          Cell Assignment MethodVoid Fill MethodCell Assignment
          MethodsAVERAGE-Assigns the average value of all points in the cell.
          This is
          the default.MINIMUM-Assigns the minimum value found in the points
          within the cell.MAXIMUM-Assigns the maximum value found in the points
          within the cell.IDW-Uses Inverse Distance Weighted interpolation to
          determine the cell
          value.NEAREST-Uses Nearest Neighbor assignment to determine the cell
          value.Void Fill MethodsNONE-NoData is assigned to the
          cell.SIMPLE-Averages the values from
          data cells immediately surrounding a
          NoData cell to eliminate small voids.LINEAR-Triangulates across void
          areas and uses linear interpolation on
          the triangulated value to determine the cell value. This is the
          default.NATURAL_NEIGHBOR-Uses natural neighbor interpolation to
          determine the
          cell value. Theinterpolation methods derive cell values using a
          TIN based
          approach while also offering the opportunity to speed up processing
          time by thinning the sampling of LAS data using the Window Size
          technique. TriangulationTriangulation MethodsLinear-Uses linear
          interpolation to determine cell values.Natural
          Neighbors-Uses natural neighbor interpolation to determine
          cell value.Window Size Selection MethodsMaximum-The point with the
          highest value in each window size is
          maintained. This is the default.Minimum-The point with the lowest
          value in each window size is
          maintained.Closest To Mean-The point whose value is closest to the
          average of all
          point values in the window size is maintained.
      data_type {String}:
          Specifies the type of numeric values that will be stored in the output
          raster.FLOAT-The output raster will use 32-bit floating point, which
          supports
          values ranging from -3.402823466e+38 to 3.402823466e+38. This is the
          default.INT-The output raster will use an appropriate integer bit
          depth. This
          option will round z-values to the nearest whole number and write an
          integer to each raster cell value.
      sampling_type {String}:
          Specifies how theparameter will be interpreted to define the
          output raster's cell size. Sampling Value
          OBSERVATIONS-Thewill define the number of columns or rows in
          the output raster based on whichever is longest. The cell size will be
          derived by dividing the longest side of the output's extent with the
          input in theparameter. If an observation value of 3000 is used on a
          dataset whose longest side is 23.67 kilometers, the output raster's
          resolution will be 7.89 meters. This method offers a helpful way of
          creating an output with a predictable size that can be generated
          rapidly. Sampling ValueSampling Value         CELLSIZE-The
          cell size will be directly defined by
          theparameter. This is the default. Sampling Value
      sampling_value {Double}:
          The value used in conjunction with theparameter to define the
          output raster's cell size. Sampling Type
      z_factor {Double}:
          The factor by which z-values will be multiplied. This is typically
          used to convert z linear units to match x,y linear units. The default
          is 1, which leaves elevation values unchanged. This parameter is not
          available if the spatial reference of the input surface has a z-datum
          with a specified linear unit.

     OUTPUTS:
      out_raster (Raster Dataset):
          The location and name of the output raster. When storing a raster
          dataset in a geodatabase or in a folder such as an Esri Grid, do not
          add a file extension to the name of the raster dataset. A file
          extension can be provided to define the raster's format when storing
          it in a folder, such as .tif to generate a GeoTIFF or .img to generate
          an ERDAS IMAGINE format file.If the raster is stored as a .tif file or
          in a geodatabase, the raster
          compression type and quality can be specified using geoprocessing
          environment settings.

        """