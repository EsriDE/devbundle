# Generated documentation for module arcpy.conversion


class LayerToKML(object):
    """
    Converts a feature or raster layer to KML format (.kmz or .kml file). The output KML will contain a translation of Esri feature geometries, raster cells, layer symbology, and other properties.
    """

    @property
    def description(self) -> str:
        return """

        LayerToKML_conversion(layer, out_kmz_file, {layer_output_scale}, {is_composite}, {boundary_box_extent}, {image_size}, {dpi_of_client}, {ignore_zvalue})

        Converts a feature or raster layer to KML format (.kmz or .kml file).
        The output KML will contain a translation of Esri feature geometries,
        raster cells, layer symbology, and other properties.

     INPUTS:
      layer (Feature Layer / Raster Layer / Mosaic Layer / Group Layer / Layer File):
          The feature or raster layer or group layer that will be converted to
          KML format.
      layer_output_scale {Double}:
          The scale of the output file. For raster layers, a value of 0 can be
          used to create one untiled output image. If a value greater than or
          equal to 1 is used, it will determine the output resolution of the
          raster. This parameter has no effect on layers that are not raster
          layers.
      is_composite {Boolean}:
          Specifies whether the output will be a single composite image. This
          parameter only applies if you specify the output KML as a .kmz file,
          as output .kml files do not support ground overlay images or
          rasters.COMPOSITE-The output will be a single composite image
          representing the
          raster or vector features in the source layer. The raster is draped
          over the terrain as a GroundOverlay. Use this option to reduce the
          size of the output file. When this option is used, individual features
          and layers in the .kml file cannot be selected. Only output .kmz files
          support images.NO_COMPOSITE-If the input has vector features, they
          will be preserved
          as KML vectors.
      boundary_box_extent {Extent}:
          The geographic extent of the layer to be converted. Only features or
          raster cells in this extent will be included in the output KML. The
          extent can be specified using the following options:MAXOF-The maximum
          extent of all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      image_size {Long}:
          The size of the tiles for raster layers if the layer_output_scale
          parameter value is greater than or equal to 1. This parameter has no
          effect on layers that are not raster layers.
      dpi_of_client {Long}:
          The device resolution for KML output when the is_composite parameter
          is set to COMPOSITE. Use this parameter with the image_size parameter
          to control output image resolution.This parameter does not resample
          source rasters. Input rasters will
          have a snapshot taken and included in the KML output as a simple .png
          image.
      ignore_zvalue {Boolean}:
          Specifies whether the z-values of the input features will be ignored
          and all features will be located, or clamped, at the ground
          elevation.ABSOLUTE-The z-values of the features will be maintained in
          the output
          KML. The features will be drawn in KML clients relative to sea
          level.CLAMPED_TO_GROUND-The z-values of the input features will be
          ignored
          and all features will be located, or clamped, at the ground elevation.
          If the input features do not have z-values, they will always be
          clamped to the ground. This is the default.

     OUTPUTS:
      out_kmz_file (File / Workspace / KML Layer):
          The output .kml or .kmz file. The output file can use the .kmz
          extension to produce an archive or zipped file, or the .kml extension
          to produce a basic KML format file. An output .kmz file is the
          default.Output .kmz files support raster layers, symbology and other
          layer
          properties, attachments, and other advanced features. Output .kml
          files will use basic KML symbols and properties.

        """