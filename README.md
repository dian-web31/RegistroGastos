# 🌍💸 Control de Gastos de Viaje

Una aplicación práctica y ligera que te ayuda a **registrar y visualizar tus gastos diarios** mientras estás de viaje, ya sea **dentro de Colombia** o en el **exterior**. Convierte automáticamente los valores desde otras monedas a **pesos colombianos (COP)** utilizando una [API]( https://github.com/fawazahmed0/exchange-api) libre para las divisas.

---

## ✨ Características principales

✅ Crea viajes con presupuesto diario  
✅ Registra gastos en **efectivo o tarjeta**  
✅ Clasifica gastos por tipo: transporte, alojamiento, alimentación, entretenimiento y compras  
✅ Conversión automática a pesos COP si estás en el exterior  
✅ Reportes al finalizar cada viaje sobre los gastos diarios y por tipo de gasto  
✅ No permite registrar más gastos una vez termina el viaje

---

## 🧳 ¿Cómo funciona?

1. **Inicia un nuevo viaje**
   - Indica si es nacional o internacional
   - Ingresa fechas de inicio y fin
   - Define un presupuesto diario

2. **Registra tus gastos**
   - Fecha del gasto
   - Valor (en la moneda local si estás en el exterior)
   - Medio de pago (efectivo o tarjeta)
   - Tipo de gasto (alimentación, transporte, etc.)

3. **Visualiza reportes**
   - Gasto por día, total y separado por medio de pago
   - Gasto por tipo, total y separado por medio de pago

---

## 🌐 Conversión de moneda

Si viajas al exterior, la app consulta automáticamente la tasa de cambio mediante la siguiente API gratuita:

> [https://github.com/fawazahmed0/exchange-api](https://github.com/fawazahmed0/exchange-api)

---

## 🧭 Requisitos

- Python 3.9 o superior
- Conexión a internet para la conversión de divisas

---

## ⚙️ Cómo ejecutar la aplicación

```bash
git clone https://github.com/tuusuario/control-gastos-viaje.git
cd control-gastos-viaje
python main.py
