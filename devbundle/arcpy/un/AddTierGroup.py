# Generated documentation for module arcpy.un


class AddTierGroup(object):
    """
    Adds a tier group to a domain network in a utility network.
    """

    @property
    def description(self) -> str:
        return """

        AddTierGroup_un(in_utility_network, domain_network, name)

        Adds a tier group to a domain network in a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the domain network where the tier
          group will be added.
      domain_network (String):
          The name of the domain network to which the tier group will be added.
          Tier groups can only be added to domain networks that have a
          hierarchical tier definition.
      name (String):
          A unique name for the new tier group. The name can be a maximum of 64
          characters in length.

        """