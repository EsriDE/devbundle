# Generated documentation for module arcpy.geoanalytics


class OverlayLayers(object):
    """
    Overlays the geometries from multiple layers into a single layer. Overlay can be used to combine, erase, modify, or update spatial features.
    """

    @property
    def description(self) -> str:
        return """

        OverlayLayers_geoanalytics(input_layer, overlay_layer, output_name, overlay_type, {include_overlaps}, {data_store})

        Overlays the geometries from multiple layers into a single layer.
        Overlay can be used to combine, erase, modify, or update spatial
        features.

     INPUTS:
      input_layer (Feature Set):
          The point, line, or polygon features that will be overlaid with the
          overlay layer.
      overlay_layer (Feature Set):
          The features that will be overlaid with the input layer features.
      output_name (String):
          The name of the output feature service.
      overlay_type (String):
          Specifies the type of overlay to be performed.INTERSECT-A geometric
          intersection of the input layers will be
          computed. Features or portions of features that overlap in both the
          input layer and overlay layer will be written to the output layer.
          This is the default.ERASE-Only those features or portions of features
          in the input layer
          that do not overlap the features in the overlay layer will be written
          to the output.UNION-A geometric union of the input layer and overlay
          layer will be
          computed. All features and their attributes will be written to the
          layer.IDENTITY-A geometric intersection of the input features and
          identity
          features will be computed. Features or portions of features that
          overlap in both the input layer and the overlay layer will be written
          to the output layer.SYMMETRICAL_DIFFERENCE-Features or portions of
          features in the input
          layer and overlay layer that do not overlap will be written to the
          output layer.
      include_overlaps {Boolean}:
          Specifies whether one or both of the input layers have overlapping
          features. This parameter is only supported for ArcGIS Enterprise
          10.6.1.OVERLAPPING-One or both of the layers have overlapping
          features. This
          is the default.NOT_OVERLAPPING-Neither layer has overlapping features.
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