# Generated documentation for module arcpy.un


class DeleteNetworkCategory(object):
    """
    Deletes a network category in a utility network.
    """

    @property
    def description(self) -> str:
        return """

        DeleteNetworkCategory_un(in_utility_network, category_name)

        Deletes a network category in a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the network category to be deleted.
      category_name (String):
          The name of the network category to delete.

        """