# Generated documentation for module arcpy.nd


class AddAngleDirectedLayout(object):
    """
    Adds the Angle Directed Layout algorithm to the list of layouts to be automatically chained at the end of the generation of diagrams based on a given template. This tool also presets the Angle Directed Layout algorithm parameters for any diagram based on that template.
    """

    @property
    def description(self) -> str:
        return """

        AddAngleDirectedLayout_nd(in_utility_network, template_name, is_active, {are_containers_preserved}, {iterations_number}, {number_of_directions})

        Adds the Angle Directed Layout algorithm to the list of layouts to be
        automatically chained at the end of the generation of diagrams based
        on a given template. This tool also presets the Angle Directed Layout
        algorithm parameters for any diagram based on that template.

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
      are_containers_preserved {Boolean}:
          Specifies how the algorithm will process
          containers.PRESERVE_CONTAINERS-The layout algorithm will apply to the
          top graph
          of the diagram so containers are preserved.IGNORE_CONTAINERS-The
          layout algorithm will apply to both content and
          noncontent features in the diagram. This is the default.
      iterations_number {Long}:
          The number of iterations to process. The default is 1.
      number_of_directions {String}:
          The number of directions that will be used to align the diagram edges
          and their connected junctions.TWELVE_DIRECTIONS-The edges will move so
          they progressively approach
          one of the 12 axes, starting with the edge's origin junction and
          inclined at 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, or 360
          degrees.EIGHT_DIRECTIONS-The edges will move so they progressively
          approach
          one of the 8 axes, starting with the edge's origin junction and
          inclined at 45, 90, 135, 180, 225, 270, 315, or 360 degrees. This is
          the default.FOUR_DIRECTIONS-The edges will move so they progressively
          approach one
          of the 4 axes, starting with the edge's origin junction and inclined
          at 90, 180, 270, or 360 degrees.

        """