# Generated documentation for module arcpy.management


class CreateRandomRaster(object):
    """
    Creates a raster dataset of random values with a distribution you define.
    """

    @property
    def description(self) -> str:
        return """

        CreateRandomRaster_management(out_path, out_name, {distribution}, {raster_extent}, {cellsize}, {build_rat})

        Creates a raster dataset of random values with a distribution you
        define.

     INPUTS:
      out_path (Workspace):
          The folder or geodatabase where the output raster dataset will be
          stored.
      out_name (String):
          The name and format of the raster dataset you are creating.To store
          the output as a raster dataset in a geodatabase, do not add a
          file extension to the raster dataset name.For file-based rasters, use
          the appropriate extension to specify the
          format to create as follows:.tif-TIFF raster.img-ERDAS IMAGINE
          raster.crf-CRF rasterNo
          extension-Esri Grid
      distribution {String}:
          Specifies the random value distribution method to use.Each type has
          one or two settings to control the distribution.UNIFORM {Minimum},
          {Maximum}-A uniform distribution with the defined
          range. The default values are 0.0 for {Minimum} and 1.0 for {Maximum}.
          Both values are of type double.INTEGER {Minimum}, {Maximum}-An integer
          distribution with the defined
          range. The default values are 1 for {Minimum} and 10 for {Maximum}.
          Both values are of type long.NORMAL {Mean}, {Standard Deviation}-A
          normal distribution with defined
          {Mean} and {Standard Deviation} values. The default values are 0.0 for
          {Mean} and 1.0 for {Standard Deviation}. Both values are of type
          double.EXPONENTIAL {Mean}-An exponential distribution with a defined
          {Mean}
          value. The default value is 1.0. The value is of type double.POISSON
          {Mean}-A Poisson distribution with a defined {Mean} value. The
          default value is 1.0. The value is of type double.GAMMA {Alpha},
          {Beta}-A gamma distribution with defined {Alpha} and
          {Beta} values. The default values are 1.0 for {Alpha} and 1.0 for
          {Beta}. Both values are of type double.BINOMIAL {N}, {Probability}-A
          binomial distribution with defined {N}
          and {Probability} values. The {N} value is of type long with a default
          of 10. The {Probability} value is of type double with a default of
          0.5.GEOMETRIC {Probability}-A geometric distribution with a defined
          {Probability} value. The default value is 0.5. The value is of type
          double.NEGATIVE BINOMIAL {r}, {Probability}-A Pascal distribution with
          defined {r} and {Probability} values. The {r} value is of type double
          with a default of 10.0. The {Probability} value is of type double with
          a default of 0.5.
      raster_extent {Extent}:
          The extent of the output raster dataset.MAXOF-The maximum extent of
          all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      cellsize {Double}:
          The spatial resolution of the output raster dataset.
      build_rat {Boolean}:
          Specifies whether the tool will unconditionally build a raster
          attribute table for the output raster in which the selected
          distribution results in an integer output raster.This parameter has no
          effect if the output raster is floating point.BUILD-A raster attribute
          table will be unconditionally built for
          integer output rasters. This is the default.DO_NOT_BUILD-A raster
          attribute table will not be built for integer
          output rasters if the number of unique values is greater than or equal
          to 65535. If the number of unique values is less than 65535, a raster
          attribute table will be built.

        """