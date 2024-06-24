# Generated documentation for module arcpy.ba


class GeneratePointsFromBusinessListings(object):
    """
    Generates a point feature layer from a business point location search.
    """

    @property
    def description(self) -> str:
        return """

        GeneratePointsFromBusinessListings_ba(out_feature_class, {in_search_features}, {search_terms}, {exact_match}, {match_name_only}, {filters;filters...}, {max_count}, {business_dataset}, {find_related_poi})

        Generates a point feature layer from a business point location search.

     INPUTS:
      in_search_features {Feature Layer}:
          The area that will be used to search for businesses. Selected features
          supersede the feature class and will be used as the search area.
      search_terms {String}:
          The terms that will be used to search for businesses. You can use
          terms such as business name or business type keywords. If this
          parameter is not set, all businesses from the in_search_features
          parameter value will be returned.
      exact_match {Boolean}:
          Specifies whether only the text provided for the search_terms
          parameter will be returned from the search.EXACT_MATCH-Only exact
          matches to the text provided for the
          search_terms parameter will be returned.PARTIAL_MATCH-Partial matches
          to the text provided for the
          search_terms parameter as well as exact matches will be returned. This
          is the default.
      match_name_only {Boolean}:
          Specifies whether the search will be limited to the business name
          only.MATCH_NAME_ONLY-Only exact matches to the business name provided
          for
          the search_terms parameter will be returned.MATCH_ALL_FIELDS-Partial
          matches to the business name provided for the
          search_terms parameter as well as exact matches will be returned. This
          is the default.
      filters {Value Table}:
          The filters that will be applied to the search_terms
          parameter.filter_name-Set the filter by the dataset
          field.filter_value-Set the
          filter by applying a value to the selected field.include-Set the
          filter by including or excluding field values.
      max_count {Long}:
          The limit for the number of returned features. The default value is
          1,000,000 for local data and 5,000 for online data hosted by ArcGIS
          Online.The record limit when using on-premises hosted data is set by
          your
          administrator.
      business_dataset {String}:
          The dataset that will be used in the business search.
      find_related_poi {Boolean}:
          Specifies whether semantic search will be used to find related items
          to the search terms.FIND_RELATED_POI-Semantic search will be
          used.IGNORE_RELATED_POI-Semantic search will not be used. This is the
          default.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class that will contain the returned businesses.

        """