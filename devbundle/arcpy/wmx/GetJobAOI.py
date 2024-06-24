# Generated documentation for module arcpy.wmx


class GetJobAOI(object):
    """
    Gets the job's location of interest (LOI) as a feature layer. The output layer has either the polygon representing the area of interest (AOI) of the job or point representing the point of interest (POI) of the job.
    """

    @property
    def description(self) -> str:
        return """

        GetJobAOI_wmx(Input_JobID, aoi_Layer, {Input_DatabasePath})

        Gets the job's location of interest (LOI) as a feature layer. The
        output layer has either the polygon representing the area of interest
        (AOI) of the job or point representing the point of interest (POI) of
        the job.

     INPUTS:
      Input_JobID (String):
          The ID of the job whose AOI is to be retrieved.
      Input_DatabasePath {File}:
          The Workflow Manager (Classic) database connection file for the input
          job. If no connection file is specified, the current default Workflow
          Manager (Classic) database in the project is used.

     OUTPUTS:
      aoi_Layer (Feature Layer):
          The layer name for the location of interest retrieved. The output
          layer has either the polygon representing the area of interest (AOI)
          of the job or point representing the point of interest (POI) of the
          job.

        """