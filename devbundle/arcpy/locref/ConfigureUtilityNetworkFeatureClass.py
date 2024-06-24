# Generated documentation for module arcpy.locref


class ConfigureUtilityNetworkFeatureClass(object):
    """
    Configures a Utility Network pipeline feature class for use with a linear referencing system (LRS).
    """

    @property
    def description(self) -> str:
        return """

        ConfigureUtilityNetworkFeatureClass_locref(in_feature_class, route_id_field, from_measure_field, to_measure_field)

        Configures a Utility Network pipeline feature class for use with a
        linear referencing system (LRS).

     INPUTS:
      in_feature_class (Feature Layer):
          The input Utility Network feature that is also the LRS centerline
          feature.
      route_id_field (Field):
          The field in the feature class that will be mapped as the LRS Network
          Route ID.
      from_measure_field (Field):
          The From measure field of the centerline feature class.
      to_measure_field (Field):
          The To measure field of the centerline feature class.

        """