# Generated documentation for module arcpy.geoanalytics


class CopyToDataStore(object):
    """
    Copies features from the input to a new feature service in your portal.
    """

    @property
    def description(self) -> str:
        return """

        CopyToDataStore_geoanalytics(input_layer, output_name, {data_store})

        Copies features from the input to a new feature service in your
        portal.

     INPUTS:
      input_layer (Record Set):
          The features to be copied.
      output_name (String):
          Name of output feature service.
      data_store {String}:
          The ArcGIS Data Store to which the output will be saved. The default
          is SPATIOTEMPORAL_DATA_STORE. All results stored to the
          SPATIOTEMPORAL_DATA_STORE will be stored in WGS84. Results stored in a
          RELATIONAL_DATA_STORE will maintain their coordinate
          system.SPATIOTEMPORAL_DATA_STORE-Output will be stored in your
          spatiotemporal
          big data store. This is the default.RELATIONAL_DATA_STORE-Output will
          be stored in your relational data
          store.

        """