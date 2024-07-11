from models.__init__ import CONN, CURSOR


class Author:
    def __init__(self, name, id=None):
        self.name = name
        self.id = id


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise ValueError("Name Must be greater than 2 characters!")
    

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            name TEXT
            );
        """
        CURSOR.execute(sql)
        CONN.commit()


    def save(self):
        sql = """
            INSERT INTO authors (name)
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid


    @classmethod
    def create(cls, name):
        author = Author(name)
        author.save()
        return author
    
    def delete(self):
        sql = """
            DELETE FROM authors
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()


    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM authors
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
        

    @classmethod
    def instance_from_db(cls, row):
        return Author(id=row[0], name = row[1])
    

    @classmethod
    def all_authors(cls):
        sql = """
            SELECT *
            FROM authors
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM authors
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None


    def __repr__(self):
        return(f'Author id={self.id} Author name={self.name}')