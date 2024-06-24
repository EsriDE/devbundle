# Generated documentation for module arcpy.management


class RasterToDTED(object):
    """
    Splits a raster dataset into separate files based on the DTED tiling structure.
    """

    @property
    def description(self) -> str:
        return """

        RasterToDTED_management(in_raster, out_folder, dted_level, {resampling_type})

        Splits a raster dataset into separate files based on the DTED tiling
        structure.

     INPUTS:
      in_raster (Raster Layer):
          Select a single band raster dataset that represents elevation.
      out_folder (Folder):
          Select a destination where the folder structure and DTED files will be
          created.
      dted_level (String):
          Select an appropriate level based on the resolution of your elevation
          data.DTED_0-900 mDTED_1-90 mDTED_2-30 m
      resampling_type {String}:
          Choose an appropriate technique based on the type of data you
          have.NEAREST-The fastest resampling method, and it minimizes changes
          to
          pixel values. Suitable for discrete data, such as land
          cover.BILINEAR-Calculates the value of each pixel by averaging
          (weighted for
          distance) the values of the surrounding 4 pixels. Suitable for
          continuous data.CUBIC-Calculates the value of each pixel by fitting a
          smooth curve
          based on the surrounding 16 pixels. Produces the smoothest image, but
          can create values outside of the range found in the source data.
          Suitable for continuous data.

        """