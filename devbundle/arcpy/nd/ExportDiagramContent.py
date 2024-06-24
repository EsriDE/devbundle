# Generated documentation for module arcpy.nd


class ExportDiagramContent(object):
    """
    Exports diagram content in a simple format (JSON) that reflects basic connectivity. Additional optional information such as diagram properties, diagram feature geometry, network element attributes, and aggregated elements can also be exported.
    """

    @property
    def description(self) -> str:
        return """

        ExportDiagramContent_nd(in_utility_network, network_diagram_name, out_file, {include_diagram_properties}, {include_geometries}, {include_attributes}, {include_aggregations}, {use_domains})

        Exports diagram content in a simple format (JSON) that reflects basic
        connectivity. Additional optional information such as diagram
        properties, diagram feature geometry, network element attributes, and
        aggregated elements can also be exported.

     INPUTS:
      in_utility_network (Utility Network / Trace Network / Utility Network Layer / Trace Network Layer / Diagram Layer):
          The utility network or trace network layer, utility network or trace
          network data element, or network diagram layer related to the network
          diagram to export.
      network_diagram_name (String):
          The name of the network diagram to export.
      include_diagram_properties {Boolean}:
          Specifies whether the diagram properties will be
          exported.INCLUDE_DIAGRAM_PROPERTIES-The diagram properties
          (statistics,
          creation and update dates, and so on) will be
          exported.EXCLUDE_DIAGRAM_PROPERTIES-The diagram properties will not be
          exported. This is the default.
      include_geometries {Boolean}:
          Specifies whether the geometry of the diagram features will be
          exported.INCLUDE_GEOMETRIES-Each diagram feature will be exported with
          its
          geometry.EXCLUDE_GEOMETRIES-Each diagram feature will be exported
          without its
          geometry. This is the default.
      include_attributes {Boolean}:
          Specifies whether the attributes of the associated network elements
          will be exported.INCLUDE_ATTRIBUTES-The associated network element
          attributes will be
          exported.EXCLUDE_ATTRIBUTES-The associated network element attributes
          will not
          be exported. This is the default.
      include_aggregations {Boolean}:
          Specifies whether each diagram feature will be exported with a list of
          network elements it aggregates.INCLUDE_AGGREGATIONS-Each diagram
          feature will be exported with a list
          of network elements it aggregates with their asset group and asset
          type values.EXCLUDE_AGGREGATIONS-The diagram feature aggregations will
          not be
          exported. This is the default.
      use_domains {Boolean}:
          Specifies how coded domain and subtype values will be exported. This
          parameter is enabled when the include_attributes parameter is set to
          INCLUDE_ATTRIBUTES or the include_aggregations parameter is set to
          INCLUDE_AGGREGATIONS.USE_CODED_VALUE_NAMES-Coded domain and subtype
          values will be exported
          using their string descriptions rather than raw
          values.DONT_USE_CODED_VALUE_NAMES-Coded domain and subtype values will
          be
          exported as raw values. This is the default.

     OUTPUTS:
      out_file (File):
          The output .json file that will be created with the exported diagram
          content.

        """