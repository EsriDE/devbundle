# Generated documentation for module arcpy.geoanalytics


class MergeLayers(object):
    """
    Combines feature layers to create a single output layer.
    """

    @property
    def description(self) -> str:
        return """

        MergeLayers_geoanalytics(input_layer, merge_layer, output_name, {merging_attributes;merging_attributes...}, {data_store})

        Combines feature layers to create a single output layer.

     INPUTS:
      input_layer (Record Set):
          The point, line, or polygon features or table to merge with the merge
          layer.
      merge_layer (Record Set):
          The point, line, or polygon features or table to merge with the input
          layer. The merge layer must contain the same feature type and time
          type as the input layer.
      output_name (String):
          The name of the output feature service.
      merging_attributes {Value Table}:
          A list of values that describe how fields from the merge layer are to
          be modified and matched with fields in the input layer. All fields
          from the input layer will be written to the output layer. If no
          merging attributes are defined, all fields from the merge layer will
          be written to the output layer. If a field exists in one layer
          but not the other, the output
          layer will still contain two fields. The output field will contain
          null values for the input features that did not have the field. For
          example, if the input layer contains a field namedbut the merge layer
          does not contain, the output will contain, but its values will be null
          for all the features copied from the merge layer. TYPETYPETYPE
          You can control how fields in the merge layer are written to
          the output layer using the following merge types:        Remove-The
          merge layer field will be removed from the output
          layer.Rename-The merge layer field will be renamed in the output. You
          cannot
          rename a field from the merge layer to a field from the input layer.
          To make field names equivalent, use the match option.
          Match-The merge layer field is renamed and matched to a
          field from the input layer. For example, the input layer has a field
          namedand the merge layer has a field named. You can matchto, and the
          output will contain thefield with values of thefield used for features
          copied from the merge layer. Type casting is supported for numeric
          values. Matching numeric fields to string fields is not supported.
          CODESTATUSSTATUSCODECODESTATUS
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