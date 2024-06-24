# Generated documentation for module arcpy.un


class ImportTraceConfigurations(object):
    """
    Imports named trace configurations from JSON format (.json file) to a utility network.
    """

    @property
    def description(self) -> str:
        return """

        ImportTraceConfigurations_un(in_utility_network, in_json_file)

        Imports named trace configurations from JSON format (.json file) to a
        utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network to which the named trace configurations will be
          imported.
      in_json_file (File):
          The .json file containing the named trace configurations to import.

        """