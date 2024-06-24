# Generated documentation for module arcpy.topographic


class UpdateGeoNames(object):
    """
    Updates the name field on input features based on the information from GeoNames_FeaturesP and GEONAMES_TABLE.
    """

    @property
    def description(self) -> str:
        return """

        UpdateGeoNames_topographic(in_features;in_features..., in_geonames_features, in_geonames_table, named_feature_id_field, name_id_field, name_field)

        Updates the name field on input features based on the information from
        GeoNames_FeaturesP and GEONAMES_TABLE.

     INPUTS:
      in_features (Feature Layer):
          The input features that will be updated. Each in_features value should
          have field names matching the values specified for the
          named_feature_id_field, name_id_field, and name_field parameters.
      in_geonames_features (Feature Layer):
          The input GeoNames features that identify unique named feature
          locations.
      in_geonames_table (Table View):
          A table containing name records related to the input GeoNames
          features.
      named_feature_id_field (Field):
          The field storing GeoNames named feature identifier values. These
          values should not be null or empty on the input features.
      name_id_field (Field):
          The field to store GeoNames name identifier values.
      name_field (Field):
          The field to store GeoNames name values.

        """