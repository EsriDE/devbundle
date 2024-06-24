# Generated documentation for module arcpy.management


class SplitRaster(object):
    """
    Divides a raster dataset into smaller pieces, by tiles or features from a polygon.
    """

    @property
    def description(self) -> str:
        return """

        SplitRaster_management(in_raster, out_folder, out_base_name, split_method, format, {resampling_type}, {num_rasters}, {tile_size}, {overlap}, {units}, {cell_size}, {origin}, {split_polygon_feature_class}, {clip_type}, {template_extent}, {nodata_value})

        Divides a raster dataset into smaller pieces, by tiles or features
        from a polygon.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Layer):
          The raster to split.
      out_folder (Folder):
          The destination for the new raster datasets.
      out_base_name (String):
          The prefix for each of the raster datasets you will create. A number
          will be appended to each prefix, starting with 0.
      split_method (String):
          Determines how to split the raster dataset.SIZE_OF_TILE-Specify the
          width and height of the tile.NUMBER_OF_TILES-
          Specify the number of raster tiles to create by
          breaking the dataset into a number of columns and
          rows.POLYGON_FEATURES-Use the individual polygon geometries in a
          feature
          class to split the raster.
      format (String):
          The format for the output raster datasets.TIFF-Tagged Image File
          Format. This is the default.BMP-Microsoft
          Bitmap.ENVI-ENVI DAT.Esri BIL-Esri Band Interleaved by Line.Esri
          BIP-Esri Band Interleaved by Pixel.Esri BSQ-Esri Band
          Sequential.GIF-Graphic Interchange Format.GRID-Esri Grid.IMAGINE
          IMAGE-ERDAS IMAGINE.JP2-JPEG 2000.JPEG-Joint Photographic Experts
          Group.PNG-Portable Network Graphics.
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
      num_rasters {Point}:
          The number of columns (x) and rows (y) to split the raster dataset
          into. This is a point whose X and Y coordinates define number of rows
          and columns. The X coordinate is the number of columns and the Y
          coordinate is the number of rows.
      tile_size {Point}:
          The x and y dimensions of the output tiles. The default unit of
          measurement is in pixels. You can change this with the units
          parameter. This is a point whose X and Y coordinates define the
          dimensions of output tiles. The X coordinate is the horizontal
          dimension of the output and the Y coordinate is the vertical dimension
          of the output.
      overlap {Double}:
          The tiles do not have to line up perfectly; set the amount of overlap
          between tiles with this parameter. The default unit of measurement is
          in pixels. You can change this with the units parameter.
      units {String}:
          Set the units of measurement for the tile_size and the overlap
          parameters.PIXELS-The unit is in pixels. This is the
          default.METERS-The unit is
          in meters.FEET-The unit is in feet.DEGREES-The unit is in decimal
          degrees.MILES-The unit is in miles.KILOMETERS-The unit is in
          kilometers.
      cell_size {Point}:
          The spatial resolution of the output raster. If left blank, the output
          cell size will match the input raster. When you change the cell size
          values, the tile size is reset to the image size and the tile count is
          reset to 1.
      origin {Point}:
          Change the coordinates for the lower left origin point, where the
          tiling scheme will begin. If left blank, the lower left origin would
          be the same as the input raster.
      split_polygon_feature_class {Feature Layer}:
          A feature class that will be used to split the raster dataset.
      clip_type {String}:
          Limits the extent of your raster dataset before you split it.NONE-Use
          the full extent of the input raster dataset.EXTENT-Specify
          bounding box as your clipping boundary.FEATURE_CLASS-Specify a feature
          class to clip the extent.
      template_extent {Extent}:
          An extent or a dataset used to define the clipping boundary. The
          dataset can be a raster or feature class.MAXOF-The maximum extent of
          all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      nodata_value {String}:
          All the pixels with the specified value will be set toin the
          output raster dataset. NoData

        """