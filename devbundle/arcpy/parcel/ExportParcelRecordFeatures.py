# Generated documentation for module arcpy.parcel


class ExportParcelRecordFeatures(object):
    """
    Exports the parcel features associated with a selected parcel record to individual feature classes. The tool exports parcel features that were created by and retired by the selected record.
    """

    @property
    def description(self) -> str:
        return """

        ExportParcelRecordFeatures_parcel(in_record_polygon_feature, target_feature_dataset)

        Exports the parcel features associated with a selected parcel record
        to individual feature classes. The tool exports parcel features that
        were created by and retired by the selected record.

     INPUTS:
      in_record_polygon_feature (Feature Layer):
          The parcel fabric records layer that contains the selected record
          polygon. Only one record polygon can be selected.
      target_feature_dataset (Feature Dataset):
          The feature dataset where the exported parcel fabric feature classes
          will reside. If you're using an existing feature class, the features
          will be overwritten with the exported features.

        """