# Avito Clone API

FastAPI backend with SQLAlchemy and SQLite by default. It includes user and ad creation, ad search, and a payment workflow.

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Set `DATABASE_URL` to use another SQLAlchemy-supported database. Interactive API documentation is available at `/docs`.

## Payment API

- `POST /api/v1/payments` creates a pending payment using the current ad price.
- `GET /api/v1/payments/{payment_id}` reads a payment.
- `GET /api/v1/payments/buyer/{buyer_id}` lists payments for a buyer.
- `PATCH /api/v1/payments/{payment_id}/status` marks a pending payment `succeeded`, `failed`, or `cancelled`.

This is an application payment record and state workflow; connecting a real payment provider requires provider credentials and webhook verification.
