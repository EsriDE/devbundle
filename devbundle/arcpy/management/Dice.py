# Generated documentation for module arcpy.management


class Dice(object):
    """
    Subdivides a feature into smaller features based on a specified vertex limit. This tool is intended as a way to subdivide extremely large features that cause issues with drawing, analysis, editing, and/or performance but are difficult to split up with standard editing and geoprocessing tools. This tool should not be used in any cases other than those where tools are failing to complete successfully due to the size of features.
    """

    @property
    def description(self) -> str:
        return """

        Dice_management(in_features, out_feature_class, vertex_limit)

        Subdivides a feature into smaller features based on a specified vertex
        limit. This tool is intended as a way to subdivide extremely large
        features that cause issues with drawing, analysis, editing, and/or
        performance but are difficult to split up with standard editing and
        geoprocessing tools. This tool should not be used in any cases other
        than those where tools are failing to complete successfully due to the
        size of features.

     INPUTS:
      in_features (Feature Layer):
          The input feature class or feature layer. The geometry type must be
          multipoint, line, or polygon.
      vertex_limit (Long):
          Features with geometries that exceed this vertex limit will be
          subdivided before being written to the output feature class.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class of diced features.

        """