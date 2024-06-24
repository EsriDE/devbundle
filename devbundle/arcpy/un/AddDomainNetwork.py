# Generated documentation for module arcpy.un


class AddDomainNetwork(object):
    """
    Adds a domain network to a utility network.
    """

    @property
    def description(self) -> str:
        return """

        AddDomainNetwork_un(in_utility_network, domain_network_name, tier_definition, subnetwork_controller_type, {domain_network_alias_name})

        Adds a domain network to a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network to which the domain network will be added.
      domain_network_name (String):
          The name of the new domain network. The domain network name will
          prefix the feature class names that are created. For example, a domain
          named ElectricDistribution would include a feature class named
          ElectricDistributionJunction.
      tier_definition (String):
          Specifies the tier definition for the new domain
          network.HIERARCHICAL-The tier will be defined as hierarchical. In
          hierarchical
          domain networks, tiers are nested within one another, so features
          existing in subnetworks for a lower tier naturally participate in all
          higher tiers. For example, in a gas network, a valve isolation zone
          exists in a pressure zone, which in turn exists in a system zone. A
          feature in the isolation zone also exists in the pressure zone and in
          the system zone.PARTITIONED-The tier will be defined as partitioned.
          Features in
          partitioned domain networks only exist in one tier. The relationship
          between tiers is ordered and linear. Features can exist in one or
          multiple subnetworks in one tier.
      subnetwork_controller_type (String):
          Specifies the subnetwork controller type for the new domain
          network.SOURCE-The subnetwork controller type is a set of sources. A
          source is
          an origin of the delivered resource. For example, in an electric
          system, sources of electricity are power generating stations and
          substations.SINK-The subnetwork controller type is a set of sinks. A
          sink is the
          destination of the gathered resource.
      domain_network_alias_name {String}:
          The alias name of the domain network. This optional parameter is used
          to give a more descriptive name to the domain network.

        """