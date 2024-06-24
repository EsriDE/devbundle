# Generated documentation for module arcpy.geoanalytics


class ClipLayer(object):
    """
    Extracts input features from within specified polygons.
    """

    @property
    def description(self) -> str:
        return """

        ClipLayer_geoanalytics(input_layer, clip_layer, output_name, {data_store})

        Extracts input features from within specified polygons.

     INPUTS:
      input_layer (Feature Set):
          The dataset containing the point, line, or polygon features to be
          clipped.
      clip_layer (Feature Set):
          The dataset containing the polygon features used to clip the input
          features.
      output_name (String):
          The name of the output feature service.
      data_store {String}:
          Specifies the ArcGIS Data Store where the output will be saved. The
          default is SPATIOTEMPORAL_DATA_STORE. All results stored in a
          spatiotemporal big data store will be stored in WGS84. Results stored
          in a relational data store will maintain their coordinate
          system.SPATIOTEMPORAL_DATA_STORE-Output will be stored in a
          spatiotemporal
          big data store. This is the default.RELATIONAL_DATA_STORE-Output will
          be stored in a relational data
          store.

        """