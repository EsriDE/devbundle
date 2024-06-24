# Generated documentation for module arcpy.nd


class AddPartialOverlappingEdgesLayout(object):
    """
    Adds the Partial Overlapping Edges Layout algorithm to the list of layouts to be automatically chained at the end of the building of diagrams based on a given template. This tool also presets the Partial Overlapping Edges Layout algorithm parameters for any diagram based on that template.
    """

    @property
    def description(self) -> str:
        return """

        AddPartialOverlappingEdgesLayout_nd(in_utility_network, template_name, is_active, buffer_width_absolute, offset_absolute, {optimize_edges})

        Adds the Partial Overlapping Edges Layout algorithm to the list of
        layouts to be automatically chained at the end of the building of
        diagrams based on a given template. This tool also presets the Partial
        Overlapping Edges Layout algorithm parameters for any diagram based on
        that template.

     INPUTS:
      in_utility_network (Utility Network / Trace Network):
          The utility network or trace network containing the diagram template
          that will be modified.
      template_name (String):
          The name of the diagram template that will be modified.
      is_active (Boolean):
          Specifies whether the layout algorithm will automatically run when
          generating diagrams based on the specified template.
          ACTIVE-The added layout algorithm will automatically run
          during the generation of any diagram that is based on the
          template_name parameter value. This is the default. The
          parameter values specified for the layout algorithm are used to
          run the layout during diagram generation. They are also loaded by
          default when the algorithm is to be run on any diagram based on the
          input template.INACTIVE-All the parameter values currently specified
          for the added
          layout algorithm will be loaded by default when the algorithm is to be
          run on any diagram based on the input template.
      buffer_width_absolute (Linear Unit):
          The width of the buffer zone in which to search for collinear edge
          segments.
      offset_absolute (Linear Unit):
          The distance that will separate the detected edge segments.
      optimize_edges {Boolean}:
          Specifies how segments will be placed along edges:OPTIMIZE_EDGES-The
          placement of segments will be optimized in each set
          of collinear segments. This is done by focusing on their connections
          instead of their positions. Segments that cross each other can be
          repositioned so they do not cross.DO_NOT_OPTIMIZE_EDGES-The initial
          position of each segment will be
          maintained in the collinear segment set and crossings will be
          preserved. This is the default.

        """