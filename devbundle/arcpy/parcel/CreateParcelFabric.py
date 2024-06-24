# Generated documentation for module arcpy.parcel


class CreateParcelFabric(object):
    """
    Creates a parcel fabric and its associated datasets. The parcel fabric is created in a feature dataset that resides in a file, enterprise, or mobile geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        CreateParcelFabric_parcel(target_dataset, name, {config_keyword})

        Creates a parcel fabric and its associated datasets. The parcel fabric
        is created in a feature dataset that resides in a file, enterprise, or
        mobile geodatabase.

     INPUTS:
      target_dataset (Feature Dataset):
          The feature dataset in which the parcel fabric and related schema will
          be created. The feature dataset can reside in a file, enterprise, or
          mobile geodatabase.
      name (String):
          The name of the parcel fabric that will be created. Associated
          datasets will be prefixed with the parcel fabric name.
      config_keyword {String}:
          The configuration keyword applies to enterprise geodatabase data only.
          It determines the storage parameters of the database table.

        """