# Generated documentation for module arcpy.wmx


class CreateNewJobs(object):
    """
    Creates one or more jobs of the selected job type and assigns the jobs to a user or user group. The created jobs can be prioritized and assigned a polygon or point location of interest (LOI).
    """

    @property
    def description(self) -> str:
        return """

        CreateNewJobs_wmx(Input_DatabasePath, Job_Type, Number_of_Jobs, {Assignment_Type}, {Assign_To}, {Priority}, {Feature_Layer_LOI}, {Union})

        Creates one or more jobs of the selected job type and assigns the jobs
        to a user or user group. The created jobs can be prioritized and
        assigned a polygon or point location of interest (LOI).

     INPUTS:
      Input_DatabasePath (File):
          The Workflow Manager (Classic) database connection file that contains
          the job type information. If no connection file is specified, the
          current default Workflow Manager (Classic) database is used.
      Job_Type (String):
          The job type to be used for creating the new job.
      Number_of_Jobs (Long):
          The number of jobs to be created. This input is ignored if the
          Feature_Layer_LOI parameter has a value or if Union = "UNION".
      Assignment_Type {String}:
          Specifies the assignment type to use to assign new jobs. If no value
          is specified, the default value configured in the job type is
          used.Groups-The new jobs will be assigned to a group.Users-The new
          jobs
          will be assigned to a user.Unassigned-The new jobs will be unassigned.
      Assign_To {String}:
          The user or group to whom the new jobs will be assigned. The value is
          restricted to a user or group based on the selected assignment type.
      Priority {String}:
          The priority of the jobs that will be created. If no priority is
          specified, the default value configured in the job type is used.
      Feature_Layer_LOI {Feature Layer}:
          The polygon, point, or multipoint features whose geometry will be used
          to create the LOI of the new jobs. One job will be created for each
          feature in the layer unless Union = "UNION".
      Union {Boolean}:
          Specifies whether one job will be created with the union of all
          polygons, point, or multipoint in the input feature layer as the LOI
          of the job.UNION-One union polygon or multipont feature will be
          generated from
          the LOI features and one job will be created regardless of the input
          number of jobs.NO_UNION-Each feature in the input layer will be used
          to generate the
          LOI of one job. The total number of jobs created is equal to the total
          number of input features. This is the default.

        """