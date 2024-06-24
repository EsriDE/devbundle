# Generated documentation for module arcpy.wmx


class CreateWorkflowDatabase(object):
    """
    Creates Workflow Manager (Classic) schema and configures an enterprise geodatabase as the Workflow Manager (Classic) database.
    """

    @property
    def description(self) -> str:
        return """

        CreateWorkflowDatabase_wmx(Input_Database_Connection, AOI_Spatial_Reference, Import_Configuration, {Input_Custom_Configuration}, {User_Store})

        Creates Workflow Manager (Classic) schema and configures an enterprise
        geodatabase as the Workflow Manager (Classic) database.

     INPUTS:
      Input_Database_Connection (Workspace):
          The location of the enterprise geodatabase connection file that will
          host the Workflow Manager (Classic) schema and configuration. The
          connection file must connect directly to the database, and the
          connection should be made as a database owner.
      AOI_Spatial_Reference (Coordinate System):
          The spatial reference of the AOI feature class. You can
          specify the spatial reference in the following ways:        Input the
          path to a .prj file, such as
          c:/workspace/watershed.prj.Define a spatial reference object-such as
          AOI_Spatial_Reference =
          arcpy.SpatialReference("c:/data/Africa/Carthage.prj") or
          AOI_Spatial_Reference = arcpy.SpatialReference('WGS 1984')-prior to
          using this tool, which you then use as the spatial reference
          parameter.
      Import_Configuration (String):
          Specifies the Workflow Manager (Classic) elements to be
          imported into the new Workflow Manager (Classic) database. The default
          is(Minimum Configuration in Python). Minimum
          configurationMinimum Configuration-Imports the basic elements that the
          Workflow
          Manager (Classic) system requires.Quick Configuration-Includes the
          Minimum Configuration elements plus
          samples for several elements. Custom Configuration-Specifies a
          Workflow Manager (Classic)
          configuration file in theparameter, exported from a preexisting
          database. Input Custom Configuration
      Input_Custom_Configuration {File}:
          A custom configuration file that was exported from an existing
          Workflow Manager (Classic) database.
      User_Store {String}:
          Specifies the user store from which the users and roles will be
          retrieved. The users can be imported from a portal and are assigned to
          roles created in the Workflow Manager (Classic) repository. The portal
          user profile information cannot be edited using ArcGIS Workflow
          Manager (Classic) Administrator. The users and roles can be created in
          the Workflow Manager (Classic) repository using the TRADITIONAL
          option. When using the TRADITIONAL option, the users and roles can be
          imported from the Active Directory in ArcGIS Workflow Manager
          (Classic) Administrator.PORTAL-The users will be imported from the
          portal you are currently
          signed in to.TRADITIONAL-The users and roles will be created in the
          Workflow
          Manager (Classic) repository using ArcGIS Workflow Manager (Classic)
          Administrator. Users and roles can be imported from the Active
          Directory when this option is used. This is the default.

        """