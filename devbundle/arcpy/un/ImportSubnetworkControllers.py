# Generated documentation for module arcpy.un


class ImportSubnetworkControllers(object):
    """
    Imports subnetwork controllers from a .csv file into a utility network.
    """

    @property
    def description(self) -> str:
        return """

        ImportSubnetworkControllers_un(in_utility_network, csv_file)

        Imports subnetwork controllers from a .csv file into a utility
        network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network to which the subnetwork controllers will be
          imported.
      csv_file (File):
          The .csv file containing the subnetwork controllers to import.

        """