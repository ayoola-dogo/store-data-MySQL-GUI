import MySQLdb as mysql
import GuiDBConfig as guiConf


class MySQL:
    # class variable
    GUIDB = 'GuiDB'

    def connect(self):
        # Connect by unpacking dictionary credentials
        conn = mysql.connect(**guiConf.dbConfig)
        # create cursor
        cursor = conn.cursor()
        return conn, cursor

    def close(self, cursor, conn):
        # close cursor
        cursor.close()

        # close connection to MySQL
        conn.close()

    def showDBs(self):
        # connect to MySQL
        conn, cursor = self.connect()

        # Print results
        cursor.execute("SHOW DATABASES")
        print(cursor)
        print(cursor.fetchall())

        # close cursor and connection
        self.close(cursor, conn)

    def createGuiDB(self):
        # connect to MySQL
        conn, cursor = self.connect()

        try:
            cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(MySQL.GUIDB)
            )
        except mysql.Error as err:
            print("Failed to create DB: {}".format(err))

        # close cursor and connection
        self.close(cursor, conn)

    def dropGuiDB(self):
        # connect to MySQL
        conn, cursor = self.connect()
        try:
            cursor.execute(
                "DROP DATABASE {}".format(MySQL.GUIDB)
            )
        except mysql.Error as err:
            print("Failed to drop DB: {}".format(err))

        # close cursor and connection
        self.close(cursor, conn)

    def useGuiDB(self, cursor):
        # Takes in cursor of an open connection object
        '''Expect opens connection'''
        # select DB
        cursor.execute("USE {}".format(MySQL.GUIDB.lower()))

    def createTables(self):
        # connect to MySQL
        conn, cursor = self.connect()
        self.useGuiDB(cursor)
        # create Table inside DB
        cursor.execute("CREATE TABLE Books ("
                       "Book_ID INT NOT NULL AUTO_INCREMENT,"
                       "Book_Title VARCHAR(25) NOT NULL,"
                       "Book_Page INT NOT NULL,"
                       "PRIMARY KEY (Book_ID)"
                       ") ENGINE=InnoDB"
        )

        # create second Table inside DB
        cursor.execute("CREATE TABLE Quotations ("
                       "Quote_ID INT AUTO_INCREMENT,"
                       "Quotation VARCHAR(250),"
                       "Books_Book_ID INT,"
                       "PRIMARY KEY (Quote_ID),"
                       "FOREIGN KEY (Books_Book_ID)"
                       "    REFERENCES Books(Book_ID)"
                       "    ON DELETE CASCADE"
                       ") ENGINE=InnoDB")

        # close cursor and connection
        self.close(cursor, conn)

    def createTablesNoFk(self):
        # connect to MySQL
        conn, cursor = self.connect()
        self.useGuiDB(cursor)

        # create Table inside DB
        cursor.execute("CREATE TABLE Books ("
                       "Book_ID INT NOT NULL AUTO_INCREMENT,"
                       "Book_Title VARCHAR(25) NOT NULL,"
                       "Book_Page INT NOT NULL,"
                       "PRIMARY KEY (Book_ID)"
                       ") ENGINE=InnoDB")

        # create second Table inside DB
        # No FOREIGN KEY relation to Books Table
        cursor.execute("CREATE TABLE Quotations ("
                       "Quote_ID INT AUTO_INCREMENT,"
                       "Quotations VARCHAR(250),"
                       "Books_Book_ID INT,"
                       "PRIMARY KEY (Quote_ID)"
                       ") ENGINE=InnoDB")

        # close cursor and connection
        self.close(cursor, conn)

    def dropTables(self):
        # connect to MySQL
        conn, cursor = self.connect()
        self.useGuiDB(cursor)
        cursor.execute("DROP TABLE quotations")
        cursor.execute("DROP TABLE books")

        # close cursor and connection
        self.close(cursor, conn)

    def showTables(self):
        # connect to MySQL
        conn, cursor = self.connect()

        # show Tables from guidb DB
        cursor.execute("SHOW TABLES FROM guidb")
        print(cursor.fetchall())

        # close cursor and connection
        self.close(cursor, conn)

    def insertBooks(self, title, page, bookQuote):
        # connect to MySQL
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        # insert data
        cursor.execute("INSERT INTO books (Book_Title, Book_page) VALUES ({}, {})".format(title, page))

        # last inserted auto increment value
        keyID = cursor.lastrowid
        print(keyID)

        cursor.execute("INSERT INTO quotations (Quotation, Books_Book_ID) VALUES ({}, {})".format(bookQuote, keyID))

        # commit transaction
        conn.commit()

        # close cursor and connection
        self.close(cursor, conn)

    def insertBooksExample(self):
        # connect to MySQL
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        # insert hard-coded data
        cursor.execute("INSERT INTO books (Book_Title, Book_Page) VALUES ('Design Patterns', 17)")

        # last inserted auto increment value
        keyID = cursor.lastrowid
        print(keyID)

        cursor.execute("INSERT INTO quotations (Quotation, Books_Book_ID) VALUES ({}, {})"
                       .format('Programming to an interface, not an Implementation', keyID))

        # commit transaction
        conn.commit()

        # close cursor and connection
        self.close(cursor, conn)

    def showBooks(self):
        # connect to MySQL
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        # print results
        cursor.execute("SELECT * FROM Books")
        allBooks = cursor.fetchall()
        print(allBooks)

        # close cursor and connection
        self.close(cursor, conn)

    def showColumns(self):
        # connect to MySQL
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        # execute command
        cursor.execute("SHOW COLUMNS FROM quotations")
        print(cursor.fetchall())

        print('\n Pretty Print:\n-------------------------------------------------------------')
        from pprint import pprint
        # execute command
        cursor.execute("SHOW COLUMNS FROM quotations")
        pprint(cursor.fetachall())

        # close cursor and connection
        self.close(cursor, conn)

    def showData(self):
        # connect to MySQL
        conn, cursor = self.connect()
        self.useGuiDB(cursor)

        # execute command
        cursor.execute("SELECT * FROM books")
        print(cursor.fetchall())
        cursor.execute("SELECT * from quotations")
        print(cursor.fetchall())

        # close cursor and connection
        self.close(cursor, conn)

    def showDataWithReturn(self):
        # connect to MySQL
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        # execute command
        cursor.execute("SELECT * FROM books")
        booksData = cursor.fetchall()
        cursor.execute("SELECT * FROM quotations")
        quoteData = cursor.fetchall()

        # close cursor and connection
        self.close(cursor, conn)

        # print booksData, quoteData
        for record in quoteData:
            print(record)

        return booksData, quoteData

    def updateGOF(self):
        # connect to MySQL server
        conn, cursor = self.connect()

        self.useGuiDB(cursor)

        # execute command
        cursor.execute("SELECT Book_ID FROM books WHERE Book_Title='Design Patterns'")
        primkey = cursor.fetchall()[0][0]
        print("Primary Key=" + str(primkey))

        cursor.execute("SELECT * FROM quotations WHERE Books_Book_ID=({})".format((primkey,)))
        print(cursor.fetchall())

        # close cursor and connection
        self.close(cursor, conn)

    def updateGOF_commit(self):
        pass

