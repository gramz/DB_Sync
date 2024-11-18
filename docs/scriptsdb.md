Tabla para usuarios: Alumnos y Profesores
<br>
<br>
<code>CREATE TABLE Usuarios (
    usuario VARCHAR(50) NOT NULL,
    pass VARCHAR(255) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    mail VARCHAR(150) NOT NULL,
    carne VARCHAR(50) NOT NULL,
    PRIMARY KEY (usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4; </code>
<br>
<br>
Tabla de los cursos para cursos a crear
<br>
<code>CREATE TABLE Cursos (
    idcarrera INT NOT NULL,           
    carrera VARCHAR(100) NOT NULL,    
    Asignatura VARCHAR(100) NOT NULL, 
    codigo VARCHAR(50) NOT NULL,      
    PRIMARY KEY (idcarrera, codigo)   
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;</code>

Tabla para asignación de cursos a usuarios
<br>
<code>CREATE TABLE Asignaciones (
    codigo VARCHAR(50) NOT NULL,     
    carne VARCHAR(50) NOT NULL,     
    rol VARCHAR(50) NOT NULL,       
    PRIMARY KEY (codigo)            
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;</code>
<br>
