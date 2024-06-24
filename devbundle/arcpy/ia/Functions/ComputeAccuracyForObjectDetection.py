# Generated documentation for module arcpy.ia.Functions


class ComputeAccuracyForObjectDetection(object):
    """
    Calculates the accuracy of a deep learning model by comparing the detected objects from the Detect Objects Using Deep Learning tool to ground truth data.
    """

    @property
    def description(self) -> str:
        return """

        ComputeAccuracyForObjectDetection_ia(detected_features, ground_truth_features, out_accuracy_table, {out_accuracy_report}, {detected_class_value_field}, {ground_truth_class_value_field}, {min_iou}, {mask_features})

        Calculates the accuracy of a deep learning model by comparing the
        detected objects from the Detect Objects Using Deep Learning tool to
        ground truth data.

     INPUTS:
      detected_features (Feature Class / Feature Layer):
          The polygon feature class containing the objects detected from the
          Detect Objects Using Deep Learning tool.
      ground_truth_features (Feature Class / Feature Layer):
          The polygon feature class containing ground truth data.
      detected_class_value_field {Field}:
          The field in the detected objects feature class that contains the
          class values or class names. If a field name is not specified,
          aorfield will be used. If
          these fields do not exist, all records will be identified as belonging
          to one class. ClassvalueValueThe class values or class names
          must match those in the ground
          reference feature class exactly.
      ground_truth_class_value_field {Field}:
          The field in the ground truth feature class that contains the class
          values. If a field name is not specified, aorfield will be
          used. If
          these fields do not exist, all records will be identified as belonging
          to one class. ClassvalueValueThe class values or class names
          must match those in the detected
          objects feature class exactly.
      min_iou {Double}:
          The IoU ratio to use as a threshold to evaluate the accuracy of the
          object-detection model. The numerator is the area of overlap between
          the predicted bounding box and the ground reference bounding box. The
          denominator is the area of union or the area encompassed by both
          bounding boxes. The IoU ranges from 0 to 1.
      mask_features {Feature Class / Feature Layer}:
          A polygon feature class that delineates the area or areas where
          accuracy will be computed. Only the features that intersect the mask
          will be assessed for accuracy.

     OUTPUTS:
      out_accuracy_table (Table):
          The output accuracy table.
      out_accuracy_report {File}:
          The name of the output accuracy report. The report is a PDF document
          containing accuracy metrics and charts.

        """