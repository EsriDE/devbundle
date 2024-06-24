# Generated documentation for module arcpy.nd


class AddReduceJunctionByCategoryRule(object):
    """
    Adds a diagram rule to automatically reduce junctions during the building of diagrams based on an existing template. This reduction depends on whether the junctions are tagged with specific network categories.
    """

    @property
    def description(self) -> str:
        return """

        AddReduceJunctionByCategoryRule_nd(in_utility_network, template_name, is_active, inverse_category_selection, category;category..., {connectivity_options}, {unconnected_junctions}, {one_connected_junction}, {two_connected_junctions}, {edges_attributes;edges_attributes...}, {description})

        Adds a diagram rule to automatically reduce junctions during the
        building of diagrams based on an existing template. This reduction
        depends on whether the junctions are tagged with specific network
        categories.

     INPUTS:
      in_utility_network (Utility Network):
          The utility network containing the diagram template that will be
          modified.
      template_name (String):
          The name of the diagram template that will be modified.
      is_active (Boolean):
          Specifies whether the rule will be enabled when generating and
          updating diagrams based on the specified template.ACTIVE-The added
          rule will become enabled during the generation and
          update of any diagrams based on the input template. This is the
          default.INACTIVE-The added rule will not become enabled during the
          generation
          or update of any diagrams based on the input template.
      inverse_category_selection (String):
          Specifies how the junctions that are tagged with the specified network
          categories will be reduced.EXCLUDE_CATEGORIES-Junctions that are
          tagged with the specified
          network categories will not be reduced, while other junctions will be
          reduced. This is the default.INCLUDE_CATEGORIES-Junctions that are
          tagged with the specified
          network categories will be reduced.
      category (String):
          The network categories that will be excluded or included depending on
          the inverse_category_selection parameter value.If the
          inverse_category_selection parameter is set to
          INCLUDE_CATEGORIES, one or more network categories must be specified.
          All junctions that are tagged with the specified categories will be
          reduced in the generated diagrams.If the inverse_category_selection
          parameter is set to
          EXCLUDE_CATEGORIES, the junctions that are tagged with the specified
          categories will not be reduced in the generated diagrams, while
          junctions that are not tagged with the specified categories will be
          reduced.
      connectivity_options {String}:
          Specifies the number of junction connections that will be considered
          for reduction.MAX_2_CONNECTED_JUNCTIONS-Junctions with two or fewer
          connections will
          be considered. In this case, a specific process will be run according
          to the number of candidate junction connections that will be reduced.
          This is the default.MIN_3_CONNECTED_JUNCTIONS-Junctions with three or
          more connections
          will be considered. In this case, upstream traces will be run to
          determine whether candidate junction connections will be reduced.
      unconnected_junctions {Boolean}:
          Specifies whether each unconnected network diagram junction candidate
          will be reduced. This parameter is only enabled when
          connectivity_options =
          "MAX_2_CONNECTED_JUNCTIONS".REDUCE_UNCONNECTED_JCT-Unconnected network
          diagram junction candidates
          will be reduced. Each junction will be
          removed.KEEP_UNCONNECTED_JCT-Unconnected network diagram junction
          candidates
          will not be reduced; they will be kept. This is the default.
      one_connected_junction {Boolean}:
          Specifies whether each network diagram junction reduction candidate
          that is connected to a single junction will be reduced. This parameter
          is only enabled when connectivity_options =
          "MAX_2_CONNECTED_JUNCTIONS".REDUCE_JCT_TO_1JCT-Network diagram
          junction reduction candidates that
          are connected to a single junction will be reduced. Each junction and
          its incident edge will be reduced onto its single connected
          junction.KEEP_JCT_TO_1JCT-Network diagram junction reduction
          candidates that
          are connected to a single junction will not be reduced; they will be
          kept. This is the default.
      two_connected_junctions {Boolean}:
          Specifies whether each network diagram junction reduction candidate
          that is connected to two other junctions will be reduced. This
          parameter is only enabled when connectivity_options =
          "MAX_2_CONNECTED_JUNCTIONS".REDUCE_JCT_TO_2JCTS-Network diagram
          junction reduction candidates that
          connect two other junctions will be reduced. Each junction and its
          incident edges will be reduced onto a super span edge (the reduction
          edge). This is the default.KEEP_JCT_TO_2JCTS-Network diagram junction
          reduction candidates that
          connect two other junctions will not be reduced; they will be kept.
      edges_attributes {String}:
          The alias of the edge attributes adjacent to the junction reduction
          candidate.The junction will be reduced only when all of its adjacent
          edges have
          the same values for each specified attribute alias.
      description {String}:
          The description of the rule.

        """