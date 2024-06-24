# Generated documentation for module arcpy.nd


class AddCollapseContainerByCategoryRule(object):
    """
    Adds a diagram rule to automatically collapse container contents during the building of diagrams based on an existing template. The collapse depends on whether the containers are tagged with specific network categories.
    """

    @property
    def description(self) -> str:
        return """

        AddCollapseContainerByCategoryRule_nd(in_utility_network, template_name, is_active, container_type, inverse_category_selection, category;category..., {reconnected_edges_option}, {description})

        Adds a diagram rule to automatically collapse container contents
        during the building of diagrams based on an existing template. The
        collapse depends on whether the containers are tagged with specific
        network categories.

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
      container_type (String):
          Specifies the geometry type of the container element the rule will
          process.JUNCTIONS-The Collapse Container rule will process the
          junction and
          junction object containers only.EDGES-The Collapse Container rule
          will process the edge and edge
          object containers only. Only the linear container will be
          processedBOTH-The Collapse Container rule will process any container
          features
          and objects regardless of their type. Both junction and edge types
          will be processed. This is the default
      inverse_category_selection (String):
          Specifies how the containers that are tagged with the specified
          network categories will be processed.EXCLUDE_CATEGORIES-Containers
          that are tagged with the specified
          network categories will not be collapsed, while other containers will
          be collapsed. This is the default.INCLUDE_CATEGORIES-Containers that
          are tagged with the specified
          network categories will be collapsed.
      category (String):
          The network categories that will be excluded or included depending on
          the inverse_category_selection parameter value.If the
          inverse_category_selection parameter is set to
          INCLUDE_CATEGORIES, one or more network categories must be specified.
          All containers that are tagged with the specified categories will be
          collapsed in the generated diagrams.If the inverse_category_selection
          parameter is set to
          EXCLUDE_CATEGORIES, the contents related to any containers that are
          tagged with the specified categories will not be collapsed in the
          generated diagrams, while contents related to containers that are not
          tagged with the specified categories will be collapsed.
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
      description {String}:
          The description of the rule.

        """