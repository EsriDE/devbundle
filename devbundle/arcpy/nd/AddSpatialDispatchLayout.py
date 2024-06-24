# Generated documentation for module arcpy.nd


class AddSpatialDispatchLayout(object):
    """
    Adds the Spatial Dispatch Layout algorithm to the list of layouts to be automatically chained at the end of the building of diagrams based on a given template. This tool also presets the Spatial Dispatch Layout algorithm parameters for any diagram based on that template.
    """

    @property
    def description(self) -> str:
        return """

        AddSpatialDispatchLayout_nd(in_utility_network, template_name, is_active, {are_containers_preserved}, {iterations_number}, {maximum_shift_factor})

        Adds the Spatial Dispatch Layout algorithm to the list of layouts to
        be automatically chained at the end of the building of diagrams based
        on a given template. This tool also presets the Spatial Dispatch
        Layout algorithm parameters for any diagram based on that template.

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
          The number of iterations to process. The default is 5.
      maximum_shift_factor {Double}:
          The maximum value used to increase the diagram junctions' displacement
          for junctions that are very close together. The greater the shift
          factor, the larger the separation between the diagram junctions that
          almost overlap. The default is 2.

        """