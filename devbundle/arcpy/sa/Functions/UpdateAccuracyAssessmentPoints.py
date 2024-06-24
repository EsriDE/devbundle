# Generated documentation for module arcpy.sa.Functions


class UpdateAccuracyAssessmentPoints(object):
    """
    Updates the Target field in the attribute table to compare reference points to the classified image.
    """

    @property
    def description(self) -> str:
        return """

        UpdateAccuracyAssessmentPoints_sa(in_class_data, in_points, out_points, {target_field}, {polygon_dimension_field}, {point_dimension_field})

        Updates the Target field in the attribute table to compare reference
        points to the classified image.

     INPUTS:
      in_class_data (Mosaic Layer / Raster Layer / Feature Layer):
          The input classification image or other thematic GIS reference data.
          The input can be a raster or feature class.Typical data is a
          classification image of a single band, integer data
          type.If using polygons as input, only use those that are not used as
          training samples. You can also use land-cover data in shapefile or
          feature class format.
      in_points (Feature Layer):
          The point feature class providing the accuracy assessment points to be
          updated.All points from this input will be copied to the updated
          output
          feature class, and the target_field parameter value will be updated
          from the input raster or feature class data.
      target_field {String}:
          Specifies whether the input data is a classified image or ground truth
          data.CLASSIFIED-The input is a classified image. This is the
          default.GROUND_TRUTH-The input is reference data.
      polygon_dimension_field {Field}:
          The dimension field for the in_points parameter value. The assessment
          points will be updated based on the matching dimension values with
          this field.
      point_dimension_field {Field}:
          The dimension field in the in_points parameter value. Input data with
          identical dimension values will be used to update corresponding
          points. When the in_class_data parameter value is a
          multidimensional
          raster, rasters with dimension values that match the dimension field
          in the test points will be used in updating. The multidimensional
          raster is expected to have one time dimension (field). Otherwise, the
          first dimension will be used to match the dimension field of the test
          points. StdTime

     OUTPUTS:
      out_points (Feature Class):
          The output point feature class that contains the updated random point
          field for accuracy assessment purposes.

        """