Portafolio QA — API Testing con Postman

Proyecto: Colección de pruebas de API (positivas y negativas) sobre reqres.in, una API pública de práctica Herramienta: Postman Entregable adjunto: coleccion-api-testing.postman_collection.json (colección exportada, importable en Postman)

Resumen de casos de prueba
#	Nombre	Método	Endpoint	Resultado esperado	Resultado obtenido	Estado
1	Obtener usuario existente	GET	/api/users/2	200	200	✅ Pass
2	Usuario inexistente	GET	/api/users/999	404	404	✅ Pass
3	Listar usuarios (paginado)	GET	/api/users?page=2	200	200	✅ Pass
4	Crear usuario válido	POST	/api/users	201	201	✅ Pass
5	Crear usuario con body vacío	POST	/api/users	A confirmar	400 Bad Request	⚠️ Ver nota
6	Actualizar usuario	PUT	/api/users/2	200	200	✅ Pass
7	Eliminar usuario	DELETE	/api/users/2	204	204	✅ Pass
8	Login exitoso	POST	/api/login	200 + token	200 + token	✅ Pass
9	Login fallido (sin password)	POST	/api/login	400	400	✅ Pass

9/9 casos ejecutados — comportamiento validado en los 9.

Nota sobre el caso #5 (body vacío)

Antes de ejecutar esta prueba, la hipótesis era que reqres.in, al ser una API de práctica, no validaría el body vacío y devolvería igualmente un 201 Created como si hubiese creado el usuario.

El resultado real fue 400 Bad Request, contradiciendo esa hipótesis inicial — la API sí rechaza la creación de un usuario sin datos.

Aprendizaje documentado: este caso confirma la importancia de ejecutar la prueba en vez de asumir el comportamiento del sistema, incluso cuando se tiene una expectativa razonable basada en la naturaleza del sistema (API de práctica vs. sistema productivo). En un contexto de testing real, ninguna suposición reemplaza la verificación empírica.

Detalle del caso #9 — Login fallido (sin password)

Request:

json
POST https://reqres.in/api/login
{
  "email": "eve.holt@reqres.in"
}

Respuesta obtenida:

Status: 400 Bad Request
Body:
json
{
    "error": "Missing password"
}



Assertions (tests automatizados) utilizados

Cada request de la colección incluye al menos una validación automática de status code, por ejemplo:

javascript
pm.test("Status code correcto", function () {
    pm.response.to.have.status(200);
});

Para las requests de listado (GET paginado), se agregó además una validación de estructura de respuesta:

javascript
pm.test("La respuesta contiene datos", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.data).to.be.an('array');
});
