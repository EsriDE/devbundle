# Generated documentation for module arcpy.wmx


class UpgradeWorkflowDatabase(object):
    """
    Upgrades an existing Workflow Manager (Classic) database with the latest schema and configuration. The Workflow Manager (Classic) database is used to store the job and configuration information for your work management system and one feature class that is used to store the geometries for the location of interest (LOI) for your jobs.
    """

    @property
    def description(self) -> str:
        return """

        UpgradeWorkflowDatabase_wmx(Input_Database_Connection, {User_Store})

        Upgrades an existing Workflow Manager (Classic) database with the
        latest schema and configuration. The Workflow Manager (Classic)
        database is used to store the job and configuration information for
        your work management system and one feature class that is used to
        store the geometries for the location of interest (LOI) for your jobs.

     INPUTS:
      Input_Database_Connection (Workspace):
          The location of the enterprise geodatabase connection file to the
          Workflow Manager (Classic) database, which contains Workflow Manager
          (Classic) system tables. The connection file must connect directly to
          the database, and the connection should be made as a database owner.
      User_Store {String}:
          Specifies the user store from which the users and roles will be
          retrieved. The users can be imported from a portal and are assigned to
          roles created in the Workflow Manager (Classic) repository. The portal
          user profile information cannot be edited using ArcGIS Workflow
          Manager (Classic) Administrator. The users and roles can be created in
          the Workflow Manager (Classic) repository using the Traditional
          option. When using the Traditional option, the users and roles may be
          imported from the Active Directory in ArcGIS Workflow Manager
          (Classic) Administrator.PORTAL-The users will be imported from the
          portal you are currently
          signed in to.TRADITIONAL-The users and roles will be created in the
          Workflow
          Manager (Classic) repository using ArcGIS Workflow Manager (Classic)
          Administrator. Users and roles can be imported from the Active
          Directory when this option is used. This is the default.

        """