# Generated documentation for module arcpy.geoanalytics


class SummarizeCenterAndDispersion(object):
    """
    Finds central features and directional distributions and calculates mean and median locations from the input.
    """

    @property
    def description(self) -> str:
        return """

        SummarizeCenterAndDispersion_geoanalytics(input_layer, output_name, generate_types;generate_types..., {ellipse_size}, {weight_field}, {group_by_field}, {data_store})

        Finds central features and directional distributions and calculates
        mean and median locations from the input.

     INPUTS:
      input_layer (Feature Set):
          The point, line, or polygon layer to be summarized.
      output_name (String):
          The name of the output feature service.
      generate_types (String):
          Specifies the summary types to be generated. You can use one or more
          summary types. A unique layer will be created for each summary type
          selected.CENTRAL_FEATURE-A layer will be created that contains a copy
          of the
          most central feature from the input layer.MEAN_CENTER-A point layer
          will be created that represents the mean
          center of the input layer.MEDIAN_CENTER-A point layer will be created
          that represents the median
          center of the input layer.ELLIPSE-A polygon layer will be created that
          represents the
          directional ellipse of the input layer.
      ellipse_size {String}:
          Specifies the size of output ellipses in standard
          deviations.1_STANDARD_DEVIATION-Output ellipses will cover one
          standard deviation
          of the input features. This is the
          default.2_STANDARD_DEVIATIONS-Output ellipses will cover two standard
          deviations of the input features.3_STANDARD_DEVIATIONS-Output ellipses
          will cover three standard
          deviations of the input features.
      weight_field {Field}:
          A numeric field used to weight locations according to their relative
          importance. This applies to all summary types.
      group_by_field {Field}:
          The field used to group similar features. This applies to all
          summary types. For example, if you choose a field namedthat contains
          values of tree, bush, and grass, all of the features with the value
          tree will be analyzed for their own center or dispersion. This example
          will result in three features, one for each group of tree, bush, and
          grass. PlantType
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