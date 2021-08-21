CREAR TABLA Autores (
    Id INT NO NULO,
    Nombre VARCHAR (70) NOT NULL,
    País VARCHAR (100) NOT NULL,
    LLAVE PRIMARIA (Id)
);

INSERTAR EN Autores
    (Id, nombre, país)
VALORES
    (1, 'JD Salinger', 'Estados Unidos'),
    (2, 'F. Scott. Fitzgerald', 'Estados Unidos'),
    (3, 'Jane Austen', 'Reino Unido'),
    (4, 'Scott Hanselman', 'Estados Unidos'),
    (5, 'Jason N. Gaylord', 'Estados Unidos'),
    (6, 'Pranav Rastogi', 'India'),
    (7, 'Todd Miranda', 'Estados Unidos'),
    (8, 'Christian Wenz', 'Estados Unidos')
;

CREAR TABLA Libros (
    Id INT NO NULO,
    Título VARCHAR (50) NOT NULL,
    LLAVE PRIMARIA (Id)
);

INSERTAR EN Libros
    (Id, título)
VALORES
    (1, 'El pescador entre el centeno'),
    (2, 'Nueve historias'),
    (3, 'Franny y Zooey'),
    (4, 'El gran Gatsby'),
    (5, 'Tender id the Night'),
    (6, 'Orgullo y prejuicio'),
    (7, 'ASP.NET 4.5 profesional en C # y VB')
;

CREAR TABLA BooksAuthors (
    AuthorId INT NO NULO,
    BookId INT NO NULO,
    FOREIGN KEY (AuthorId) REFERENCIAS Autores (Id),
    FOREIGN KEY (BookId) REFERENCIAS Libros (Id)
);

INSERTAR EN BooksAuthors
    (BookId, AuthorId)
VALORES
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 2),
    (5, 2),
    (6, 3),
    (7, 4),
    (7, 5),
    (7, 6),
    (7, 7),
    (7, 8)
;