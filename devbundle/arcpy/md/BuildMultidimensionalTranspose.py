# Generated documentation for module arcpy.md


class BuildMultidimensionalTranspose(object):
    """
    Transposes a multidimensional raster dataset, which divides the multidimensional data along each dimension to optimize performance when accessing pixel values across all slices.
    """

    @property
    def description(self) -> str:
        return """

        BuildMultidimensionalTranspose_md(in_multidimensional_raster, {delete_transpose})

        Transposes a multidimensional raster dataset, which divides the
        multidimensional data along each dimension to optimize performance
        when accessing pixel values across all slices.

     INPUTS:
      in_multidimensional_raster (Raster Layer):
          The input CRF multidimensional raster dataset.
      delete_transpose {Boolean}:
          Specifies whether an existing transpose will be
          deleted.DELETE_TRANSPOSE-If a transpose exists, it will be deleted and
          no new
          transpose will be built.NO_DELETE_TRANSPOSE-If a transpose exists, it
          will be overwritten by
          the newly built transpose. This is the default.

        """