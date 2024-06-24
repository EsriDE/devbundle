# Generated documentation for module arcpy.nd


class AddExpandContainerRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically expand container contents during diagram buildings. This rule expands all of the container contents in the diagrams.
    """

    @property
    def description(self) -> str:
        return """

        AddExpandContainerRule_nd(in_utility_network, template_name, is_active, containers_visibility, container_type, inverse_source_selection, {container_sources;container_sources...}, {description})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically expand container contents during diagram
        buildings. This rule expands all of the container contents in the
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
      containers_visibility (Boolean):
          Specifies whether the containers stay visible after they are
          expanded.KEEP_VISIBLE-The containers will stay visible after they are
          expanded. This is the default.HIDE-The containers will be hidden
          after they are expanded.
      container_type (String):
          Specifies the geometry type of the container source class or object
          table that will be processed.JUNCTIONS-Only junction container source
          classes or object tables
          (polygon container source classes, point container source classes, or
          container junction object tables) will be processed.EDGES-Only edge
          container source classes or object tables (linear
          container source classes or container edge object tables) will be
          processed.BOTH-All container source classes and object tables
          regardless of
          their type (both junction and edge types) will be processed. This is
          the default.
      inverse_source_selection (String):
          Specifies how the specified container source classes and object tables
          will be processed.EXCLUDE_SOURCE_CLASSES-Containers that are based on
          the specified
          source classes and object tables will not be expanded, while other
          containers will be expanded. This is the
          default.INCLUDE_SOURCE_CLASSES-Containers that are based on the
          specified
          source classes and object tables will be expanded.
      container_sources {Table / Feature Class}:
          The container source class (or classes) and object table (or tables)
          that will be excluded or included depending on the rule process.When
          inverse_source_selection = "EXCLUDE_SOURCE_CLASSES", no
          particular container source class or object table can be specified. In
          this case, all containers in the generated diagrams regardless of
          their source class or object table will be expanded. When
          inverse_source_selection = "INCLUDE_SOURCE_CLASSES", the particular
          container source class (or classes) and object table (or tables) to be
          expanded must be specified.When inverse_source_selection =
          "EXCLUDE_SOURCE_CLASSES", the
          containers belonging to the specified source classes or object tables
          will not be expanded in the generated diagrams; however, container
          features and container objects that don't belong to those source
          classes and tables will be expanded. Conversely, when
          inverse_source_selection = "INCLUDE_SOURCE_CLASSES", the containers
          belonging to the specified source classes and object tables will be
          expanded in the generated diagrams; however, container features and
          container objects that don't belong to those source classes and object
          tables will not be expanded.
      description {String}:
          The description of the rule.

        """