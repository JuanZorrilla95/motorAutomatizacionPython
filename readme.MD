Producto: motor que basicamente toma un invoice, evalua reglas y decide que hacer con ese invoice

Negocio:
Rules = definición

RuleRun = auditoría

Invoice = estado del negocio

1. Crear invoice. POST /invoices


2. Crear reglas de negocio. POST /rules/config


3 .Ejecutar reglas sobre una invoice. POST /rules/run/{invoice_id}

El proyecto tiene:
- Arquitectura extensible
- Principios SOLID
- Separación de responsabilidades
