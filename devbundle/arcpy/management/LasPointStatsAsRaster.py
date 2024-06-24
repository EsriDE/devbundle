# Generated documentation for module arcpy.management


class LasPointStatsAsRaster(object):
    """
    Creates a raster whose cell values reflect statistical information about LAS points.
    """

    @property
    def description(self) -> str:
        return """

        LasPointStatsAsRaster_management(in_las_dataset, out_raster, {method}, {sampling_type}, {sampling_value})

        Creates a raster whose cell values reflect statistical information
        about LAS points.

     INPUTS:
      in_las_dataset (LAS Dataset Layer):
          The LAS dataset that will be processed.
      method {String}:
          Specifies the type of statistics that will be collected about the LAS
          points in each cell of the output raster.PULSE_COUNT-The number of
          last return points will be
          collected.POINT_COUNT-The number of points from all returns will be
          collected.PREDOMINANT_LAST_RETURN-The most frequent last return value
          will be
          collected.PREDOMINANT_CLASS-The most frequent class code will be
          collected.INTENSITY_RANGE-The range of intensity values will be
          collected.Z_RANGE-The range of elevation values will be collected.
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