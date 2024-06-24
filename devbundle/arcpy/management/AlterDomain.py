# Generated documentation for module arcpy.management


class AlterDomain(object):
    """
    Alters the properties of an existing attribute domain in a workspace.
    """

    @property
    def description(self) -> str:
        return """

        AlterDomain_management(in_workspace, domain_name, {new_domain_name}, {new_domain_description}, {split_policy}, {merge_policy}, {new_domain_owner})

        Alters the properties of an existing attribute domain in a workspace.

     INPUTS:
      in_workspace (Workspace):
          The geodatabase that contains the domain that will be altered.
      domain_name (String):
          The name of the domain the will be altered.
      new_domain_name {String}:
          The new name of the domain.
      new_domain_description {String}:
          The new description of the domain.
      split_policy {String}:
          Specifies the split policy that will used for the domain. The behavior
          of an attribute's values when a feature is split is controlled by its
          split policy.DEFAULT-The attributes of the two resulting features will
          be the
          default value of the attribute of the given feature class or
          subtype.DUPLICATE-The attribute of the two resulting features will be
          a copy
          of the original object's attribute value.GEOMETRY_RATIO-The attributes
          of resulting features will be a ratio of
          the original feature's value. The ratio is based on the proportion
          into which the original geometry is divided. If the geometry is
          divided equally, the attribute of each new feature will be one-half
          the value of the original object's attribute. This option only applies
          to range domains.
      merge_policy {String}:
          Specifies the merge policy that will be used for the domain. When two
          features are merged into a single feature, merge policies will control
          attribute values in the new feature. This parameter is only applicable
          to range domains, as coded value domains can only use the default
          merge policy.DEFAULT-The attribute of the resulting feature will be
          the default
          value of the attribute of the given feature class or subtype. This
          option only applies to nonnumeric fields and coded value
          domains.SUM_VALUES-The attribute of the resulting feature will be on
          the sum
          of the values from the original feature's attribute. This option only
          applies to range domains.AREA_WEIGHTED-The attribute of the resulting
          feature will be the
          weighted average of the attribute values of the original features. The
          average is based on the original feature's geometry. This option only
          applies to range domains.
      new_domain_owner {String}:
          The name of the database user that the domain ownership will be
          transferred to. Ensure that the new domain owner exists in the
          database; the tool does not check the validity of the owner name
          specified. This parameter is not applicable for domains created in a
          file geodatabase.

        """