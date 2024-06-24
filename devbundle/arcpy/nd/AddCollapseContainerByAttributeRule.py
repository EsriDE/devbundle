# Generated documentation for module arcpy.nd


class AddCollapseContainerByAttributeRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically collapse all contents related to containers during diagram buildings. The containers with contents to be collapsed are identified using an SQL query based on their attributes.
    """

    @property
    def description(self) -> str:
        return """

        AddCollapseContainerByAttributeRule_nd(in_utility_network, template_name, is_active, container_source, {where_clause}, {description}, {reconnected_edges_option})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically collapse all contents related to containers
        during diagram buildings. The containers with contents to be collapsed
        are identified using an SQL query based on their attributes.

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
      container_source (Table / Feature Class):
          The container source class or object table that references the
          containers with the contents to be collapsed.
      where_clause {SQL Expression}:
          An SQL expression that will be used to select the subset of containers
          in this source class or object table with the contents to be collapsed
          in the generated diagrams. For more information about SQL syntax, see
          SQL reference for query expressions used in ArcGIS.
      description {String}:
          The description of the rule.
      reconnected_edges_option {Boolean}:
          Specifies whether edges that are reconnected to the collapsed
          junctions will be aggregated.DONT_AGGREGATE_RECONNECTED_EDGES-Any edge
          connecting a content
          junction will be kept and reconnected to the collapsed container
          junction.AGGREGATE_RECONNECTED_EDGES-Any edge connecting a content
          junction
          will be replaced by a reduction edge that is reconnected to the
          collapsed container junction. Multiple edges between two collapsed
          junctions will be systematically aggregated under the same reduction
          edge. This is the default.

        """