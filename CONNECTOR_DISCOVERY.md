# Elastic Observability Connector — Connector Discovery

**Vendor API Baseline:** https://elastic.co

## Архитектура API
- **Базовый адрес:** `https://<deployment>.kb.<region>.aws.elastic-cloud.com/api`
- **Протокол:** REST / HTTPS (JSON)
- **Аутентификация:** Kibana/Elasticsearch API Key (Authorization: ApiKey <token>)
- **Ключевые эндпоинты:**
  - индексы логов (/status)
  - правила алертов (/alerting/rules)
  - дашборды Kibana (/saved_objects)
  - APM-транзакции
- **Тестовая точка проверки подключения:** `GET /api/status`.
