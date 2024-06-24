# Generated documentation for module arcpy.management


class CreateRasterDataset(object):
    """
    Creates an empty raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        CreateRasterDataset_management(out_path, out_name, {cellsize}, pixel_type, {raster_spatial_reference}, number_of_bands, {config_keyword}, {pyramids}, {tile_size}, {compression}, {pyramid_origin})

        Creates an empty raster dataset.

     INPUTS:
      out_path (Workspace):
          The folder or geodatabase where the raster dataset will be stored.
      out_name (String):
          The name, location, and format for the newly created dataset.When
          storing the raster dataset in a file format, specify the file
          extension as follows:.bil for Esri BIL.bip for Esri BIP.bmp for
          BMP.bsq for Esri BSQ.crf
          for CRF.dat for ENVI DAT.gif for GIF.img for ERDAS IMAGINE.jpg for
          JPEG.jp2 for JPEG 2000.png for PNG.tif for TIFFNo extension for Esri
          GridWhen storing a raster dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset. When storing a
          raster dataset to a JPEG format file, a JPEG
          2000 format file, a TIFF format file, or a geodatabase, you can
          specifyandvalues in the geoprocessing environments. Compression
          TypeCompression Quality
      cellsize {Double}:
          The pixel size that will be used for the new raster dataset.
      pixel_type (String):
          The bit depth (radiometric resolution) of the output raster dataset.
          If this is not specified, the raster dataset will be created with a
          default pixel type of 8-bit unsigned integer.Not all data types are
          supported by all raster formats. Check the List
          of supported sensors help topic to ensure that the format you are
          using will support the necessary data type.1_BIT-The pixel type will
          be a 1-bit unsigned integer. The values can
          be 0 or 1.2_BIT-The pixel type will be a 2-bit unsigned integer. The
          values
          supported can range from 0 to 3.4_BIT-The pixel type will be a 4-bit
          unsigned integer. The values
          supported can range from 0 to 15.8_BIT_UNSIGNED-The pixel type will be
          an unsigned 8-bit data type. The
          values supported can range from 0 to 255.8_BIT_SIGNED-The pixel type
          will be a signed 8-bit data type. The
          values supported can range from -128 to 127.16_BIT_UNSIGNED-The pixel
          type will be a 16-bit unsigned data type.
          The values can range from 0 to 65,535.16_BIT_SIGNED-The pixel type
          will be a 16-bit signed data type. The
          values can range from -32,768 to 32,767.32_BIT_UNSIGNED-The pixel type
          will be a 32-bit unsigned data type.
          The values can range from 0 to 4,294,967,295.32_BIT_SIGNED-The pixel
          type will be a 32-bit signed data type. The
          values can range from -2,147,483,648 to 2,147,483,647.32_BIT_FLOAT-The
          pixel type will be a 32-bit data type supporting
          decimals.64_BIT-The pixel type will be a 64-bit data type supporting
          decimals.
      raster_spatial_reference {Coordinate System}:
          The coordinate system for the output raster dataset.If this is not
          specified, the coordinate system set in the environment
          settings will be used.
      number_of_bands (Long):
          The number of bands of the output raster dataset.
      config_keyword {String}:
          The storage parameters (configuration) for a file or enterprise
          geodatabase. Configuration keywords are set up by your database
          administrator.
      pyramids {Pyramid}:
          Creates pyramids.For Pyramid Levels, specify a number of -1 or higher.
          A value of 0
          will not create pyramids, and a value of -1 will automatically
          determine the correct number of pyramid layers to create.Pyramid
          Resampling Technique defines how the data will be resampled
          when creating the pyramids.NEAREST-Use nearest neighbor for nominal
          data or raster datasets with
          color maps, such as land-use or pseudo color images.BILINEAR-Use
          bilinear interpolation with continuous data, such as
          satellite imagery or aerial photography.CUBIC-Use cubic convolution
          with continuous data, such as satellite
          imagery or aerial photography. It is similar to bilinear
          interpolation; however, it resamples the data using a larger
          matrix.Pyramid Compression Type defines the method used when
          compressing the
          pyramids.DEFAULT-The compression that is normally used by the raster
          dataset
          format will be used.LZ77-A lossless compression will be used. The
          values of the cells in
          the raster will not be changed.JPEG-A lossy compression will be
          used.NONE-No data compression will be used.
      tile_size {Tile Size}:
          The size of the tiles.The tile width controls the number of pixels
          that can be stored in
          each tile. This is specified as a number of pixels in x. The default
          tile width is 128.The tile height controls the number of pixels that
          can be stored in
          each tile. This is specified as a number of pixels in y. The default
          tile height is 128.Only geodatabases and enterprise geodatabases use
          tile size.
      compression {Compression}:
          Specifies the type of compression that will be used to store the
          raster dataset.LZ77-Lossless compression that preserves all raster
          cell values will
          be used.JPEG-Lossy compression that uses the public JPEG compression
          algorithm
          will be used. If you choose JPEG, you can also specify the compression
          quality. The valid compression quality value ranges are from 0 to 100.
          This compression can be used for .jpg files and .tif files.JPEG
          2000-Lossy compression will be used.PACKBITS-PackBits compression will
          be used for .tif files.LZW-Lossless compression that preserves all
          raster cell values will be
          used.RLE-Run-length encoding will be used for .img files.CCITT GROUP
          3-Lossless compression for 1-bit data will be used.CCITT GROUP
          4-Lossless compression for 1-bit data will be used.CCITT_1D-Lossless
          compression for 1-bit data will be used.NONE-No compression will be
          used. This is the default.
      pyramid_origin {Point}:
          The origination location of the raster pyramid. It is recommended that
          you specify this point if you plan to build large mosaics in a file
          geodatabase or enterprise geodatabase, especially if you plan to
          mosaic them over time (for example, when updating).Set the pyramid
          reference point at the upper left corner of the raster
          dataset.In setting this point for a file geodatabase or enterprise
          geodatabase, partial pyramiding will be used when updating with a new
          mosaicked raster dataset. Partial pyramiding updates the parts of the
          pyramid that do not exist due to the new mosaicked datasets. It is a
          good practice to set a pyramid reference point so that the entire
          raster mosaic will be below and to the right of this point. However, a
          pyramid reference point should not be set too large either.

        """