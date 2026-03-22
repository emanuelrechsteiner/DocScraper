"""Auth router — API key CRUD endpoints (#21)."""

import uuid

from fastapi import APIRouter, HTTPException

from ..models.schemas import (
    APIKeyCreateRequest,
    APIKeyListResponse,
    APIKeyResponse,
    APIResponse,
    MetaResponse,
    UserCreateRequest,
    UserResponse,
)
from ..services.auth_service import auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=APIResponse, status_code=201)
async def register_user(request: UserCreateRequest) -> APIResponse:
    """Register a new user account.

    Args:
        request: Email and optional display name.

    Returns:
        APIResponse wrapping UserResponse with the new user ID.

    Raises:
        HTTPException: 409 if email already registered.
    """
    try:
        user = auth_service.create_user(email=request.email, name=request.name)
    except ValueError as exc:
        raise HTTPException(
            status_code=409,
            detail={"code": "EMAIL_EXISTS", "message": str(exc)},
        ) from exc

    return APIResponse(
        data=UserResponse(
            user_id=user.user_id,
            email=user.email,
            name=user.name,
            tier=user.tier,
            created_at=user.created_at,
        ).model_dump(mode="json"),
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )


@router.post("/keys", response_model=APIResponse, status_code=201)
async def create_api_key(
    request: APIKeyCreateRequest, user_id: str = "user_default"
) -> APIResponse:
    """Create a new API key for a user (#21).

    The full key is returned ONLY in this response. It cannot be
    retrieved again — store it securely.

    Args:
        request: Key name/label.
        user_id: Owner user ID (will come from auth context in production).

    Returns:
        APIResponse wrapping APIKeyResponse with the full key.

    Raises:
        HTTPException: 404 if user not found.
    """
    try:
        key_data, raw_key = auth_service.create_api_key(
            user_id=user_id, name=request.name
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail={"code": "USER_NOT_FOUND", "message": str(exc)},
        ) from exc

    return APIResponse(
        data=APIKeyResponse(
            key_id=key_data.key_id,
            name=key_data.name,
            prefix=key_data.prefix,
            key=raw_key,
            created_at=key_data.created_at,
            is_active=key_data.is_active,
        ).model_dump(mode="json"),
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )


@router.get("/keys", response_model=APIResponse)
async def list_api_keys(user_id: str = "user_default") -> APIResponse:
    """List all API keys for a user (#21).

    Full keys are never returned — only prefix and metadata.

    Args:
        user_id: Owner user ID.

    Returns:
        APIResponse wrapping APIKeyListResponse.
    """
    keys = auth_service.list_api_keys(user_id)

    key_list = [
        APIKeyResponse(
            key_id=k.key_id,
            name=k.name,
            prefix=k.prefix,
            key=None,
            created_at=k.created_at,
            is_active=k.is_active,
        )
        for k in keys
    ]

    return APIResponse(
        data=APIKeyListResponse(
            keys=key_list, total=len(key_list)
        ).model_dump(mode="json"),
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )


@router.delete("/keys/{key_id}", response_model=APIResponse)
async def revoke_api_key(
    key_id: str, user_id: str = "user_default"
) -> APIResponse:
    """Revoke an API key (#21).

    Args:
        key_id: The key to revoke.
        user_id: Must match the key owner.

    Returns:
        APIResponse confirming revocation.

    Raises:
        HTTPException: 404 if key not found or unauthorized.
    """
    success = auth_service.revoke_api_key(key_id=key_id, user_id=user_id)
    if not success:
        raise HTTPException(
            status_code=404,
            detail={
                "code": "KEY_NOT_FOUND",
                "message": f"Key {key_id} not found or not owned by user",
            },
        )

    return APIResponse(
        data={"key_id": key_id, "status": "revoked"},
        meta=MetaResponse(request_id=f"req_{uuid.uuid4().hex[:12]}"),
    )
