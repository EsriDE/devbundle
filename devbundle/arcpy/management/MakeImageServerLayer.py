# Generated documentation for module arcpy.management


class MakeImageServerLayer(object):
    """
    Creates a temporary raster layer from an image service. The layer that is created will not persist after the session ends unless the document is saved.
    """

    @property
    def description(self) -> str:
        return """

        MakeImageServerLayer_management(in_image_service, out_imageserver_layer, {template}, {band_index;band_index...}, {mosaic_method}, {order_field}, {order_base_value}, {lock_rasterid}, {cell_size}, {where_clause}, {processing_template})

        Creates a temporary raster layer from an image service. The layer that
        is created will not persist after the session ends unless the document
        is saved.

     INPUTS:
      in_image_service (Image Service / String):
          The name of the input image service or the SOAP URL that references
          the image service.An example of using the image service name called
          ProjectX is:
          C:\MyProject\ServerConnection.ags\ProjectX.ImageServer.An example of a
          URL is
          http://AGSServer:8399/arcgis/services/ISName/ImageServer.
      template {Extent}:
          The output extent of the image layer.MAXOF-The maximum extent of all
          inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      band_index {Value Table}:
          The bands that will be exported for the layer. If no bands are
          specified, all the bands will be used in the output.
      mosaic_method {String}:
          The mosaic method defines how the mosaic is created from different
          rasters.SEAMLINE-Smooth transitions between images using
          seamlines.NORTH_WEST-Display imagery that is closest to the northwest
          corner of
          the mosaic dataset boundary.CLOSEST_TO_CENTER-Display imagery that is
          closest to the center of the
          screen.LOCK_RASTER-Select specific raster datasets to
          display.BY_ATTRIBUTE-Display and prioritize imagery based on a field
          in the
          attribute table.CLOSEST_TO_NADIR-Display the rasters with viewing
          angles closest to
          zero.CLOSEST_TO_VIEWPOINT-Display imagery that is closest to a
          selected
          viewing angle.NONE-Order rasters based on the ObjectID in the mosaic
          dataset
          attribute table.
      order_field {String}:
          The default field to use to order the rasters when the mosaic method
          is By_Attribute. The list of fields is defined as those in the service
          table that are of type metadata and are integer (for example, the
          values can represent dates or cloud cover percentage).
      order_base_value {String}:
          The images are sorted based on the difference between this input value
          and the attribute value in the specified field.
      lock_rasterid {String}:
          The raster ID or raster name to which the service should be locked,
          such that only the specified rasters are displayed. If left blank
          (undefined), it will be similar to the system default. Multiple IDs
          can be defined as a semicolon-delimited list.
      cell_size {Double}:
          The cell size for the output image service layer.
      where_clause {SQL Expression}:
          Define a query using SQL.
      processing_template {String}:
          The raster function processing template that can be applied on the
          output image service layer.None-No processing template.

     OUTPUTS:
      out_imageserver_layer (Raster Layer):
          The name of the output image layer.

        """