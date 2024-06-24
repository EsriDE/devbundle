# Generated documentation for module arcpy.topographic


class GenerateProductLayout(object):
    """
    Automates the process of producing a layout or map based on a standard specification.
    """

    @property
    def description(self) -> str:
        return """

        GenerateProductLayout_topographic(geodatabase, aoi_layer, product, version, output_location, {rasters;rasters...}, {template}, {output_type}, {export_file})

        Automates the process of producing a layout or map based on a standard
        specification.

     INPUTS:
      geodatabase (Workspace):
          The input geodatabase that contains the features for the final map
          product. The schema of the workspace must match the schema of the
          product selected.
      aoi_layer (Feature Layer):
          A polygon feature layer that describes the processing extent. The
          feature layer must have only one feature selected or must be a feature
          class with only one feature.
      product (String):
          Specifies the supported map product that will be used.MTM50-An MGCP
          Topographic Map at 1:50,000 cartographic product scale
          will be used.MTM100-A MGCP Topographic Map at 1:100,000 cartographic
          product scale
          will be used.TM25-A Topographic Map at 1:25,000 cartographic product
          scale will be
          used.TM50-A Topographic Map at 1:50,000 cartographic product scale
          will be
          used.TM100-A Topographic Map at 1:100,000 cartographic product scale
          will
          be used.JOGA-A Joint Operations Graphic at 1:250,000 cartographic
          product
          scale will be used.CTM50-A Civilian Topographic map at 1:50,000
          cartographic product
          scale will be used.
      version (String):
          The supported versions of the selected product.
      output_location (Folder):
          The folder path to which the output file will be written.
      rasters {Raster Layer / Mosaic Layer}:
          The input rasters used if the product requires an elevation guide
          surround element to calculate the elevation bands and spot height
          features. If you specify more than one raster, the rasters must have
          the same cell size, band number, and pixel type. If no raster is
          specified, the elevation guide data frame will not be processed and a
          warning will appear.
      template {Layout}:
          The layout template to be used. If no layout template is specified,
          the default layout template for the product will be used.
      output_type {String}:
          Specifies the type of output.PAGX-A layout file will be created. This
          is the default.APRX-An ArcGIS
          Pro project file will be created.PDF-A .pdf file will be
          created.TIFF-A .tiff file will be created.PPKX-An ArcGIS Pro packaged
          project file will be created.
      export_file {File}:
          A file that defines a set of parameter values for the specified
          output_type parameter value.

        """