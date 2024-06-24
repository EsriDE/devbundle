# Generated documentation for module arcpy.nd


class AddReduceEdgeByAttributeRule(object):
    """
    Adds a diagram rule to automatically reduce diagram edges during diagram building based on an existing template. This rule can be set up to reduce diagram edges by attributes.
    """

    @property
    def description(self) -> str:
        return """

        AddReduceEdgeByAttributeRule_nd(in_utility_network, template_name, is_active, network_source, {where_clause}, {description}, {reconnected_edges_option})

        Adds a diagram rule to automatically reduce diagram edges during
        diagram building based on an existing template. This rule can be set
        up to reduce diagram edges by attributes.

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
      network_source (Table / Feature Class):
          The network edge source class or object table to reduce. All diagram
          edges related to network lines or edge objects that belong to this
          source class or object table are candidates for the reduction.
      where_clause {SQL Expression}:
          An SQL expression used to select the subset of network edges among the
          edges that are candidates for the reduction based on the input
          template. For more information on SQL syntax, see the SQL reference
          for query expressions used in ArcGIS help topic.
      description {String}:
          The description of the rule.
      reconnected_edges_option {Boolean}:
          Specifies whether the rule will aggregate the edges that are
          reconnected to the reduction
          junctions.DONT_AGGREGATE_RECONNECTED_EDGES-Any edge connecting a point
          along the
          edge that is reduced is reconnected to the reduction
          junction.AGGREGATE_RECONNECTED_EDGES-Any edge connecting a point along
          the edge
          that is reduced is replaced by a reduction edge. This reduction edge
          is reconnected to the reduction junction. This is the default.

        """