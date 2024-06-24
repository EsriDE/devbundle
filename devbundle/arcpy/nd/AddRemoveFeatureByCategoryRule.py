# Generated documentation for module arcpy.nd


class AddRemoveFeatureByCategoryRule(object):
    """
    Adds a diagram rule to automatically remove diagram features during diagram building based on an existing template. This removal depends on whether the diagram features are tagged with specific network categories. You can also constrain the removal of features based on connectivity.
    """

    @property
    def description(self) -> str:
        return """

        AddRemoveFeatureByCategoryRule_nd(in_utility_network, template_name, is_active, source_type, inverse_category_selection, category;category..., {unconnected_junctions}, {one_connected_junction}, {description})

        Adds a diagram rule to automatically remove diagram features during
        diagram building based on an existing template. This removal depends
        on whether the diagram features are tagged with specific network
        categories. You can also constrain the removal of features based on
        connectivity.

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
      source_type (String):
          Specifies the geometry type of the network elements that will be
          processed.JUNCTIONS-Only junction features or junction objects
          (network polygon
          source classes, network point source classes, or junction object
          tables) will be processed.EDGES-Only edge features or edge objects
          will be processedBOTH-Both junction and edge types will be processed.
          This is the
          default.
      inverse_category_selection (String):
          Specifies how the network features or network objects that are tagged
          with the specified network categories will be
          processed.EXCLUDE_CATEGORIES-Network features and objects that are
          tagged with
          the specified network categories will not be removed, while any other
          network features and objects will be removed. This is the
          default.INCLUDE_CATEGORIES-Network features and objects that are
          tagged with
          the specified network categories will be removed.
      category (String):
          The network categories that will be excluded or included depending on
          the inverse_category_selection parameter value.If the
          inverse_category_selection parameter is set to
          INCLUDE_CATEGORIES, one or more network categories must be specified.
          All network features and objects that are tagged with the specified
          categories will be removed from the generated diagrams.If the
          inverse_category_selection parameter is set to
          EXCLUDE_CATEGORIES, the network features and objects that are tagged
          with the specified categories will not be removed from the generated
          diagrams, while network features and objects that are not tagged with
          the specified categories will be removed.
      unconnected_junctions {Boolean}:
          Specifies whether diagram junction and diagram container candidates
          must be unconnected to be removed.MUST_BE_UNCONNECTED-Diagram junction
          and diagram container candidates
          must be unconnected to be removed.NO_CONSTRAINT-Neither diagram
          junction nor diagram container
          candidates need to be unconnected to be removed. This is the
          default.This parameter is only used when the source_type parameter is
          set to
          JUNCTIONS.
      one_connected_junction {Boolean}:
          Specifies whether diagram junction and diagram container candidates
          must be connected to a single diagram junction or diagram container to
          be removed.MUST_BE_CONNECTED_TO_SINGLE_JUNCTION-Diagram junction and
          diagram
          container candidates must be connected to a single diagram junction or
          diagram container to be removed.NO_CONSTRAINT-Neither diagram junction
          nor diagram container
          candidates need to be connected to a single diagram junction or
          diagram container to be removed. This is the default.This parameter is
          only used when the source_type parameter is set to
          JUNCTIONS.
      description {String}:
          The description of the rule.

        """