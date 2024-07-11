from models.__init__ import CONN, CURSOR


class Book:
    def __init__(self, name, date, author_id,id=None):
        self.name = name
        self.date = date
        self.id = id
        self.author_id = author_id


    @property
    def author_id(self):
        return self._author_id
    

    @author_id.setter
    def author_id(self, author_id):
        changed_author_id = int(author_id)
        if isinstance(changed_author_id, int) and changed_author_id > 0:
            self._author_id = changed_author_id


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise ValueError("Name must be greater than 2 characters!")

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) == 10:
            self._date = date
        else:
            raise ValueError("Date must be 10 characters!")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT,
            date TEXT,
            author_id INTEGER
            );
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO books (name, date, author_id)
            VALUES (?,?,?)
        """
        CURSOR.execute(sql, (self.name, self.date, self.author_id))
        CONN.commit()

        self.id = CURSOR.lastrowid

    @classmethod
    def create(cls, name, date, author_id):
        book = Book(name, date, author_id)
        book.save()
        return book

    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM books
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM books
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        return Book(id=row[0], name = row[1], date = row[2], author_id = row[3])
    


    @classmethod
    def all_books(cls):
        sql = """
            SELECT *
            FROM books
        """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]


    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books
        """
        CURSOR.execute(sql)
        CONN.commit()

    def __repr__(self):
        return(f'Book id={self.id} Book name={self.name} Book date={self.date}')
    