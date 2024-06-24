# Generated documentation for module arcpy.ia.Functions


class ComputeConfusionMatrix(object):
    """
    Computes a confusion matrix with errors of omission and commission and derives a kappa index of agreement, Intersection over Union (IoU), and an overall accuracy between the classified map and the reference data.
    """

    @property
    def description(self) -> str:
        return """

        ComputeConfusionMatrix_ia(in_accuracy_assessment_points, out_confusion_matrix)

        Computes a confusion matrix with errors of omission and commission and
        derives a kappa index of agreement, Intersection over Union (IoU), and
        an overall accuracy between the classified map and the reference data.

     INPUTS:
      in_accuracy_assessment_points (Feature Layer):
          The accuracy assessment point feature class created from the
          Create Accuracy Assessment Points tool, containing theandfields. These
          fields are both long integer field types. ClassifiedGrndTruth

     OUTPUTS:
      out_confusion_matrix (Table):
          The output file name of the confusion matrix in table format.The
          format of the table is determined by the output location and path.
          By default, the output will be a geodatabase table. If the path is not
          in a geodatabase, specify a .dbf extension to save it in dBASE format.

        """