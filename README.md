# Repositorio de Proyecto Final de Camada 23855 de Python

Integrantes:
    - Maximiliano Bracho | DNI 34.433.679

# HumanBuddy
HumanBuddy es una plataforma y red social de todos aquellos amantes de los animales.
En HummanBuddy consideramos como familia a nuestras mascotas, y las cuidamos en consecuencia.

HummanBuddy cuenta con las siguientes funcionalidades de negocio:
-Cadena de Veterinarias: HummanBuddy habilita la gestión de una o más veterinarias, conjuntamente con los veterinarios asignados a cada una y los distintos empleados administrativos.
-Gestión de Mascotas: HummanBuddy habilita al público general a registrarse y dar de alta sus mascotas, pudiendo llevar el histórico de atenciones de las mismas.
-Registro de Atenciones: HummanBuddy permite a los veterinarios atender a sus mascotas asignadas.
-Mensajería: HummanBuddy permite a los veterinarios y los padres humanos conversar a través de mensajería iniciada por el veterinario.

Técnicamente HummanBuddy cuenta con:
-Superusuario para dar de alta grupos de usuarios, y usuarios.  y veterinarias (se les debe asignar un usuario creado)
-Registro de usuarios: se le asigna grupos User y Daddy automáticamente: se permite la autocreación de usuarios
-Como Administrator se accede al Portal de Admin de Plataforma y Portal de Permisos
-Como Daddy se accede al Portal de Padres, donde se puede:
    - CRUD de Mascotas
    - Ver atenciones de Mascotas
    - Ver Mensajes: los mensajes listados pueden ser respondidos
    - Editar Perfil de Daddy
-Como Vet se accede al Portal de Veterinaria, donde se puede:
    - CRUD de Sucursales Veterinarias
    - CRUD de Veterinario (con asignación de usuario creado previamente)
    - CRUD de Empleado (con asignación de usuario creado previamente)
    - Como Veterinarian se accede al Portal de Atenciones, donde se puede:
    - Listar mascotas asignadas a la veterinaria
    - Atender mascotas
    - Contactar Daddy de mascota
    - Ver Mensajes: los mensajes listados pueden ser respondidos
- Como Employee no se puede hacer nada: esto es apropósito para mostrar el menú contextual y porque sería desarrollo futuro.

Demo:

- Administrator: mbracho || riQm1907
- Veteriniaria: Vet || riQm1907
- Daddy: daddy || riQm1907
- Veterinario: veterinario1 || riQm1907
