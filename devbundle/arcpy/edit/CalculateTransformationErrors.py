# Generated documentation for module arcpy.edit


class CalculateTransformationErrors(object):
    """
    Calculates residue errors and the root mean square error (RMSE) based on the coordinates of the input links between known control points to be used for spatial data transformation.
    """

    @property
    def description(self) -> str:
        return """

        CalculateTransformationErrors_edit(in_link_features, out_link_table, {method})

        Calculates residue errors and the root mean square error (RMSE) based
        on the coordinates of the input links between known control points to
        be used for spatial data transformation.

     INPUTS:
      in_link_features (Feature Layer):
          The input link features that link known control points for spatial
          transformation.
      method {String}:
          Specifies the transformation method that will be used to convert the
          input feature coordinates.AFFINE-A minimum of three transformation
          links is required. This is
          the default.PROJECTIVE-A minimum of four transformation links is
          required.SIMILARITY-A minimum of two transformation links is required.

     OUTPUTS:
      out_link_table (Table):
          The output table containing the input links feature IDs and their
          residual errors. The residual errors for input links will be written
          to the specified output table that contains the following
          fields:Orig_FID-The input link feature IDX_Source-The x-coordinate of
          the
          source or from the end location of
          the linkY_Source-The y-coordinate of the source or from the end
          location of
          the linkX_Destination-The x-coordinate of the destination or to the
          end
          location of the linkY_Destination-The y-coordinate of the destination
          or to the end
          location of the linkResidual_Error-The residual error of the
          transformed location

        """