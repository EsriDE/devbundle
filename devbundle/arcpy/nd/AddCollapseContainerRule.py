# Generated documentation for module arcpy.nd


class AddCollapseContainerRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically collapse container contents during diagram buildings. This rule collapses all of the container contents in the diagrams.
    """

    @property
    def description(self) -> str:
        return """

        AddCollapseContainerRule_nd(in_utility_network, template_name, is_active, container_type, inverse_source_selection, {container_sources;container_sources...}, {description}, {reconnected_edges_option})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically collapse container contents during diagram
        buildings. This rule collapses all of the container contents in the
        diagrams.

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
      container_type (String):
          Specifies the geometry type of the container source class or object
          table that will be processed.JUNCTIONS-Only junction container source
          classes and object tables
          (polygon container source classes, point container source classes, and
          container junction object tables) will be processed.EDGES-Only edge
          container source classes and object tables (linear
          container source classes or container edge object tables) will be
          processed.BOTH-All container source classes and object tables
          regardless of
          their type (both junction and edge types) will be processed. This is
          the default.
      inverse_source_selection (String):
          Specifies how the specified container source classes and object tables
          will be processed.EXCLUDE_SOURCE_CLASSES-Containers that are based on
          the specified
          source classes and object tables will not be collapsed, while other
          containers will be collapsed. This is the
          default.INCLUDE_SOURCE_CLASSES-Containers that are based on the
          specified
          source classes and object tables will be collapsed.
      container_sources {Table / Feature Class}:
          The container source class (or classes) and object table (or tables)
          that will be excluded or included depending on the rule process.When
          inverse_source_selection = "EXCLUDE_SOURCE_CLASSES", the rule can
          be configured without specifying a network source class or object
          table. In this case, it will collapse contents of any container source
          classes and object tables in the generated diagrams. When
          inverse_source_selection = "INCLUDE_SOURCE_CLASSES", the container
          source class (or classes) or object table (or tables) to be collapsed
          must be specified.When inverse_source_selection =
          "EXCLUDE_SOURCE_CLASSES", the contents
          related to any container features or container objects belonging to
          the specified classes or object tables will not be collapsed in the
          generated diagrams; however, contents related to container features
          and container objects that don't belong to those classes and object
          tables will be collapsed. Conversely, when inverse_source_selection =
          "INCLUDE_SOURCE_CLASSES", the contents related to any container
          features and container objects belonging to the specified source
          classes and object tables will be collapsed in the generated diagrams;
          however, contents related to container features and container objects
          that don't belong to those source classes and object tables will not
          be collapsed.
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