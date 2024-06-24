# Generated documentation for module arcpy.nd


class AddReduceJunctionByAttributeRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically reduce diagram junctions during diagram buildings. The junctions that will be reduced are queried from a given network junction source class or object table by attributes according to the number of other junctions to which they are connected.
    """

    @property
    def description(self) -> str:
        return """

        AddReduceJunctionByAttributeRule_nd(in_utility_network, template_name, is_active, junction_source, {where_clause}, {connectivity_options}, {unconnected_junctions}, {one_connected_junction}, {two_connected_junctions}, {edges_attributes;edges_attributes...}, {description})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically reduce diagram junctions during diagram
        buildings. The junctions that will be reduced are queried from a given
        network junction source class or object table by attributes according
        to the number of other junctions to which they are connected.

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
      junction_source (Table / Feature Class):
          The network junction source class or object table that will be
          processed. All diagram junctions related to network junctions that
          belong to this source class or object table are reduction candidates.
      where_clause {SQL Expression}:
          An SQL expression that will be used to select the subset of network
          junctions from the junction reduction candidates in the diagrams based
          on the input template. For more information about SQL syntax, see SQL
          reference for query expressions used in ArcGIS.
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