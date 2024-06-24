# Generated documentation for module arcpy.nd


class AddSetRootJunctionByAttributeRule(object):
    """
    Adds a diagram rule to automatically flag diagram junctions as root junctions during diagram building based on an existing template. This rule specifies root junctions based on a particular junction source class or object table and filters using their attributes.
    """

    @property
    def description(self) -> str:
        return """

        AddSetRootJunctionByAttributeRule_nd(in_utility_network, template_name, is_active, junction_source, {where_clause}, {description})

        Adds a diagram rule to automatically flag diagram junctions as root
        junctions during diagram building based on an existing template. This
        rule specifies root junctions based on a particular junction source
        class or object table and filters using their attributes.

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
          The network junction source class or object table to process. All
          diagram junctions related to network features or objects that belong
          to this source class or table are root junction candidates.
      where_clause {SQL Expression}:
          An optional SQL expression used to filter out the expected root
          junctions from the root junction candidates in the diagrams based on
          the input template. For more information on SQL syntax, see SQL
          reference for query expressions used in ArcGIS.
      description {String}:
          The description of the rule.

        """