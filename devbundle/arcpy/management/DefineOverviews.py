# Generated documentation for module arcpy.management


class DefineOverviews(object):
    """
    Lets you set how mosaic dataset overviews are generated. The settings made with this tool are used by the Build Overviews tool.
    """

    @property
    def description(self) -> str:
        return """

        DefineOverviews_management(in_mosaic_dataset, {overview_image_folder}, {in_template_dataset}, {extent}, {pixel_size}, {number_of_levels}, {tile_rows}, {tile_cols}, {overview_factor}, {force_overview_tiles}, {resampling_method}, {compression_method}, {compression_quality})

        Lets you set how mosaic dataset overviews are generated. The settings
        made with this tool are used by the Build Overviews tool.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to build overviews on.
      overview_image_folder {Workspace}:
          The folder or geodatabase to store the overviews.
      in_template_dataset {Raster Layer / Feature Layer}:
          A raster dataset or feature class to define the extent of the
          overviews.
      extent {Envelope}:
          Set the extent using minimum and maximum x and y coordinates.This is
          specified as space delimited in the following order: X-minimum
          X-maximum Y-minimum Y-maximum.The mosaic dataset boundary will
          determine the extent of the overviews
          if you do not define an extent.
      pixel_size {Double}:
          If you prefer not to use all the raster's pyramids, specify a base
          pixel size at which your overviews will be generated.The units for
          this parameter are the same as the spatial reference of
          the mosaic dataset.
      number_of_levels {Long}:
          Specify the number of levels of overviews that you want to generate
          overviews. A value of -1 will determine an optimal value for you.
      tile_rows {Long}:
          Set the number of rows (in pixels) for each tile.Larger values will
          result in fewer, larger individual overviews, and
          increase the likelihood that you will need to regenerate lower level
          overviews. A smaller value will result in more, smaller files.
      tile_cols {Long}:
          Set the number of columns (in pixels) for each tile.Larger values will
          result in fewer, larger individual overviews, and
          increase the likelihood that you will need to regenerate lower level
          overviews. A smaller value will result in more, smaller files.
      overview_factor {Long}:
          Set a ratio to determine the size of the next overview. For example,
          if the cell size of the first level is 10, and the overview factor is
          3, then the next overview pixel size will be 30.
      force_overview_tiles {Boolean}:
          Generate overviews at all levels, or only above existing pyramid
          levels.NO_FORCE_OVERVIEW_TILES-Create overviews above the raster
          pyramid
          levels. This is the default.FORCE_OVERVIEW_TILES-Create overviews at
          all levels.
      resampling_method {String}:
          Choose an algorithm for aggregating pixel values in the overviews.
          NEAREST-The fastest resampling method because it minimizes
          changes to pixel values. Suitable for discrete data, such as land
          cover. If theis thematic, then nearest neighbor will be the default.
          Raster MetadataData Type         BILINEAR-Calculates the value of each
          pixel by averaging
          (weighted for distance) the values of the surrounding 4 pixels.
          Suitable for continuous data. This is the default,
          unless theis thematic. Raster
          MetadataData TypeCUBIC-Calculates the value of each pixel by fitting
          a smooth curve
          based on the surrounding 16 pixels. Produces the smoothest image, but
          can create values outside of the range found in the source data.
          Suitable for continuous data.
      compression_method {String}:
          Define the type of data compression to store the overview images.
          JPEG-A lossy compression. This is the default, unless theis
          thematic. Raster MetadataData TypeThis compression method is
          only valid if the mosaic dataset items
          adhere to JPEG specifications.JPEG_YCbCr-A lossy compression using the
          luma (Y) and chroma (Cb and
          Cr) color space components.None-No data compression. LZW-A
          lossless compression. If theis thematic, then nearest
          neighbor will be the default. Raster MetadataData Type
      compression_quality {Long}:
          Choose a value from 1 - 100. Higher values generate better quality
          outputs, but they create larger files.

        """