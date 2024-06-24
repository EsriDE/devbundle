# Generated documentation for module arcpy.parcel


class DuplicateParcels(object):
    """
    Duplicates parcels in the same parcel type or in a different parcel type or duplicates parcels multiple times to create strata parcels (floor levels).
    """

    @property
    def description(self) -> str:
        return """

        DuplicateParcels_parcel(in_parcel_polygon_features, record_name, duplicate_to_parcel_type, {repeat}, {update_field}, {start}, {increment})

        Duplicates parcels in the same parcel type or in a different parcel
        type or duplicates parcels multiple times to create strata parcels
        (floor levels).

     INPUTS:
      in_parcel_polygon_features (Feature Layer):
          The input parcel polygon layer containing the parcels that will be
          duplicated.
      record_name (String):
          The name of the parcel record that will be associated with the
          duplicated parcels. If the parcel record provided does not exist, it
          will be created and the duplicated parcels will be assigned to it.
      duplicate_to_parcel_type (String):
          The parcel type in which to duplicate the parcel. You can duplicate a
          parcel in the same parcel type or a different parcel type.
      repeat {Long}:
          The number of times the parcel will be duplicated. When duplicating
          parcels to create strata parcels, this parameter represents the number
          of floors that will be created.
      update_field {Field}:
          A numeric field (long) that will be incrementally updated with
          an integer number for each duplicated parcel. This parameter is
          typically used when duplicating parcels to create strata parcels
          (floor levels). If the parcel type supports the storage of strata
          parcels, thefield is used as the update field. FloorOrderThe
          number will start at the value specified for the start parameter
          and will increment by the value specified for the increment parameter.
      start {Long}:
          The starting value or floor level of the first parcel that will be
          duplicated.
      increment {Long}:
          The interval at which the value (floor level) in the update field will
          increase. For example, if the start number is 1 and the increment
          number is 2, the values will increase by 2 for each duplicated parcel
          (1, 3, 5, 7, and so on).

        """