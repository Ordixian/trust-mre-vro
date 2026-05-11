# Updated cleaner import style
from app.api import verify_router, payments_router
from app.core import settings

# Then in your router inclusion:
app.include_router(verify_router, prefix="/api/v1/verify")
app.include_router(payments_router, prefix="/api/v1/payments")