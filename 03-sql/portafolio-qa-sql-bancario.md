Portafolio QA — SQL para Testing (Escenario Bancario)

Proyecto: Diseño de queries SQL orientadas a testing de datos en un sistema bancario (cuentas, clientes, transacciones) Motor objetivo: PostgreSQL (estándar también aplicable a Oracle/MySQL) Contexto: Ejercicio de diseño — simula validaciones típicas que un QA realizaría contra una base de datos real para verificar consistencia de información

Esquema de datos utilizado
clientes (id, nombre, email, fecha_registro)
cuentas (numero_cuenta, cliente_id, saldo, estado)
transacciones (id, cuenta_origen, cuenta_destino, monto, fecha, estado)

Relaciones:

cuentas.cliente_id → clientes.id
transacciones.cuenta_origen / transacciones.cuenta_destino → cuentas.numero_cuenta
Bloque 1 — Validaciones básicas de datos
1. Cuentas con saldo negativo (bug crítico)
sql
SELECT numero_cuenta, saldo
FROM cuentas
WHERE saldo < 0;

Propósito QA: un saldo negativo nunca debería existir en un sistema bancario bien diseñado. Esta query detecta ese caso de forma directa — cualquier resultado devuelto es un bug de severidad alta.

2. Clientes registrados en un rango de fechas
sql
SELECT nombre, email, fecha_registro
FROM clientes
WHERE fecha_registro BETWEEN '2026-01-01' AND '2026-01-31';

Propósito QA: verificar que la cantidad de registros de un período coincida con lo que muestra un reporte o dashboard interno.

3. Historial de transacciones de una cuenta específica
sql
SELECT id, cuenta_origen, monto, fecha, estado
FROM transacciones
WHERE cuenta_origen = 32
ORDER BY fecha ASC;

Propósito QA: revisar el historial completo de movimientos de una cuenta puntual — típico ante un reclamo de cliente ("no reconozco este movimiento").

4. Emails duplicados en clientes
sql
SELECT email, COUNT(*) as cantidad
FROM clientes
GROUP BY email
HAVING COUNT(*) > 1;

Propósito QA: detectar un bug de integridad de datos — un email no debería poder repetirse entre distintos clientes.

5. Transacciones rechazadas junto al saldo actual de la cuenta
sql
SELECT t.id, t.estado, c.numero_cuenta, c.saldo
FROM transacciones t
JOIN cuentas c ON t.cuenta_origen = c.numero_cuenta
WHERE t.estado = 'rechazada';

Propósito QA: obtener los datos necesarios para auditar manualmente si una transacción rechazada afectó el saldo de la cuenta (algo que no debería pasar nunca).

6. Saldo total consolidado por cliente
sql
SELECT cl.nombre, SUM(c.saldo) as saldo_total
FROM clientes cl
JOIN cuentas c ON cl.id = c.cliente_id
GROUP BY cl.nombre;

Propósito QA: verificar el saldo consolidado de un cliente con múltiples cuentas (ahorro, corriente, etc.).

7. Cantidad de transacciones por estado
sql
SELECT estado, COUNT(*) as cantidad_transacciones
FROM transacciones
GROUP BY estado;

Propósito QA: contrastar contra lo que muestra un dashboard de monitoreo — la cantidad de aprobadas/rechazadas/pendientes debe coincidir.

8. Transacciones de monto alto en un rango corto de fechas
sql
SELECT id, cuenta_origen, monto, fecha
FROM transacciones
WHERE monto > 50000000
AND fecha BETWEEN '2026-08-01' AND '2026-08-07';

Propósito QA: validar que sistemas antifraude detecten correctamente montos elevados en ventanas de tiempo cortas.

Bloque 2 — JOIN combinados con agregaciones (nivel avanzado)
9. Cuentas por cliente
sql
SELECT cl.nombre, cta.numero_cuenta, cta.saldo
FROM clientes cl
JOIN cuentas cta ON cl.id = cta.cliente_id;

