# Generated documentation for module arcpy.geoanalytics


class GWR(object):
    """
    Performs Geographically Weighted Regression (GWR), which is a local form of linear regression that is used to model spatially varying relationships.
    """

    @property
    def description(self) -> str:
        return """

        GWR_geoanalytics(in_features, dependent_variable, model_type, explanatory_variables;explanatory_variables..., output_features, neighborhood_type, neighborhood_selection_method, {number_of_neighbors}, {distance_band}, {local_weighting_scheme}, {data_store})

        Performs Geographically Weighted Regression (GWR), which is a local
        form of linear regression that is used to model spatially varying
        relationships.

     INPUTS:
      in_features (Feature Set):
          The point feature class containing the dependent and explanatory
          variables.
      dependent_variable (Field):
          The numeric field containing the observed values that will be modeled.
      model_type (String):
          Specifies the type of data that will be modeled.CONTINUOUS-The
          dependent_variable value is continuous. The Gaussian
          model will be used, and the tool will perform ordinary least squares
          regression.
      explanatory_variables (Field):
          A list of fields representing independent explanatory variables in the
          regression model.
      output_features (String):
          The name of the output feature service.
      neighborhood_type (String):
          Specifies whether the neighborhood used is constructed as a fixed
          distance or allowed to vary in spatial extent depending on the density
          of the features.NUMBER_OF_NEIGHBORS-The neighborhood size is a
          function of a
          specified number of neighbors included in calculations for each
          feature. Where features are dense, the spatial extent of the
          neighborhood is smaller; where features are sparse, the spatial extent
          of the neighborhood is larger.DISTANCE_BAND-The neighborhood size is a
          constant or fixed distance
          for each feature.
      neighborhood_selection_method (String):
          Specifies how the neighborhood size will be determined.USER_DEFINED-
          The neighborhood size will be determined by either the
          number_of_neighbors or distance_band parameter.
      number_of_neighbors {Long}:
          The closest number of neighbors (up to 1000) to consider for each
          feature. The number must be an integer between 2 and 1000.
      distance_band {Linear Unit}:
          The spatial extent of the neighborhood.
      local_weighting_scheme {String}:
          Specifies the kernel type that will be used to provide the spatial
          weighting in the model. The kernel defines how each feature is related
          to other features within its neighborhood.BISQUARE-A weight of 0 will
          be assigned to any feature outside the
          neighborhood specified. This is the default.GAUSSIAN-All features will
          receive weights, but weights become
          exponentially smaller the farther away they are from the target
          feature.
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