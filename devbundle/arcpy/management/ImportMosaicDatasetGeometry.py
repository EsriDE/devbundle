# Generated documentation for module arcpy.management


class ImportMosaicDatasetGeometry(object):
    """
    Modifies the geometry for the footprints, boundary, or seamlines in a mosaic dataset to match those in a feature class.
    """

    @property
    def description(self) -> str:
        return """

        ImportMosaicDatasetGeometry_management(in_mosaic_dataset, target_featureclass_type, target_join_field, input_featureclass, input_join_field)

        Modifies the geometry for the footprints, boundary, or seamlines in a
        mosaic dataset to match those in a feature class.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset whose geometries you want to edit.
      target_featureclass_type (String):
          The geometry that you want to change.FOOTPRINT-The footprint polygons
          in the mosaic datasetSEAMLINE-The
          seamline polygons in the mosaic datasetBOUNDARY-The boundary polygon
          in the mosaic dataset
      target_join_field (Field):
          The field in the mosaic dataset to use as a basis for the join.
      input_featureclass (Feature Layer):
          The feature class with the new geometry.
      input_join_field (Field):
          The field in the input_featureclass to use as a basis for the join.If
          the input_featureclass has more than 1,000 records, add an index on
          this field by running the Add_Attribute_Index tool. If your mosaic
          dataset is very large and the join field is not indexed, the tool will
          take much longer to complete.

        """