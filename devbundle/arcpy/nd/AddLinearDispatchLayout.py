# Generated documentation for module arcpy.nd


class AddLinearDispatchLayout(object):
    """
    Adds the Linear Dispatch Layout algorithm to the list of layouts to be automatically chained at the end of the building of diagrams based on a given template. This tool also presets the Linear Dispatch Layout algorithm parameters for any diagram based on that template.
    """

    @property
    def description(self) -> str:
        return """

        AddLinearDispatchLayout_nd(in_utility_network, template_name, is_active, {junction_placement_type}, {is_unit_absolute}, {maximum_shift_absolute}, {maximum_shift_proportional}, {minimum_shift_absolute}, {minimum_shift_proportional}, {iterations_number}, {is_path_preserved}, {are_leaves_moved}, {are_leaves_expanded}, {expand_shift_absolute}, {expand_shift_proportional})

        Adds the Linear Dispatch Layout algorithm to the list of layouts to be
        automatically chained at the end of the building of diagrams based on
        a given template. This tool also presets the Linear Dispatch Layout
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
      junction_placement_type {String}:
          Specifies how the junctions will be moved.EQUAL_DISTANCE-All junctions
          with two connected edges will be moved so
          the distances between them and their two connected junctions are
          equal. This is the default.USER_DEFINE_DISTANCE-All junctions with two
          connected edges will be
          moved so there is a minimum distance (the minimum_shift_ parameter
          value) between them and the other end of the edges to which they
          connect. This occurs at the end of the layout algorithm
          process.ITERATIVE_DISTANCE-All junctions with two connected edges will
          be
          moved slightly according to the iterations_number and maximum_shift_
          parameter values.
      is_unit_absolute {Boolean}:
          Specifies how parameters representing distances will be
          interpreted.ABSOLUTE_UNIT-The layout algorithm will interpret distance
          values as
          linear units.PROPORTIONAL_UNIT-The layout algorithm will interpret
          distance values
          as relative units to an estimation of the average of the junction
          sizes in the current diagram extent. This is the default.
      maximum_shift_absolute {Linear Unit}:
          The maximum distance the junctions with two connections will be spaced
          from the junctions to which they connect. The default is 2 in the
          units of the diagram's coordinate system. At the time this distance is
          reached, junctions will not be moved during additional iterations.
          This parameter can only be used with the ITERATIVE_DISTANCE junction
          placement type and absolute units.
      maximum_shift_proportional {Double}:
          The maximum distance the junctions with two connections will be spaced
          from the junctions to which they connect. The default is 2. At the
          time this distance is reached, junctions will not be moved during
          additional iterations. This parameter can only be used with the
          ITERATIVE_DISTANCE junction placement type and proportional units.
      minimum_shift_absolute {Linear Unit}:
          The minimum distance that will separate each junction with two
          connected edges from its two edge extremities after the layout
          algorithm runs. The default is 2 in the units of the diagram's
          coordinate system. When this parameter value is too large, the
          junctions with two connections are moved so the distances between each
          moved junction and its edge extremities are equal along the path
          defined by its two connected edges. This parameter can only be used
          with the USER_DEFINE_DISTANCE junction placement type and absolute
          units.
      minimum_shift_proportional {Double}:
          The minimum distance that will separate each junction with two
          connected edges from its two edge extremities after the layout
          algorithm runs. The default is 2. When this parameter value is too
          large, the junctions with two connections are moved so the distances
          between each moved junction and its edge extremities are equal along
          the path defined by its two connected edges. This parameter is used
          with the USER_DEFINE_DISTANCE junction placement type and proportional
          units.
      iterations_number {Long}:
          The number of iterations that will be processed. The default is 5.
          This parameter can only be used with the ITERATIVE_DISTANCE junction
          placement type.
      is_path_preserved {Boolean}:
          Specifies how vertices along edges will be processed.PRESERVE_PATH-All
          vertices along the connected edges will be
          preserved, and new vertices will be added at the moved junctions'
          original locations. This is the default.IGNORE_PATH-Vertices along
          edges will not be preserved.
      are_leaves_moved {Boolean}:
          Specifies whether leaf junctions-junctions with one connection-will be
          moved during the layout algorithm process.MOVE_LEAVES-Leaf junctions
          will be moved.DO_NOT_MOVE_LEAVES-Leaf
          junctions will not be moved. This is the
          default unless the specified input network diagram is based on a
          template for which the Linear Dispatch Layout algorithm has been
          configured with another parameter value.
      are_leaves_expanded {Boolean}:
          Specifies whether leaf junctions will be expanded:EXPAND_LEAVES-Leaf
          junctions will be expanded. The
          expand_shift_absolute parameter value specifies the maximum distance
          the leaf junctions can be expanded from the junctions to which they
          connect.DO_NOT_EXPAND_LEAVES-Leaf junctions will not be expanded. This
          is the
          default unless the specified input network diagram is based on a
          template for which the Linear Dispatch Layout algorithm has been
          configured with another parameter value.
      expand_shift_absolute {Linear Unit}:
          The maximum distance leaf junctions will be expanded from the
          junctions to which they connect. The default is 2 in the units of the
          diagram's coordinate system unless the specified input network diagram
          is based on a template for which the Linear Dispatch Layout algorithm
          has been configured with another parameter value. At the time this
          distance is reached, leaf junctions will not be moved during
          additional iterations. This parameter can only be used with
          theparameter and absolute units. Expand leaves
      expand_shift_proportional {Double}:
          The maximum distance the leaf junctions will be expanded from
          the junctions to which they connect. The default is 2 unless the
          specified input network diagram is based on a template for which the
          Linear Dispatch Layout algorithm has been configured with another
          parameter value. At the time this distance is reached, leaf junctions
          will not be moved during additional iterations. This parameter can
          only be used with theparameter and proportional units. Expand
          leaves

        """