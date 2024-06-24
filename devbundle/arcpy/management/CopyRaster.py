# Generated documentation for module arcpy.management


class CopyRaster(object):
    """
    Saves a copy of a raster dataset or converts a mosaic dataset into a single raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        CopyRaster_management(in_raster, out_rasterdataset, {config_keyword}, {background_value}, {nodata_value}, {onebit_to_eightbit}, {colormap_to_RGB}, {pixel_type}, {scale_pixel_value}, {RGB_to_Colormap}, {format}, {transform}, {process_as_multidimensional}, {build_multidimensional_transpose})

        Saves a copy of a raster dataset or converts a mosaic dataset into a
        single raster dataset.

     INPUTS:
      in_raster (Raster Dataset / Mosaic Dataset / Mosaic Layer / Raster Layer / File / Image Service):
          The raster dataset or mosaic dataset to be copied.
      config_keyword {String}:
          The storage parameters (configuration) for a geodatabase.
          Configuration keywords are set up by your database administrator.
      background_value {Double}:
          Remove the unwanted values created around the raster data. The value
          specified will be distinguished from other valuable data in the raster
          dataset. For example, a value of zero along the raster dataset's
          borders will be distinguished from zero values in the raster
          dataset.The pixel value specified will be set to NoData in the output
          raster
          dataset. For file-based rasters,must be set to the same value
          asfor the
          background value to be ignored. Enterprise and geodatabase rasters
          will work without this extra step. Ignore Background
          ValueNoData Value
      nodata_value {String}:
          All the pixels with the specified value will be set toin the
          output raster dataset. NoData
      onebit_to_eightbit {Boolean}:
          Specifies whether the input 1-bit raster dataset will be converted to
          an 8-bit raster dataset. In this conversion, the value 1 in the input
          raster dataset will be changed to 255 in the output raster dataset.
          This is useful when importing a 1-bit raster dataset to a geodatabase.
          One-bit raster datasets have 8-bit pyramid layers when stored in a
          file system, but in a geodatabase, 1-bit raster datasets can only have
          1-bit pyramid layers, which results in a lower-quality display. By
          converting the data to 8 bit in a geodatabase, the pyramid layers are
          built as 8 bit instead of 1 bit, resulting in a proper raster dataset
          in the display.NONE-No conversion will occur. This is the
          default.OneBitTo8Bit-The
          input raster will be converted.
      colormap_to_RGB {Boolean}:
          Specifies whether the input raster dataset will be converted to a
          three-band output raster dataset if the input raster dataset includes
          a color map. This is useful when mosaicking rasters with different
          color maps.NONE-No conversion will occur. This is the
          default.ColormapToRGB-The
          input dataset will be converted.
      pixel_type {String}:
          Specifies the bit depth, or radiometric resolution, that will be used
          for the raster or mosaic dataset. If not defined, the value from the
          first raster dataset will be used.1_BIT-The pixel type will be a 1-bit
          unsigned integer. The values can
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
      scale_pixel_value {Boolean}:
          Specifies whether pixel values will be scaled. When the output is a
          pixel type other than the input (such as 16 bit to 8 bit), you can
          scale the values to fit into the new range; otherwise, the values that
          do not fit into the new pixel range will be discarded.If scaling up,
          such as 8 bit to 16 bit, the minimum and maximum of the
          8-bit values will be scaled to the minimum and maximum in the 16-bit
          range. If scaling down, such as 16 bit to 8 bit, the minimum and
          maximum of the 16-bit values will be scaled to the minimum and maximum
          in the 8-bit range.NONE-The pixel values will remain the same and will
          not be scaled. Any
          values that do not fit within the value range will be discarded. This
          is the default.ScalePixelValue-The pixel values will be scaled to the
          new pixel type.
          When you scale the pixel depth, the raster will display the same, but
          the values will be scaled to the new bit depth that was specified.
      RGB_to_Colormap {Boolean}:
          Specifies whether an 8-bit, 3-band (RGB) raster dataset will be
          converted to a single-band raster dataset with a color map. This
          operation suppresses noise that is often found in scanned images and
          is ideal for screen captures, scanned maps, or scanned documents. This
          is not recommended for satellite or aerial imagery or thematic raster
          data.NONE-The RGB raster dataset will not be
          converted.RGBToColormap-The
          RGB raster dataset will be converted to a color map.
      format {String}:
          Specifies the output raster format.TIFF-The output format will be
          TIFF.COG-The output format will be
          Cloud Optimized GeoTIFF.IMAGINE Image-The output format will be ERDAS
          IMAGINE.BMP-The output format will be BMP.GIF-The output format will
          be GIF.PNG-The output format will be PNG.JPEG-The output format will
          be JPEG.JP2-The output format will be JPEG 2000.GRID-The output format
          will be Esri Grid.BIL-The output format will be Esri BIL.BSQ-The
          output format will be Esri BSQ.BIP-The output format will be Esri
          BIP.ENVI-The output format will be ENVI DAT.CRF-The output format will
          be CRF.MRF-The output format will be MRF.NetCDF-The output format will
          be NetCDF.ZARR-The output format will be Zarr.
      transform {Boolean}:
          Specifies whether a transformation associated with the input raster
          will be applied to the output. The input raster can have a
          transformation associated with it that is not saved in the input, such
          as a world file or a geometric function.NONE-No associated
          transformation will be applied to the
          output.Transform-Any associated transformation will be applied to the
          output.
      process_as_multidimensional {Boolean}:
          Specifies whether the input mosaic dataset will be processed as a
          multidimensional raster dataset.CURRENT_SLICE-The input will not be
          processed as a multidimensional
          raster dataset. If the input is multidimensional, only the slice that
          is currently displayed will be processed. This is the
          default.ALL_SLICES-The input will be processed as a multidimensional
          raster
          dataset and all slices will be processed to produce a new
          multidimensional raster dataset. Set the format parameter to CRF to
          use this option.
      build_multidimensional_transpose {Boolean}:
          Specifies whether the transpose for the input multidimensional raster
          dataset will be built, which will chunk the data along each dimension
          to optimize performance when accessing pixel values across all
          slices.NO_TRANSPOSE-No transpose will be built. This is the
          default.TRANSPOSE-The input multidimensional raster dataset will be
          transposed. The process_as_multidimensional parameter must be set to
          ALL_SLICES to use this option.

     OUTPUTS:
      out_rasterdataset (Raster Dataset):
          The name and format for the raster dataset being created..bil-Esri
          BIL.bip-Esri BIP.bmp-BMP.bsq-Esri BSQ.crf-CRF.dat-ENVI
          DAT.img-ERDAS IMAGINE.gif-GIF.jpg-JPEG.jp2-JPEG
          2000.mrf-MRF.nc-NetCDF.png-PNG.tif-TIFF and Cloud Optimized
          GeoTIFF.zarr-ZarrNo extension for Esri GridWhen storing a raster
          dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset.When storing a raster
          dataset to JPEG, JPEG 2000, or TIFF format, or
          to a geodatabase, you can specify a compression type and compression
          quality.

        """