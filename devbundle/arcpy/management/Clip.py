# Generated documentation for module arcpy.management


class Clip(object):
    """
    Cuts out a portion of a raster dataset, mosaic dataset, or image service layer.
    """

    @property
    def description(self) -> str:
        return """

        Clip_management(in_raster, rectangle, out_raster, {in_template_dataset}, {nodata_value}, {clipping_geometry}, {maintain_clipping_extent})

        Cuts out a portion of a raster dataset, mosaic dataset, or image
        service layer.

     INPUTS:
      in_raster (Mosaic Dataset / Mosaic Layer / Raster Dataset / Raster Layer):
          The raster dataset, mosaic dataset, or image service to be clipped.
      rectangle (Envelope / Feature Class / Feature Layer):
          The four coordinates that define the extent of the bounding box that
          will be used to clip the raster. Coordinates are expressed in the
          order of x-min, y-min, x-max, y-max.If the in_template_dataset
          parameter is set, it will automatically set
          this parameter. If the in_template_dataset parameter is a feature
          layer, the clipping extent is extracted from the bounding box. In this
          case, the rectangle parameter can be left empty as long as the
          in_template_dataset parameter value is specified.If both the rectangle
          and in_template_dataset parameters are set, the
          rectangle parameter value will be used.If the value specified is not
          aligned with the input raster dataset,
          the tool verifies that the proper alignment is used. This may cause
          the output to have a slightly different extent than specified.
      in_template_dataset {Feature Layer / Raster Layer}:
          A raster dataset or feature class that will be used as the extent. The
          clip output includes pixels that intersect the minimum bounding
          rectangle.If a feature class is used as the output extent and you want
          to clip
          the raster based on the polygon features, set the clipping_geometry
          parameter to ClippingGeometry. This option may promote the pixel depth
          of the output. Ensure that the output format can support the proper
          pixel depth.
      nodata_value {String}:
          The value for pixels to be considered as NoData.
      clipping_geometry {Boolean}:
          Specifies whether the minimum bounding rectangle or the geometry of
          the specified feature class will be used to clip the data.NONE-The
          minimum bounding rectangle will be used to clip the data.
          This is the default.ClippingGeometry-The geometry of the specified
          feature class will be
          used to clip the data. The pixel depth of the output may be increased;
          ensure that the output format can support the proper pixel depth.
      maintain_clipping_extent {Boolean}:
          Specifies the extent that will be used in the clipping
          output.MAINTAIN_EXTENT-The number of columns and rows will be adjusted
          and
          the pixels will be resampled to exactly match the clipping extent
          specified.NO_MAINTAIN_EXTENT-The cell alignment of the input raster
          will be
          maintained and the output extent will be adjusted accordingly. This is
          the default.

     OUTPUTS:
      out_raster (Raster Dataset):
          The name, location, and format of the dataset being created. Ensure
          that it can support the necessary bit depth.When storing the raster
          dataset in a file format, specify the file
          extension as follows:.bil-Esri BIL.bip-Esri BIP.bmp-BMP.bsq-Esri
          BSQ.dat-ENVI
          DAT.gif-GIF.img-ERDAS IMAGINE.jpg-JPEG.jp2-JPEG
          2000.png-PNG.tif-TIFF.mrf-MRF.crf-CRFNo extension for Esri GridWhen
          storing a raster dataset in a geodatabase, do not add a file
          extension to the name of the raster dataset. When storing a
          raster dataset to a JPEG format file, a JPEG
          2000 format file, a TIFF format file, or a geodatabase, you can
          specifyandvalues in the geoprocessing environments. Compression
          TypeCompression Quality

        """