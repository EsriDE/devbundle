# Generated documentation for module arcpy.management


class MosaicDatasetToMobileMosaicDataset(object):
    """
    Converts a mosaic dataset into a mobile mosaic dataset compatible with ArcGIS Runtime SDK. A mobile mosaic dataset resides in a mobile geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        MosaicDatasetToMobileMosaicDataset_management(in_mosaic_dataset, out_mobile_gdb, mosaic_dataset_name, {where_clause}, {selection_feature}, {out_data_folder}, {convert_rasters}, {out_name_prefix}, {format}, {compression_method}, {compression_quality})

        Converts a mosaic dataset into a mobile mosaic dataset compatible with
        ArcGIS Runtime SDK. A mobile mosaic dataset resides in a mobile
        geodatabase.

     INPUTS:
      in_mosaic_dataset (Mosaic Dataset / Mosaic Layer):
          The mosaic dataset to be converted to a mobile mosaic dataset.
      mosaic_dataset_name (String):
          The name of the mobile mosaic dataset to be created.
      where_clause {SQL Expression}:
          An SQL expression to select specific items to add to the mobile mosaic
          dataset.
      selection_feature {Extent}:
          The mosaic dataset items to be included in the output based on the
          extent of another image or feature class. Items that lay along the
          defined extent will be included in the mosaic dataset. They will not
          be clipped.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      out_data_folder {Folder}:
          If specified, the tool will create a copy of the source data in this
          folder. If convert_rasters='ALWAYS', any raster functions associated
          with the mosaic dataset are processed before creating the copy.
      convert_rasters {Boolean}:
          Applies the raster functions associated with the input mosaic dataset
          before creating the mobile mosaic dataset. If you have raster
          functions that are not supported by ArcGIS Runtime SDK, the tool will
          return the appropriate error message.AS_REQUIRED-Do not convert raster
          items with functions that are not
          supported by ArcGIS Runtime SDK. This is the default.ALWAYS-Apply the
          raster function chain and save the output as
          converted raster items.
      out_name_prefix {String}:
          Appends a prefix to each item, which is copied or converted into the
          output data folder.
      format {String}:
          The format for the rasters written to the output data folder.TIFF-TIFF
          formatPNG-PNG formatJPEG-JPEG formatJP2-JPEG2000 format
      compression_method {String}:
          The method of compression for transmitting the mosaicked image from
          the computer to the display (or from the server to the client).NONE-No
          compression will be used.JPEG-Compresses up to 8:1 and is
          suitable for backdrops.LZW-Compresses approximately 2:1. Suitable for
          analysis.RLE-Lossless compression. Suitable for categorical datasets.
      compression_quality {Long}:
          A value from 0 to 100. A higher number means better image quality but
          less compression. This value only applies when JPEG or JP2 is
          specified as the compression method.

     OUTPUTS:
      out_mobile_gdb (File):
          The geodatabase where the converted mosaic dataset will be created.

        """