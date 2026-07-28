# Portafolio QA — Testing Manual en SauceDemo (saucedemo.com)

**Proyecto:** Test Plan, diseño y ejecución de casos de prueba, y exploratory testing sobre saucedemo.com
**Herramientas:** Documentación manual (Markdown), sin herramientas de gestión de bugs externas en esta primera versión
**Ambiente:** Google Chrome, saucedemo.com

---

## 1. Test Plan

### Objetivo
Validar las funcionalidades principales del sitio SauceDemo (login, catálogo de productos, carrito de compras y checkout) para identificar defectos y verificar que el sistema se comporte según lo esperado.

### Alcance
**Dentro del alcance:** Login, catálogo de productos, carrito de compras, checkout, menú lateral.
**Fuera de alcance:** Testing de performance con herramientas de carga, testing de seguridad, compatibilidad móvil.

### Estrategia de testing
- Testing funcional (caja negra) con usuario `standard_user`
- Exploratory testing con usuario `problem_user`

### Criterios de entrada
El sitio saucedemo.com debe estar accesible y se cuenta con los usuarios de prueba documentados por Sauce Labs.

### Criterios de salida
100% de los casos de prueba diseñados fueron ejecutados y todos los bugs encontrados están documentados.

### Ambiente de pruebas
Navegador: Google Chrome (última versión estable) | URL: https://www.saucedemo.com/

### Usuarios de prueba utilizados
| Usuario | Contraseña | Uso en este proyecto |
|---|---|---|
| standard_user | secret_sauce | Ejecución de los 12 test cases funcionales |
| problem_user | secret_sauce | Exploratory testing — hallazgo de bugs |

---

## 2. Test Cases y Resultados de Ejecución

Todos los casos fueron ejecutados con `standard_user`. Resultado: **12/12 Pass** ✅

| ID | Título | Prioridad | Resultado |
|---|---|---|---|
| TC-001 | Login exitoso con usuario válido | Alta | ✅ Pass |
| TC-002 | Descripción del producto válido | Media | ✅ Pass |
| TC-003 | Agregado al carrito exitoso | Alta | ✅ Pass |
| TC-004 | Botón de remove funciona correctamente | Alta | ✅ Pass |
| TC-005 | Botón de carrito (esquina superior derecha) funciona correctamente | Alta | ✅ Pass |
| TC-006 | Botón de checkout funciona correctamente | Alta | ✅ Pass |
| TC-007 | Botón continue después del checkout funciona correctamente | Alta | ✅ Pass |
| TC-008 | Botón finish funciona correctamente | Alta | ✅ Pass |
| TC-009 | Botón de generar PDF funciona correctamente | Media | ✅ Pass |
| TC-010 | Botón de ordenamiento funciona correctamente A-Z | Baja | ✅ Pass |
| TC-011 | Botón de ordenamiento funciona correctamente Z-A | Baja | ✅ Pass |
| TC-012 | Botón de ordenamiento por precio funciona correctamente (Low-High) | Baja | ✅ Pass |

*(Detalle completo de cada test case — precondiciones, datos de prueba, pasos — disponible en el documento `test-plan-saucedemo.md` de la fase de diseño.)*

---

## 3. Bug Reports — Exploratory Testing con `problem_user`

### BUG-001
| Campo | Detalle |
|---|---|
| Título | Las imágenes de los productos muestran una foto de un perro en vez del producto real |
| Pasos para reproducir | 1. Loguearse con `problem_user` 2. Ir al catálogo de productos |
| Resultado esperado | Cada producto muestra su imagen real correspondiente (mochila, campera, remera, etc.) |
| Resultado actual | Todos los productos muestran la misma imagen de un perro mordiendo una pelota |
| Severidad | Media |
| Prioridad | Alta |
| Entorno | Chrome, usuario problem_user |
| Evidencia | *(agregar captura de pantalla)* |

### BUG-002
| Campo | Detalle |
|---|---|
| Título | Al hacer clic en "Sauce Labs Fleece Jacket" se muestra una página de error no relacionada |
| Pasos para reproducir | 1. Loguearse con `problem_user` 2. Clic en el producto "Sauce Labs Fleece Jacket" |
| Resultado esperado | Se muestra la página de detalle del producto con nombre, imagen, descripción y precio |
| Resultado actual | Se muestra una página "ITEM NOT FOUND" con un mensaje de grabación telefónica no relacionado al producto, y el precio aparece como "$√-1" |
| Severidad | Alta |
| Prioridad | Alta |
| Entorno | Chrome, usuario problem_user |
| Evidencia | *(agregar captura de pantalla)* |

