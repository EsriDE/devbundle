# Generated documentation for module arcpy.conversion


class MapToKML(object):
    """
    Converts a map containing feature or raster layers to KML format (.kmz file). The output KML will contain a translation of Esri feature geometries, raster cells, layer symbology, and other properties.
    """

    @property
    def description(self) -> str:
        return """

        MapToKML_conversion(in_map, out_kmz_file, {map_output_scale}, {is_composite}, {is_vector_to_raster}, {extent_to_export}, {image_size}, {dpi_of_client}, {ignore_zvalue}, {layout})

        Converts a map containing feature or raster layers to KML format (.kmz
        file). The output KML will contain a translation of Esri feature
        geometries, raster cells, layer symbology, and other properties.

     INPUTS:
      in_map (Map):
          The map, scene, or basemap that will be converted to KML.
      map_output_scale {Double}:
          The scale at which each layer in the map will be exported.This
          parameter is important with any scale dependency, such as layer
          visibility or scale-dependent rendering. If the layer is not visible
          at the output scale, it is not included in the output KML. Any value,
          such as 1, can be used if there are no scale dependencies.For raster
          layers, a value of 0 can be used to create one untiled
          output image. If a value greater than or equal to 1 is used, it
          determines the output resolution of the raster. This parameter has no
          effect on layers that are not raster layers.Only numeric characters
          are accepted; for example, enter 20000 as the
          scale, not 1:20000. In languages that use commas as the decimal point,
          20,000 is also acceptable.If you're exporting a layer that is to be
          displayed as 3D vectors and
          the is_composite parameter is set to NO_COMPOSITE, you can set this
          parameter to any value as long as the features do not have any scale-
          dependent rendering.
      is_composite {Boolean}:
          Specifies whether the output KML will contain a single composite image
          or separate layers.COMPOSITE-The output KML will contain a single
          image that composites
          all the features in the map into a single raster image. The raster is
          draped over the terrain as a KML GroundOverlay. This option reduces
          the size of the output KML. Individual features and layers in the KML
          are not selectable.NO_COMPOSITE-The output KML will contain separate,
          individual layers.
          This is the default. Whether the layers are returned as rasters or as
          a combination of vectors and rasters is determined by the
          is_vector_to_raster parameter value.
      is_vector_to_raster {Boolean}:
          Specifies whether each feature layer in the map will be converted to a
          separate raster image or preserved as features. This parameter is not
          used if the is_composite parameter is set to
          COMPOSITE.VECTOR_TO_IMAGE-Feature layers will be converted to a
          separate raster
          image in the KML output. Normal raster layers are also added to the
          KML output. Each output KML raster layer is selectable, and its
          transparency can be adjusted in certain KML viewer
          applications.VECTOR_TO_VECTOR-Features will be preserved in the output
          KML as
          feature geometries. This is the default.
      extent_to_export {Extent}:
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
          The size of the tiles for raster layers if the map_output_scale
          parameter value is greater than or equal to 1. This parameter has no
          effect on layers that are not raster layers.
      dpi_of_client {Long}:
          The device resolution for any rasters in the output KML document.
          Typical screen resolution is 96 dpi. If the data in the map supports a
          high resolution and the KML requires it, consider increasing the
          value. Use this parameter with the image_size parameter to control
          output image resolution. The default value is 96.
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
      layout {String}:
          The name of the layout that contains legend elements that will be
          included in the KML output as screen overlays.

     OUTPUTS:
      out_kmz_file (File):
          The output KML file, which is compressed and has a .kmz extension.

        """