# Generated documentation for module arcpy.geoanalytics


class DescribeDataset(object):
    """
    Summarizes features into calculated field statistics, sample features, and extent boundaries.
    """

    @property
    def description(self) -> str:
        return """

        DescribeDataset_geoanalytics(input_layer, output_name, {sample_features}, {create_extent_layer}, {data_store})

        Summarizes features into calculated field statistics, sample features,
        and extent boundaries.

     INPUTS:
      input_layer (Record Set):
          The point, line, polygon, or tabular features to be described.
      output_name (String):
          The name of the output feature service.
      sample_features {Long}:
          The number of features that will be included in the output sample
          layer. No sample is returned if you select 0 features or don't provide
          a number. By default, no sample layer is returned.
      create_extent_layer {Boolean}:
          Specifies whether an output extent layer will be created. The extent
          is a polygon that represents the spatial and temporal extent of the
          input features.CREATE_EXTENT-An extent layer will be
          created.NO_EXTENT-An extent
          layer will not be created.
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