### BUG-003
| Campo | Detalle |
|---|---|
| Título | Los productos "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket" y "Test.allTheThings() T-Shirt (Red)" no se agregan al carrito |
| Pasos para reproducir | 1. Loguearse con `problem_user` 2. Clic en "Add to cart" en cada uno de esos 3 productos desde el catálogo |
| Resultado esperado | Cada producto se agrega al carrito y el contador aumenta |
| Resultado actual | El botón no agrega el producto; el contador del carrito no aumenta para esos 3 productos específicos |
| Severidad | Alta |
| Prioridad | Alta |
| Entorno | Chrome, usuario problem_user |
| Evidencia | *(agregar captura de pantalla)* |

### BUG-004
| Campo | Detalle |
|---|---|
| Título | El botón "Remove" no funciona desde la pantalla principal del catálogo |
| Pasos para reproducir | 1. Loguearse con `problem_user` 2. Agregar un producto al carrito 3. Clic en "Remove" desde la pantalla principal (sin entrar al carrito) |
| Resultado esperado | El producto se quita del carrito y el botón vuelve a "Add to cart" |
| Resultado actual | El botón "Remove" no responde en la pantalla principal; la remoción solo funciona entrando directamente a la pantalla del carrito |
| Severidad | Alta |
| Prioridad | Alta |
| Entorno | Chrome, usuario problem_user |
| Evidencia | *(agregar captura de pantalla)* |

### BUG-005
| Campo | Detalle |
|---|---|
| Título | Los precios mostrados en el catálogo no coinciden con el precio real del producto |
| Pasos para reproducir | 1. Loguearse con `problem_user` 2. Observar los precios listados en la pantalla principal de productos |
| Resultado esperado | Los precios mostrados en el catálogo coinciden con el precio real de cada producto |
| Resultado actual | Los precios visualizados en el catálogo no corresponden al precio real |
| Severidad | Media |
| Prioridad | Alta |
| Entorno | Chrome, usuario problem_user |
| Evidencia | *(agregar captura de pantalla)* |

### BUG-006
| Campo | Detalle |
|---|---|
| Título | El detalle del producto "Test.allTheThings() T-Shirt (Red)" muestra la información de "Sauce Labs Backpack" |
| Pasos para reproducir | 1. Loguearse con `problem_user` 2. Clic en el producto "Test.allTheThings() T-Shirt (Red)" |
| Resultado esperado | Se muestra el nombre, descripción y precio correspondientes a "Test.allTheThings() T-Shirt (Red)" |
| Resultado actual | Se muestra el nombre, descripción y precio ($29.99) de "Sauce Labs Backpack" |
| Severidad | Media |
| Prioridad | Alta |
| Entorno | Chrome, usuario problem_user |
| Evidencia | *(agregar captura de pantalla)* |

### BUG-007
| Campo | Detalle |
|---|---|
| Título | El botón "Add to cart" no responde en la página de detalle de "Sauce Labs Bolt T-Shirt" |
| Pasos para reproducir | 1. Loguearse con `problem_user` 2. Clic en el producto "Sauce Labs Bolt T-Shirt" 3. Clic en "Add to cart" desde la página de detalle |
| Resultado esperado | El producto se agrega al carrito |
| Resultado actual | El botón no responde, el producto no se agrega al carrito |
| Severidad | Alta |
| Prioridad | Alta |
| Entorno | Chrome, usuario problem_user |
| Evidencia | *(agregar captura de pantalla)* |

### BUG-008
| Campo | Detalle |
|---|---|
| Título | El checkout borra el campo "First Name" al completar el campo "Last Name" |
| Pasos para reproducir | 1. Loguearse con `problem_user` 2. Agregar "Sauce Labs Onesie" al carrito 3. Ir a checkout 4. Completar el campo "First Name" 5. Completar el campo "Last Name" |
| Resultado esperado | Ambos campos mantienen su contenido y permiten continuar con el checkout |
| Resultado actual | Al escribir en "Last Name", el contenido del campo "First Name" se borra, impidiendo completar el formulario correctamente |
| Severidad | Alta |
| Prioridad | Alta |
| Entorno | Chrome, usuario problem_user |
| Evidencia | *(agregar captura de pantalla)* |

---

## 4. Resumen ejecutivo

- **12/12** test cases funcionales ejecutados con `standard_user`: todos pasaron (comportamiento esperado, ya que es el usuario diseñado sin fallas).
- **8 bugs** encontrados y documentados mediante exploratory testing con `problem_user`.
- Distribución de severidad: **5 Alta**, **3 Media**.
- Todos los bugs afectan directamente la experiencia de compra (catálogo, carrito o checkout), lo que los convierte en hallazgos relevantes desde la perspectiva del negocio.


