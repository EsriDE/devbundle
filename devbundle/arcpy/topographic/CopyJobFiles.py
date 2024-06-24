# Generated documentation for module arcpy.topographic


class CopyJobFiles(object):
    """
    Copies Workflow Manager (Classic) job files to and from a local machine and a shared directory for processing.
    """

    @property
    def description(self) -> str:
        return """

        CopyJobFiles_topographic(job_id, source_path, target_path, {archive_source}, {delete_source}, {create_job_folder}, {database_path})

        Copies Workflow Manager (Classic) job files to and from a local
        machine and a shared directory for processing.

     INPUTS:
      job_id (Long):
          The Job ID of the Workflow Manager (Classic) job that will be updated.
      source_path (Folder):
          The path to the folder containing the files to be copied.
      target_path (Folder):
          The path to the location where the files will be copied.
      archive_source {Boolean}:
          Specifies whether the files in the source path will be zipped before
          copying to the target location.ARCHIVE-A .zip file with the contents
          of the source directory will be
          created and copied to the target location.NO_ARCHIVE-The contents of
          the source directory will be copied
          directly to the target location. This is the default.
      delete_source {Boolean}:
          Specifies whether the files in the source path will be deleted after
          the files are copied to the target location.DELETE_SOURCE-The source
          directory and all its contents will be
          deleted after the files are copied.NO_DELETE_SOURCE-The source
          directory will not be deleted after the
          files are copied. This is the default.
      create_job_folder {Boolean}:
          Specifies whether a folder will be created in the target path for
          containing the copied files.CREATE_JOB_FOLDER-A folder will be created
          in the target path with the
          name of the chosen job. Files are copied from the source path to this
          new folder.NO_CREATE_JOB_FOLDER-A folder will not be created, and
          files from the
          source path will be copied directly to the target path. This is the
          default.
      database_path {File}:
          The Workflow Manager (Classic) database connection file (.jtc) that
          contains the job information. If no connection file is specified, the
          default Workflow Manager (Classic) database will be used.

        """