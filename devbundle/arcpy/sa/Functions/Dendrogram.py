# Generated documentation for module arcpy.sa.Functions


class Dendrogram(object):
    """
    Constructs a tree diagram (dendrogram) showing attribute distances between sequentially merged classes in a signature file.
    """

    @property
    def description(self) -> str:
        return """

        Dendrogram_sa(in_signature_file, out_dendrogram_file, {distance_calculation}, {line_width})

        Constructs a tree diagram (dendrogram) showing attribute distances
        between sequentially merged classes in a signature file.

     INPUTS:
      in_signature_file (File):
          Input signature file whose class signatures are used to produce a
          dendrogram.A .gsg extension is required.
      distance_calculation {Boolean}:
          Specifies the manner in which the distances between classes in
          multidimensional attribute space are defined.VARIANCE-The distances
          between classes will be computed based on the
          variances and the Euclidean distance between the means of their
          signatures.MEAN_ONLY-The distances between classes will be determined
          by the
          Euclidean distances between the means of the class signatures only.
      line_width {Long}:
          Sets the width of the dendrogram in number of characters on a line.The
          default is 78.

     OUTPUTS:
      out_dendrogram_file (File):
          The output dendrogram ASCII file.The extension can be .txt or .asc.

        """