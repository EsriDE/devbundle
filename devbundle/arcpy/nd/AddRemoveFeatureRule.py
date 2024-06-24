# Generated documentation for module arcpy.nd


class AddRemoveFeatureRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically remove diagram features during diagram buildings. This rule removes diagram features based on different network source classes and object tables. You can constrain the removal of features based on connectivity.
    """

    @property
    def description(self) -> str:
        return """

        AddRemoveFeatureRule_nd(in_utility_network, template_name, is_active, source_type, inverse_source_selection, network_source;network_source..., {description}, {unconnected_junctions}, {one_connected_junction})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically remove diagram features during diagram
        buildings. This rule removes diagram features based on different
        network source classes and object tables. You can constrain the
        removal of features based on connectivity.

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
      source_type (String):
          Specifies the geometry type of the source class or object table that
          will be processed.JUNCTIONS-Only junction source classes or object
          tables (network
          polygon source classes, network point source classes, or junction
          object tables) will be processed.EDGES-Only edge source classes or
          object tables (network line source
          classes or edge object tables) will be processed.BOTH-Both junction
          and edge types will be processed. This is the
          default.
      inverse_source_selection (String):
          Specifies how the specified network source classes and object tables
          will be processed.EXCLUDE_SOURCE_CLASSES-Features and objects based on
          the specified
          network source classes and object tables will not be removed, while
          other features and objects will be
          removed.INCLUDE_SOURCE_CLASSES-Features and objects based on the
          specified
          network source classes and object tables will be removed. This is the
          default.
      network_source (Table / Feature Class):
          The network source class (or classes) and object table (or tables)
          that will be excluded or included depending on the rule process.By
          default, the inverse_source_selection parameter is set to
          INCLUDE_SOURCE_CLASSES, and one or more network source classes or
          object tables will be processed. All diagram features related to
          network features and objects that belong to those classes and object
          tables will be removed.When specifying the SystemJunctions class among
          the network source
          classes, the rule will systematically process both system junctions
          and system junction objects.
      description {String}:
          The description of the rule.
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

        """