Propósito QA: listar cada cuenta individual asociada a cada cliente.

10. Clientes con cuentas suspendidas
sql
SELECT cl.nombre, cl.email, cta.estado
FROM clientes cl
JOIN cuentas cta ON cl.id = cta.cliente_id
WHERE cta.estado = 'suspendida';

Propósito QA: validar reclamos de clientes sobre el estado de su cuenta.

11. Transacciones rechazadas por cliente (3 tablas unidas)
sql
SELECT cl.nombre, t.monto, t.fecha
FROM clientes cl
JOIN cuentas cta ON cl.id = cta.cliente_id
JOIN transacciones t ON t.cuenta_origen = cta.numero_cuenta
WHERE t.estado = 'rechazada';

Propósito QA: trazabilidad completa de transacciones fallidas hasta el cliente afectado.

12. Cantidad de cuentas por cliente
sql
SELECT cl.nombre, COUNT(cta.numero_cuenta) as cantidad_cuentas
FROM clientes cl
JOIN cuentas cta ON cl.id = cta.cliente_id
GROUP BY cl.nombre;

Propósito QA: reporte de control interno sobre cantidad de productos (cuentas) por cliente.

13. Clientes con más de 3 transacciones rechazadas (detección de casos sospechosos)
sql
SELECT cl.nombre, COUNT(t.id) as transacciones_rechazadas
FROM clientes cl
JOIN cuentas cta ON cl.id = cta.cliente_id
JOIN transacciones t ON t.cuenta_origen = cta.numero_cuenta
WHERE t.estado = 'rechazada'
GROUP BY cl.nombre
HAVING COUNT(t.id) > 3;

Propósito QA: apoyo a testing de reglas de negocio antifraude — validar que el sistema marque correctamente a clientes con patrones de rechazo repetidos.

14. Top 5 transacciones de mayor monto de un cliente
sql
SELECT cl.nombre, t.monto, t.fecha
FROM clientes cl
JOIN cuentas cta ON cl.id = cta.cliente_id
JOIN transacciones t ON t.cuenta_origen = cta.numero_cuenta
WHERE cl.nombre = 'Juan Pérez'
ORDER BY t.monto DESC
LIMIT 5;

Propósito QA: verificación puntual de los movimientos de mayor impacto de un cliente específico.

15. Clientes registrados sin ninguna cuenta abierta (LEFT JOIN)
sql
SELECT cl.nombre, cl.email
FROM clientes cl
LEFT JOIN cuentas cta ON cl.id = cta.cliente_id
WHERE cta.numero_cuenta IS NULL;

Propósito QA: detectar registros "incompletos" que un INNER JOIN normal excluiría silenciosamente — útil para procesos de seguimiento comercial o para encontrar fallas en el flujo de alta de cuenta.

16. Clientes de "alto valor" por promedio de transacción
sql
SELECT cl.nombre, AVG(t.monto) as promedio_transacciones
FROM clientes cl
JOIN cuentas cta ON cl.id = cta.cliente_id
JOIN transacciones t ON t.cuenta_origen = cta.numero_cuenta
GROUP BY cl.nombre
HAVING AVG(t.monto) > 5000000;

Propósito QA: validar segmentaciones de clientes basadas en promedios de transacción, comunes en reportes de banca.

17. Actividad sospechosa: clientes nuevos con monto transaccionado alto
sql
SELECT cl.nombre, SUM(t.monto) as monto_total
FROM clientes cl
JOIN cuentas cta ON cl.id = cta.cliente_id
JOIN transacciones t ON t.cuenta_origen = cta.numero_cuenta
WHERE cl.fecha_registro >= '2026-08-05'
GROUP BY cl.nombre
HAVING SUM(t.monto) > 1000000;

Propósito QA: query típica de soporte a testing de reglas antifraude — cliente recién registrado con actividad transaccional alta amerita revisión.
