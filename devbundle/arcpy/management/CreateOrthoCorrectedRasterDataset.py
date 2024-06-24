# Generated documentation for module arcpy.management


class CreateOrthoCorrectedRasterDataset(object):
    """
    Creates an orthocorrected raster dataset using a digital elevation model (DEM) and control data to accurately align imagery.
    """

    @property
    def description(self) -> str:
        return """

        CreateOrthoCorrectedRasterDataset_management(in_raster, out_raster_dataset, Ortho_type, constant_elevation, {in_DEM_raster}, {ZFactor}, {ZOffset}, {Geoid})

        Creates an orthocorrected raster dataset using a digital elevation
        model (DEM) and control data to accurately align imagery.

     INPUTS:
      in_raster (Raster Dataset / Mosaic Dataset / Mosaic Layer / Raster Layer):
          The raster dataset or mosaic dataset that will be orthorectified.
      Ortho_type (String):
          Specifies whether the orthorectification type will be a DEM or a
          specified value that represents the average elevation across the
          image.CONSTANT_ELEVATION-A specified elevation value will be
          used.DEM-A
          specified digital elevation model raster will be used.
      constant_elevation (Double):
          The constant elevation value that will be used when the Ortho_type
          parameter is CONSTANT_ELEVATION.If a DEM is used in the
          orthocorrection process, this parameter value
          is not used.
      in_DEM_raster {Raster Dataset / Mosaic Dataset / Mosaic Layer / Raster Layer / Image Service}:
          The DEM raster that will be used for orthorectification when the
          Ortho_type parameter is DEM.
      ZFactor {Double}:
          The scaling factor that will be used to convert the elevation values
          in the DEM.If the vertical units are meters, set the parameter to 1.
          If the
          vertical units are feet, set the parameter to 0.3048. If any other
          vertical units are used, use this parameter to scale the units to
          meters.
      ZOffset {Double}:
          The base value that will be added to the elevation value in the DEM.
          This can be used to offset elevation values that do not start at sea
          level.
      Geoid {Boolean}:
          Specifies whether the geoid correction required by RPCs that reference
          ellipsoidal heights will be made. Most elevation datasets are
          referenced to sea level orthometric heights, so this correction is
          required in these cases to convert to ellipsoidal heights.NONE-No
          geoid correction will be made. Use NONE only if the DEM is
          already expressed in ellipsoidal heights.GEOID-A geoid correction will
          be made to convert orthometric heights
          to ellipsoidal heights (based on EGM96 geoid).

     OUTPUTS:
      out_raster_dataset (Raster Dataset):
          The name, location, and format of the dataset that will be
          created.When storing the raster dataset in a file format, specify the
          file
          extension as follows:.bil-Esri BIL.bip-Esri BIP.bmp-BMP.bsq-Esri
          BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFF.mrf-MRF.crf-CRFNo extension for Esri GridWhen
          storing a raster dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset. When storing a
          raster dataset to a JPEG format file, a JPEG
          2000 format file, or a geodatabase, you can specify avalue and avalue
          in the geoprocessing environments. Compression TypeCompression
          Quality

        """