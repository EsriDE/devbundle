# Generated documentation for module arcpy.management


class MosaicToNewRaster(object):
    """
    Merges multiple raster datasets into a new raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        MosaicToNewRaster_management(input_rasters;input_rasters..., output_location, raster_dataset_name_with_extension, {coordinate_system_for_the_raster}, {pixel_type}, {cellsize}, number_of_bands, {mosaic_method}, {mosaic_colormap_mode})

        Merges multiple raster datasets into a new raster dataset.

     INPUTS:
      input_rasters (Mosaic Dataset / Raster Dataset / Raster Layer):
          The raster datasets that you want to merge together. The inputs must
          have the same number of bands and same bit depth.
      output_location (Workspace):
          The folder or geodatabase to store the raster.
      raster_dataset_name_with_extension (String):
          The name of the dataset you are creating.When storing the raster
          dataset in a file format, specify the file
          extension as follows:.bil-Esri BIL.bip-Esri BIP.bmp-BMP.bsq-Esri
          BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFFNo extension for Esri GridWhen storing a raster
          dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset. When storing a
          raster dataset to a JPEG format file, a JPEG
          2000 format file, a TIFF format file, or a geodatabase, you can
          specifyandvalues in the geoprocessing environments. Compression
          TypeCompression Quality
      coordinate_system_for_the_raster {Coordinate System}:
          The coordinate system for the output raster dataset.
      pixel_type {String}:
          The bit depth, or radiometric resolution of the mosaic dataset.If you
          do not set the pixel type, the 8-bit default will be used and
          your output may be incorrect.1_BIT-The pixel type will be a 1-bit
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
      cellsize {Double}:
          The pixel size that will be used for the new raster dataset.
      number_of_bands (Long):
          The number of bands that the output raster will have.
      mosaic_method {String}:
          The method used to mosaic overlapping areas.FIRST-The output cell
          value of the overlapping areas will be the value
          from the first raster dataset mosaicked into that location.LAST-The
          output cell value of the overlapping areas will be the value
          from the last raster dataset mosaicked into that location. This is the
          default.BLEND-The output cell value of the overlapping areas will be a
          horizontally weighted calculation of the values of the cells in the
          overlapping area.MEAN-The output cell value of the overlapping areas
          will be the
          average value of the overlapping cells.MINIMUM-The output cell value
          of the overlapping areas will be the
          minimum value of the overlapping cells.MAXIMUM-The output cell value
          of the overlapping areas will be the
          maximum value of the overlapping cells.SUM-The output cell value of
          the overlapping areas will be the total
          sum of the overlapping cells.For more information about each mosaic
          operator, refer to the Mosaic
          Operator help topic.
      mosaic_colormap_mode {String}:
          Applies when the input raster datasets have a colormap.Specifies the
          method that will be used to choose which color map from
          the input rasters will be applied to the mosaic output.FIRST-The color
          map from the first raster dataset in the list will be
          applied to the output raster mosaic. This is the default.LAST-The
          color map from the last raster dataset in the list will be
          applied to the output raster mosaic.MATCH-All the color maps will be
          considered when mosaicking. If all
          possible values are already used (for the bit depth), the tool will
          match the value with the closest available color.REJECT-Only the
          raster datasets that do not have a color map
          associated with them will be mosaicked.

        """