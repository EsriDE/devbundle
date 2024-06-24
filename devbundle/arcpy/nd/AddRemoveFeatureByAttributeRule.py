# Generated documentation for module arcpy.nd


class AddRemoveFeatureByAttributeRule(object):
    """
    Adds a diagram rule to the rule sequence specified on a diagram template to automatically remove diagram features during diagram buildings. The features that will be removed are queried by attributes from a given network source class or object table. You can also constrain the removal of features based on connectivity.
    """

    @property
    def description(self) -> str:
        return """

        AddRemoveFeatureByAttributeRule_nd(in_utility_network, template_name, is_active, network_source, {where_clause}, {description}, {unconnected_junctions}, {one_connected_junction})

        Adds a diagram rule to the rule sequence specified on a diagram
        template to automatically remove diagram features during diagram
        buildings. The features that will be removed are queried by attributes
        from a given network source class or object table. You can also
        constrain the removal of features based on connectivity.

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
          The network source class or object table that will be processed. All
          diagram features related to network features or objects that belong to
          this source class or object table are removal candidates.
      where_clause {SQL Expression}:
          An SQL expression that will be used to select the subset of network
          elements from the element removal candidates in the diagrams based on
          the input template. For more information about SQL syntax, see SQL
          reference for query expressions used in ArcGIS.
      description {String}:
          The description of the rule.
      unconnected_junctions {Boolean}:
          Specifies whether diagram junctions and diagram containers must be
          unconnected to be removed.MUST_BE_UNCONNECTED-Diagram junctions and
          diagram containers must be
          unconnected to be removed.NO_CONSTRAINT-Diagram junctions and diagram
          containers do not need to
          be unconnected to be removed. This is the default.This parameter can
          only be used when the specified network_source
          parameter value corresponds to junctions or containers in the network
          diagrams.
      one_connected_junction {Boolean}:
          Specifies whether diagram junctions and diagram containers must be
          connected to a single diagram junction or diagram container to be
          removed.MUST_BE_CONNECTED_TO_SINGLE_JUNCTION-Diagram junctions and
          diagram
          containers must be connected to a single diagram junction or diagram
          container to be removed.NO_CONSTRAINT-Diagram junctions and diagram
          containers do not need to
          be connected to a single diagram junction or diagram container to be
          removed. This is the default.This parameter can only be used when the
          specified network_source
          parameter value corresponds to junctions or containers in the network
          diagrams.

        """