# Generated documentation for module arcpy.un


class ExportSubnetworkControllers(object):
    """
    Exports subnetwork controllers from a utility network to a .csv file.
    """

    @property
    def description(self) -> str:
        return """

        ExportSubnetworkControllers_un(in_utility_network, out_csv_file)

        Exports subnetwork controllers from a utility network to a .csv file.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network from which subnetwork controllers will be
          exported.

     OUTPUTS:
      out_csv_file (File):
          The location and name of the .csv file to be generated.

        """