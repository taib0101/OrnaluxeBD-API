"""
# give command : $ python3 manage.py makemigrations --empty src
# To Get constraint_name serach on postgres db
    # SELECT pg_constraint.conname 
      FROM pg_constraint JOIN pg_class ON pg_constraint.conrelid = pg_class.oid 
      WHERE pg_class.relname = 'users';

# nano backedn/src/migrations/0002_auto.py
"""

"""
from django.db import migrations

from src.migration_sql_helper import set_null_foreign_key

class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        # Parent Table: roles, Child Table: users, Foreign Key: role_id
        migrations.RunSQL(
            sql=set_null_foreign_key (
                child_table="users",
                child_col="role_id",
                parent_table="roles",
                constraint_name="users_role_id_1900a745_fk_roles_role_id"
            ),
            reverse_sql=set_null_foreign_key (
                child_table="users",
                child_col="role_id",
                parent_table="roles",
                constraint_name="users_role_id_1900a745_fk_roles_role_id"
            ).replace("ON DELETE SET NULL", "ON DELETE RESTRICT")
        ),

        # Parent Table: categories, Child Table: products, Foreign Key: category_id
        migrations.RunSQL(
            sql=set_null_foreign_key(
                child_table="products",
                child_col="category_id",
                parent_table="categories",
                constraint_name="products_category_id_a7a3a156_fk_categories_category_id"
            ),
            reverse_sql=set_null_foreign_key(
                child_table="products",
                child_col="category_id",
                parent_table="categories",
                constraint_name="products_category_id_a7a3a156_fk_categories_category_id"
            ).replace("ON DELETE SET NULL", "ON DELETE RESTRICT")
        ),
        
        # Parent Table: products, Child Table: product_images, Foreign Key: product_id
        migrations.RunSQL(
            sql=set_null_foreign_key(
                child_table="product_images",
                child_col="product_id",
                parent_table="products",
                constraint_name="product_images_product_id_28ebf5f0_fk_products_product_id"
            ),
            reverse_sql=set_null_foreign_key(
                child_table="product_images",
                child_col="product_id",
                parent_table="products",
                constraint_name="product_images_product_id_28ebf5f0_fk_products_product_id"
            ).replace("ON DELETE CASCADE", "ON DELETE RESTRICT")
        ),
        
        # Parent Table: products, Child Table: ratings, Foreign Key: product_id
        migrations.RunSQL(
            sql=set_null_foreign_key(
                child_table="ratings",
                child_col="product_id",
                parent_table="products",
                constraint_name="ratings_product_id_f8f993a8_fk_products_product_id"
            ),
            reverse_sql=set_null_foreign_key(
                child_table="ratings",
                child_col="product_id",
                parent_table="products",
                constraint_name="ratings_product_id_f8f993a8_fk_products_product_id"
            ).replace("ON DELETE SET NULL", "ON DELETE RESTRICT")
        )
    ]

"""

def set_null_foreign_key(child_table, child_col, parent_table, constraint_name):

    return f"""
        ALTER TABLE {child_table} DROP CONSTRAINT IF EXISTS {constraint_name};
        ALTER TABLE {child_table}
        ADD CONSTRAINT {constraint_name}
        FOREIGN KEY ({child_col})
        REFERENCES {parent_table}({child_col})
        ON DELETE SET NULL;
    """
