
def set_null_foreign_key(child_table, child_col, parent_table, constraint_name):

    return f"""
        ALTER TABLE {child_table} DROP CONSTRAINT IF EXISTS {constraint_name};
        ALTER TABLE {child_table}
        ADD CONSTRAINT {constraint_name}
        FOREIGN KEY ({child_col})
        REFERENCES {parent_table}({child_col})
        ON DELETE SET NULL;
    """


"""
class Migration(migrations.Migration):

    dependencies = [
        ('src', '0013_alter_role_role_id_alter_user_user_id'),
    ]

    operations = [
        migrations.RunSQL(
            sql=set_null_foreign_key(
                child_table="users",
                child_col="role_id",
                parent_table="roles",
                constraint_name="users_role_id_1900a745_fk_roles_role_id"
            ),
            reverse_sql=set_null_foreign_key(
                child_table="users",
                child_col="role_id",
                parent_table="roles",
                constraint_name="users_role_id_1900a745_fk_roles_role_id"
            ).replace("ON DELETE SET NULL", "ON DELETE RESTRICT")
        )
    ]

"""