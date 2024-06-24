# Generated documentation for module arcpy.indoors


class GenerateIndoorPathways(object):
    """
    Generates preliminary pathways that are cut according to obstructions, such as walls or columns, on selected levels in one or more facilities.
    """

    @property
    def description(self) -> str:
        return """

        GenerateIndoorPathways_indoors(in_level_features, in_detail_features, target_pathways, {lattice_rotation}, {lattice_density}, {restricted_unit_features}, {restricted_unit_exp}, {detail_exp})

        Generates preliminary pathways that are cut according to obstructions,
        such as walls or columns, on selected levels in one or more
        facilities.

     INPUTS:
      in_level_features (Feature Layer):
          The input polygon features representing levels in facilities. In the
          Indoors model, this is the Levels layer. The tool honors selections
          and definition queries applied to the layer.
      in_detail_features (Feature Layer):
          The input polyline features representing architectural details that
          can serve as barriers to travel within a facility. In the Indoors
          model, this is the Details layer.If the input polyline layer contains
          feature representing both
          barriers (such as walls and windows) and nonbarriers (such as stairs
          and doorways), use the detail_exp parameter to identify which features
          represent barriers.
      target_pathways (Feature Layer):
          The feature class or feature layer to which generated pathway
          polylines will be written. In the Indoors model, this is the
          PrelimPathways layer.
      lattice_rotation {Double}:
          The number of degrees by which the input floors' primary travel
          direction is rotated clockwise from due west. If left blank, the tool
          will calculate a value based on the minimum bounding rectangle of each
          floor.The value must be between 0.0 and 180.0.
      lattice_density {Double}:
          The longest distance allowed between nodes in the generated lattice of
          pathways. The tool uses the unit of measure from the coordinate system
          of the Indoors dataset. The default value is 0.6.The value must be
          between 0.25 and 2.9.
      restricted_unit_features {Feature Layer}:
          The input polygon features representing restricted and unrestricted
          spaces within a facility. In the Indoors model, this is the Units
          layer.
      restricted_unit_exp {SQL Expression}:
          An SQL expression that will be used to select the
          restricted_unit_features parameter values where the tool will not
          generate pathways.
      detail_exp {SQL Expression}:
          An SQL expression used to select the in_detail_features parameter
          values across which the tool will not generate pathways.

        """