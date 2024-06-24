# Generated documentation for module arcpy.management


class ExportMosaicDatasetItems(object):
    """
    Saves a copy of processed images in a mosaic dataset to a specified folder and raster file format.
    """

    @property
    def description(self) -> str:
        return """

        ExportMosaicDatasetItems_management(in_mosaic_dataset, out_folder, {out_base_name}, {where_clause}, {format}, {nodata_value}, {clip_type}, {template_dataset}, {cell_size}, {image_space}, {remove_distortion})

        Saves a copy of processed images in a mosaic dataset to a specified
        folder and raster file format.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that contains the images to be exported.
      out_folder (Folder):
          The folder where the images will be saved.
      out_base_name {String}:
          A prefix to add to the name of each item after it is copied. The
          prefix will be followed by the Object ID value from the mosaic dataset
          footprints table. If no base name is set, the text in thefield
          of the mosaic
          dataset item will be used. Name
      where_clause {SQL Expression}:
          An SQL expression that will be used to save selected images in the
          mosaic dataset. For more information about SQL syntax, see SQL
          reference for query expressions used in ArcGIS.
      format {String}:
          Specifies the format that will be used for the output raster
          datasets.TIFF-TIFF format will be used. This is the default.Cloud
          Optimized
          GeoTIFF-Cloud Optimized GeoTIFF format will be used.BMP-BMP format
          will be used.ENVI-ENVI DAT format will be used.Esri BIL-Esri BIL
          format will be used.Esri BIP-Esri BIP format will be used.Esri
          BSQ-Esri BSQ format will be used.GIF-GIF format will be used.GRID-Esri
          Grid format will be used.IMAGINE IMAGE-ERDAS IMAGINE format will be
          used.JP2-JPEG 2000 format will be used.JPEG-JPEG format will be
          used.PNG-PNG format will be used.CRF-Cloud raster format will be
          used.MRF-Meta raster format will be used.
      nodata_value {String}:
          All the pixels with the specified value will be set to NoData in the
          output raster dataset.It is recommended that you specify a NoData
          value if the output images
          will be clipped.
      clip_type {String}:
          Specifies the output extent of the raster datasets. If you choose an
          extent or feature class that covers an area larger than the raster
          data, the output will have the larger extent.NONE-The output will not
          be clipped. This is the default.EXTENT-An
          extent will be used to clip the output.FEATURE_CLASS-A feature class
          extent will be used to clip the output.
      template_dataset {Extent}:
          The feature class or bounding box that will be used to limit the
          extent.MAXOF-The maximum extent of all inputs will be used.MINOF-The
          minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      cell_size {Point}:
          The horizontal (x) and vertical (y) dimensions of the output cells.If
          the cell size is not specified, the spatial resolution of the input
          will be used.
      image_space {Boolean}:
          Specifies whether raster items will be exported in map space or image
          space.MAPSPACE-Raster items will be exported in map space. This is the
          default.IMAGESPACE-Raster items will be exported in image space.
      remove_distortion {Boolean}:
          Specifies whether lens distortion will be removed from the exported
          raster in image space.REMOVED-Lens distortion will be removed from the
          exported raster in
          image space.NOTREMOVE-Lens distortion will not be removed from the
          exported raster
          in image space. This is the default.

        """