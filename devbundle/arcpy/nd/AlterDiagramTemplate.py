# Generated documentation for module arcpy.nd


class AlterDiagramTemplate(object):
    """
    Alters the properties of a diagram template such as its name, how it handles vertices along input network edges, whether the related diagrams can be stored or extended, the margin between containers and their contents in these diagrams, the removal of its rule and layout, and the reset of the diagram layer definition to the default.
    """

    @property
    def description(self) -> str:
        return """

        AlterDiagramTemplate_nd(in_utility_network, template_name, {out_name}, {is_default_template}, {are_rules_and_layouts_removed}, {are_vertices_kept}, {container_margin}, {is_diagram_storage_enabled}, {is_diagram_extension_enabled}, {description}, {are_layer_definitions_removed})

        Alters the properties of a diagram template such as its name, how it
        handles vertices along input network edges, whether the related
        diagrams can be stored or extended, the margin between containers and
        their contents in these diagrams, the removal of its rule and layout,
        and the reset of the diagram layer definition to the default.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network of the diagram template to alter.
      template_name (String):
          The name of the diagram template to alter.
      out_name {String}:
          The new name of the template.
      is_default_template {Boolean}:
          Specifies the default status of the input
          template.DEFAULT_TEMPLATE-The input diagram template will be the
          default
          template.NOT_DEFAULT_TEMPLATE-The input diagram template will not be
          the
          default template. This is the default.The default template is used
          when generating a diagram if a template
          is not specified.
      are_rules_and_layouts_removed {Boolean}:
          Specifies whether the template rule and layout definitions will be
          removed.REMOVE_RULES_AND_LAYOUTS-The rule and layout definitions
          related to
          the input diagram template will be
          removed.DO_NOT_REMOVE_RULES_AND_LAYOUTS-The rule and layout
          definitions
          related to the input diagram template will not be removed. This is the
          default.
      are_vertices_kept {Boolean}:
          Specifies how vertices along the GIS edges will be managed in the
          diagrams based on the template.KEEP_VERTICES-All vertices that display
          along GIS edges will be
          preserved on the associated edges in each network diagram based on the
          template.DO_NOT_KEEP_VERTICES-Diagram edges will be drawn as straight
          lines
          between their connected junctions. This is the default.
      container_margin {Linear Unit}:
          The minimum distance between the center of any junctions inside the
          container and the container border.
      is_diagram_storage_enabled {Boolean}:
          Specifies whether the diagrams based on the template can be
          stored.ENABLE_DIAGRAM_STORAGE-The diagrams based on the template can
          be
          stored. This is the default.DISABLE_DIAGRAM_STORAGE-The diagrams based
          on the template cannot be
          stored.
      is_diagram_extension_enabled {Boolean}:
          Specifies whether the diagrams based on the template can be
          extended.ENABLE_DIAGRAM_EXTENSION-The diagrams based on the template
          can be
          extended by connectivity, traversability, containment, or
          attachment.DISABLE_DIAGRAM_EXTENSION-The diagrams based on the
          template cannot be
          extended. This is the default.
      description {String}:
          The description of the template.
      are_layer_definitions_removed {Boolean}:
          Specifies whether the diagram template layer definition will be reset
          to the default.REMOVE_LAYER_DEFINITIONS-The diagram layer definition
          related to the
          input diagram template will be reset to the default
          (removed).DO_NOT_REMOVE_LAYER_DEFINITIONS-The diagram layer definition
          related
          to the input diagram template will not be removed. This is the
          default.

        """