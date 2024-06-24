# Generated documentation for module arcpy.management


class CreatePansharpenedRasterDataset(object):
    """
    Combines a high-resolution panchromatic raster dataset with a lower- resolution multiband raster dataset to create a high-resolution multiband raster dataset for visual analysis.
    """

    @property
    def description(self) -> str:
        return """

        CreatePansharpenedRasterDataset_management(in_raster, red_channel, green_channel, blue_channel, {infrared_channel}, out_raster_dataset, in_panchromatic_image, pansharpening_type, {red_weight}, {green_weight}, {blue_weight}, {infrared_weight}, {sensor})

        Combines a high-resolution panchromatic raster dataset with a lower-
        resolution multiband raster dataset to create a high-resolution
        multiband raster dataset for visual analysis.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster dataset that will be pan sharpened.
      red_channel (Long):
          The input raster band that will display with the red color channel.
      green_channel (Long):
          The input raster band that will display with the green color channel.
      blue_channel (Long):
          The input raster band that will display with the blue color channel.
      infrared_channel {Long}:
          The input raster band that will display with the infrared color
          channel.
      in_panchromatic_image (Raster Layer):
          The higher-resolution panchromatic image.
      pansharpening_type (String):
          Specifies the algorithm that will be used to combine the panchromatic
          and multispectral bands.IHS-Intensity, Hue, and Saturation color space
          will be used.BROVEY-The
          Brovey algorithm based on spectral modeling will be used.Esri-The Esri
          algorithm based on spectral modeling will be used.SIMPLE_MEAN-The
          averaged value between the red, green, and blue values
          and the panchromatic pixel value will be used.Gram-Schmidt-The Gram-
          Schmidt spectral-sharpening algorithm to sharpen
          multispectral data will be used.
      red_weight {Double}:
          A value from 0 to 1 that will be used to weight the red band.
      green_weight {Double}:
          A value from 0 to 1 that will be used to weight the green band.
      blue_weight {Double}:
          A value from 0 to 1 that will be used to weight the blue band.
      infrared_weight {Double}:
          A value from 0 to 1 that will be used to weight the infrared band.
      sensor {String}:
          Specifies the sensor of the multiband raster input.You can specify the
          sensor when the pansharpening_type parameter is
          set to Gram-Schmidt. Specifying the sensor will set appropriate band
          weights.UNKNOWN-The sensor is unknown or unlisted.BlackSky-The sensor
          is a
          BlackSky satellite sensor.DubaiSat-2-The sensor is a DubaiSat-2
          satellite sensor.GeoEye-1-The sensor is a GeoEye-1 and OrbView-3
          satellite sensor.GF-1 PMS-The sensor is a Gao Fen satellite 1,
          Panchromatic and
          Multispectral CCD Camera sensor.GF-2 PMS-The sensor is a Gao Fen 2
          satellite, Panchromatic and
          Multispectral CCD Camera sensor.IKONOS-The sensor is an IKONOS
          satellite sensor.Jilin-1-The sensor is a Jilin-1 satellite
          sensor.KOMPSAT-2-The sensor is a KOMPSAT-2 satellite
          sensor.KOMPSAT-3-The sensor is a KOMPSAT-3 satellite sensor.Landsat
          1-5 MSS-The sensor is a Landsat MSS satellite sensor.Landsat 7
          ETM+-The sensor is a Landsat 7 satellite sensor.Landsat 8-The sensor
          is a Landsat 8 satellite sensor.Landsat 9-The sensor is a Landsat 9
          satellite sensor.Pleiades-1-The sensor is a Pléiades satellite
          sensor.Pleiades Neo-The sensor is a Pléiades Neo satellite
          sensor.QuickBird-The sensor is a QuickBird satellite sensor.SkySat-The
          sensor is a SkySat-C satellite sensor.SPOT 5-The sensor is a SPOT 5
          satellite sensor.SPOT 6-The sensor is a SPOT 6 satellite sensor.SPOT
          7-The sensor is a SPOT 7 satellite sensor.SuperView-1-The sensor is a
          SuperView-1 satellite sensor.TH-01-The sensor is a Tian Hui 1
          satellite sensor.UltraCam-The sensor is an UltraCam aerial
          sensor.Vision-1-The sensor is a Vision-1 satellite
          sensor.WorldView-2-The sensor is a WorldView-2 satellite
          sensor.WorldView-3-The sensor is a WorldView-3 satellite
          sensor.WorldView-4-The sensor is a WorldView-4 satellite
          sensor.ZY1-02C PMS-The sensor is a Ziyuan High Panchromatic
          Multispectral
          Sensor.ZY3-CRESDA-The sensor is a Ziyuan CRESDA satellite
          sensor.ZY3-SASMAC-The sensor is a Ziyuan SASMAC satellite sensor.

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          The name, location, and format of the raster dataset that will be
          created.When storing the raster dataset in a file format, specify the
          file
          extension as follows:        When storing a raster dataset in a
          geodatabase, do not add a
          file extension to the name of the raster dataset. When storing the
          raster dataset in a file format, you must specify the file extension:
          .bil for Esri BIL.bip for Esri BIP.bmp for BMP.bsq for Esri BSQ.dat
          for ENVI DAT.gif for GIF.img for ERDAS IMAGINE.jpg for JPEG.jp2 for
          JPEG 2000.png for PNG.tif for TIFF.mrf for MRF.crf for CRFNo extension
          for Esri GridWhen storing a raster dataset in a geodatabase, do not
          add a file
          extension to the name of the raster dataset. When storing a
          raster dataset to a JPEG format file, a JPEG
          2000 format file, a TIFF format file, or a geodatabase, you can
          specifyandvalues in the geoprocessing environments. Compression
          TypeCompression Quality

        """