# Generated documentation for module arcpy.sa.Functions


class EditSignatures(object):
    """
    Edits and updates a signature file by merging, renumbering, and deleting class signatures.
    """

    @property
    def description(self) -> str:
        return """

        EditSignatures_sa(in_raster_bands;in_raster_bands..., in_signature_file, in_signature_remap_file, out_signature_file, {sample_interval})

        Edits and updates a signature file by merging, renumbering, and
        deleting class signatures.

     INPUTS:
      in_raster_bands (Composite Geodataset):
          The input raster bands for which to edit the signatures.They can be
          integer or floating point type.
      in_signature_file (File):
          Input signature file whose class signatures are to be edited.A .gsg
          extension is required.
      in_signature_remap_file (File):
          Input ASCII remap table containing the class IDs to be merged,
          renumbered, or deleted.The extension can be .rmp, .asc or .txt. The
          default is .rmp.
      sample_interval {Long}:
          The interval to be used for sampling.The default is 10.

     OUTPUTS:
      out_signature_file (File):
          The output signature file.A .gsg extension must be specified.

        """