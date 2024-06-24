# Generated documentation for module arcpy.nd


class AddReduceJunctionRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically reduce diagram junctions during diagram buildings. This tool reduces junctions based on several network junction source classes and object tables according to the number of other junctions to which they are connected.
    """

    @property
    def description(self) -> str:
        return """

        AddReduceJunctionRule_nd(in_utility_network, template_name, is_active, inverse_source_selection, {junction_source;junction_source...}, {connectivity_options}, {unconnected_junctions}, {one_connected_junction}, {two_connected_junctions}, {edges_attributes;edges_attributes...}, {description})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically reduce diagram junctions during diagram
        buildings. This tool reduces junctions based on several network
        junction source classes and object tables according to the number of
        other junctions to which they are connected.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network containing the diagram template
          that will be modified.
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
      inverse_source_selection (String):
          Specifies how the specified junction source classes and object tables
          will be processed.EXCLUDE_SOURCE_CLASSES-Junctions that are based on
          the specified
          source classes and object tables will not be processed, while other
          junctions will be processed.INCLUDE_SOURCE_CLASSES-Only junctions that
          are based on the specified
          source classes and object tables will be processed. This is the
          default.
      junction_source {Table / Feature Class}:
          The network junction source class (or classes) and object table (or
          tables) that will be excluded or included depending on the rule
          process.When specifying the SystemJunctions class among the network
          junction
          source classes, the rule will systematically process both system
          junctions and system junction objects. When
          inverse_source_selection = "INCLUDE_SOURCE_CLASSES", the
          default, one or more network junction source classes or object tables
          will be processed. All diagram junctions related to network junctions
          that belong to those source classes and object tables are reduction
          candidates. The tool will process the junction source classes
          and object tables in
          the order of this list, from the junction class or table with the
          highest priority-the first class or table in the list-to the junction
          class or table with the lowest priority-the last class or table in the
          list.When inverse_source_selection = "EXCLUDE_SOURCE_CLASSES", no
          particular junction source class or object table must be specified. In
          this case, all junctions in the generated diagrams, regardless of
          their source class or object table, will be reduced.When specifying
          the SystemJunctions class among the network junction
          source classes, the rule will systematically process both system
          junctions and system junction objects.
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