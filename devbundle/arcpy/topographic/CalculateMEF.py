# Generated documentation for module arcpy.topographic


class CalculateMEF(object):
    """
    Calculates the maximum elevation figures (MEF) for each polygon cell or quadrangle in a polygon layer. These values are used as labels for the MEF feature layer.
    """

    @property
    def description(self) -> str:
        return """

        CalculateMEF_topographic(target_mef_features, in_terrain;in_terrain..., obstruction_features;obstruction_features..., mef_field, max_vo_field, max_terrain_field, specification, {terrain_elev_field}, {vo_allowance}, {vo_accuracy}, {terrain_accuracy})

        Calculates the maximum elevation figures (MEF) for each polygon cell
        or quadrangle in a polygon layer. These values are used as labels for
        the MEF feature layer.

     INPUTS:
      target_mef_features (Feature Layer):
          The input polygon features representing the quadrangle or cell that
          will be updated with MEF values.
      in_terrain (Raster Layer / Mosaic Layer / Feature Layer):
          The input terrain that will be used to determine elevation values in
          an MEF feature cell. If a point feature layer is used, elevation
          values are obtained from the field defined in the terrain_elev_field
          parameter.
      obstruction_features (Value Table):
          The layers that will be used to identify the highest human-made
          structure in a cell. This is a value table defining features,
          elevation fields, and elevation units.
      mef_field (Field):
          The existing field in the target_mef_features layer where the maximum
          elevation figure value will be stored.
      max_vo_field (Field):
          The field in the target_mef_features layer where the maximum vertical
          obstruction value will be stored.
      max_terrain_field (Field):
          The field in the target_mef_features layer where the maximum elevation
          values from the terrain layer will be stored.
      specification (String):
          Specifies the specification that will be used to calculate maximum
          elevation figures.JOG_MIL_J_89100-The Joint Operations Graphic
          specification will be
          used.ONC_MIL_O_89102-The Operational Navigation Chart specification
          will be
          used.TPC_MIL_T_89101-The Tactical Pilotage Chart will be
          used.STANAG_3591_ED6-The NATO Standard Agreement will be used.
      terrain_elev_field {Field}:
          A field in the in_terrain parameter value that represents the
          elevation values for each feature. If a point feature layer is used
          for the in_terrain value, this parameter is required. This parameter
          is unavailable if a raster or mosaic layer is used as input for the
          in_terrain parameter.
      vo_allowance {Linear Unit}:
          A vertical allowance value that will be added to each calculated MEF
          value. The value accounts for nonrepresented natural or manufactured
          features. The default is 150 feet.
      vo_accuracy {Linear Unit}:
          The accuracy of the vertical obstruction feature layer within a
          specified number of units. The default is 20 meters.
      terrain_accuracy {Linear Unit}:
          The accuracy of the terrain layer within a specified number of units.
          The default is 20 meters.

        """