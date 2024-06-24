# Generated documentation for module arcpy.geoanalytics


class FindSimilarLocations(object):
    """
    Identifies the candidate features that are most similar or dissimilar to one or more input features based on feature attributes.
    """

    @property
    def description(self) -> str:
        return """

        FindSimilarLocations_geoanalytics(input_layer, search_layer, output_name, analysis_fields;analysis_fields..., {most_or_least_similar}, {match_method}, {number_of_results}, {append_fields;append_fields...}, {data_store})

        Identifies the candidate features that are most similar or dissimilar
        to one or more input features based on feature attributes.

     INPUTS:
      input_layer (Record Set):
          The reference layer (or a selection on a layer) containing the
          features to be matched. The tool searches for other features similar
          to these features. When more than one feature is provided, matching is
          based on attribute averages.
      search_layer (Record Set):
          The candidate layer (or a selection on a layer) containing candidate-
          matching features. The tool searches for features most similar (or
          dissimilar) to the input_layer parameter among these candidates.
      output_name (String):
          The name of the output feature service. The output feature service
          contains a record for each of the input_layer parameters and for all
          the solution-matching features found.
      analysis_fields (String):
          A list of numeric attributes representing the matching criteria.
      most_or_least_similar {String}:
          Specifies whether the features to be found are most similar or least
          similar to the input_layer parameter.MOST_SIMILAR-Finds the features
          that are most
          similar.LEAST_SIMILAR-Finds the features that are least
          similar.BOTH-Finds the features that are most similar and the features
          that
          are least similar.
      match_method {String}:
          Specifies whether matches will be based on values or cosine
          relationships.ATTRIBUTE_VALUES-Similarity or dissimilarity will be
          based on the sum
          of squared standardized attribute value differences for all the
          analysis_fields attributes.ATTRIBUTE_PROFILES-Similarity or
          dissimilarity will be computed as a
          function of cosine similarity for all the analysis_fields attributes.
      number_of_results {Long}:
          The number of solution matches to be found. Entering zero or a number
          larger than the total number of search_layer features will return
          rankings for all the candidate features, with a maximum of 10,000.
      append_fields {Field}:
          An optional list of attributes to include with the output. You can
          include a name identifier, categorical field, or date field for
          example. These fields are not used to determine similarity; they are
          only included in the output parameter attributes for your reference.
          By default, all fields are added.
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