# Generated documentation for module arcpy.un


class AddTier(object):
    """
    Creates a new tier for a domain network in a utility network.
    """

    @property
    def description(self) -> str:
        return """

        AddTier_un(in_utility_network, domain_network, name, rank, {topology_type}, {tier_group_name}, {subnetwork_field_name})

        Creates a new tier for a domain network in a utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The utility network that contains the domain network where the tier
          will be added.
      domain_network (String):
          The domain network where the tier will be created.
      name (String):
          The name of the new tier. The name must be unique in the entire
          utility network.
      rank (Long):
          The rank of the tier being added. The highest rank is the number 1.
      topology_type {String}:
          Specifies the topology type for the new tier. Subnetworks with radial
          and mesh topology types both support one or more subnetwork
          controllers. This parameter is disabled on the tool dialog box if the
          input domain network was created with a hierarchical tier definition
          and the topology type defaults to mesh. If the input domain network
          was created with a hierarchical tier definition, the default topology
          type is MESH. If the input domain network was created with a
          partitioned tier definition, the topology type parameter is
          required.RADIAL-The subnetworks will have a radial topology
          type.MESH-The
          subnetworks will have a mesh topology type. This is the
          default topology type for a tier created with a hierarchical tier
          definition.
      tier_group_name {String}:
          The existing tier group to which the new tier will be added. This
          parameter is required for domain networks with a hierarchical tier
          definition.
      subnetwork_field_name {String}:
          The name of the field where the subnetwork names for this tier
          will be stored. This is a system-maintained field that will be created
          the first time a tier is added to a tier group and reused for any
          additional tiers. For example, you have two tier groups: Distribution
          and Transmission. When you add a tier named system to the Distribution
          group and specify the subnetwork field name to be, the field is
          created. Next, you add a second tier named system to the Transmission
          group. This parameter will detect that thefield should be used as the
          subnetwork field name. This parameter is required for hierarchical
          tier types. systemsubnetsystemsubnet

        """