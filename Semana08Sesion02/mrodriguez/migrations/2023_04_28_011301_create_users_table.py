from orator.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.increments("id")
            # agregando campos de la tabla
            table.string("name").unique()
            table.string("email").unique()
            table.timestamps()

    # para borrar tabla users
    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
