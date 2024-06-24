# Generated documentation for module arcpy.nd


class AddRadialTreeLayout(object):
    """
    Adds the Radial Tree Layout algorithm to the list of layouts to be automatically chained at the end of the building of diagrams based on a given template. This tool also presets the Radial Tree Layout algorithm parameters for any diagram based on that template.
    """

    @property
    def description(self) -> str:
        return """

        AddRadialTreeLayout_nd(in_utility_network, template_name, is_active, {are_containers_preserved}, {is_unit_absolute}, {initial_radius_absolute}, {initial_radius_proportional}, {disjoined_graph_absolute}, {disjoined_graph_proportional}, {radius_factor})

        Adds the Radial Tree Layout algorithm to the list of layouts to be
        automatically chained at the end of the building of diagrams based on
        a given template. This tool also presets the Radial Tree Layout
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
      is_unit_absolute {Boolean}:
          Specifies how parameters representing distances will be
          interpreted.ABSOLUTE_UNIT-The layout algorithm will interpret distance
          values as
          linear units.PROPORTIONAL_UNIT-The layout algorithm will interpret
          distance values
          as relative units to an estimation of the average of the junction
          sizes in the current diagram extent. This is the default.
      initial_radius_absolute {Linear Unit}:
          The radius of the first concentric circle whose center is the radial
          tree root junction-that is, the radius of the circle around which the
          diagram junctions belonging to the first hierarchical level are
          placed. The default is 5 in the units of the diagram's coordinate
          system. This parameter can only be used with absolute units.
      initial_radius_proportional {Double}:
          The radius of the first concentric circle whose center is the radial
          tree root junction-that is, the radius of the circle around which the
          diagram junctions belonging to the first hierarchical level are
          placed. The default is 5. This parameter can only be used with
          proportional units.
      disjoined_graph_absolute {Linear Unit}:
          The minimum spacing that will separate features belonging to disjoined
          graphs when the diagram contains such graphs. This parameter is used
          with absolute units. The default is 4 in the units of the diagram's
          coordinate system.
      disjoined_graph_proportional {Double}:
          The minimum spacing that will separate features belonging to disjoined
          graphs when the diagram contains such graphs. This parameter is used
          with proportional units. The default is 4.
      radius_factor {Double}:
          The multiplicative factor used to increase or decrease the radius of
          each concentric circle. It is also the distance that separates each
          concentric circle related to a hierarchical level. When using a radius
          factor less than 1, the distance that separates the diagram junctions
          belonging to the (n) hierarchical level and the (n+1) hierarchical
          level progressively decreases. With a factor greater than 1, the
          distance between the hierarchical levels increases progressively. The
          default is 1.

        """