# Generated documentation for module arcpy.un


class CreateUtilityNetwork(object):
    """
    Creates a utility network in an enterprise, file, or mobile geodatabase feature dataset.
    """

    @property
    def description(self) -> str:
        return """

        CreateUtilityNetwork_un(in_feature_dataset, in_utility_network_name, service_territory_feature_class)

        Creates a utility network in an enterprise, file, or mobile
        geodatabase feature dataset.

     INPUTS:
      in_feature_dataset (Feature Dataset):
          The geodatabase feature dataset in which the utility network and
          schema will be created.
      in_utility_network_name (String):
          The name of the utility network that will be created.
      service_territory_feature_class (Polygon):
          The existing polygon feature class that will be used to create the
          utility network's geographical extent. Utility network features cannot
          be created outside of this extent.The feature class must be z- and
          m-enabled.

        """