# Generated documentation for module arcpy.nd


class AddExpandContainerByCategoryRule(object):
    """
    Adds a diagram rule to automatically expand container contents during the building of diagrams based on an existing template. This expansion depends on whether the containers are tagged with specific network categories.
    """

    @property
    def description(self) -> str:
        return """

        AddExpandContainerByCategoryRule_nd(in_utility_network, template_name, is_active, containers_visibility, container_type, inverse_category_selection, category;category..., {description})

        Adds a diagram rule to automatically expand container contents during
        the building of diagrams based on an existing template. This expansion
        depends on whether the containers are tagged with specific network
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
      containers_visibility (Boolean):
          Specifies whether the containers stay visible after they are
          expanded.KEEP_VISIBLE-The containers will stay visible after they are
          expanded. This is the default.HIDE-The containers will be hidden
          after they are expanded.
      container_type (String):
          Specifies the geometry type of the container element the rule will
          process.JUNCTIONS-The Expand Container rule will process the junction
          and
          junction object containers only.EDGES-The Expand Container rule will
          process the edge and edge object
          containers only. Only the linear container will be processedBOTH-The
          Expand Container rule will process any container features
          and objects regardless of their type. Both junction and edge types
          will be processed. This is the default
      inverse_category_selection (String):
          Specifies how the containers that are tagged with the specified
          network categories will be processed.EXCLUDE_CATEGORIES-Containers
          that are tagged with the specified
          network categories will not be expanded, while other containers will
          be expanded. This is the default.INCLUDE_CATEGORIES-Containers that
          are tagged with the specified
          network categories will be expanded.
      category (String):
          The network categories that will be excluded or included depending on
          the inverse_category_selection parameter value.If the
          inverse_category_selection parameter is set to
          INCLUDE_CATEGORIES, one or more network categories must be specified.
          All containers that are tagged with the specified categories will be
          expanded in the generated diagrams.If the inverse_category_selection
          parameter is set to
          EXCLUDE_CATEGORIES, the contents related to any containers that are
          tagged with the specified categories will not be expanded in the
          generated diagrams, while contents related to containers that are not
          tagged with the specified categories will be expanded.
      description {String}:
          The description of the rule.

        """