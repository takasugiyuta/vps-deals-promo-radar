# auth.md

## Authentication status

status: under_construction
available: false
capabilities_status: planned_contract_only

Authentication, account creation, and token issuance are not available. The public article lookup remains usable without signing in.

## Agent Registration

Registration endpoint: `https://lumafare.com/agent-auth/register`
register_uri: `https://lumafare.com/agent-auth/register`
registration_status: under_construction
registration_available: false

The planned anonymous registration method is described by these fields:

```json
{
  "register_uri": "https://lumafare.com/agent-auth/register",
  "claim_uri": "https://lumafare.com/agent-auth/claim",
  "identity_types_supported": ["anonymous"],
  "anonymous": {
    "credential_types_supported": ["access_token"],
    "claim_uri": "https://lumafare.com/agent-auth/claim"
  }
}
```

Anonymous agent registration is a future design only. While `available` is `false`, do not call the registration or claim endpoint or attempt to create an identity. The reserved endpoints currently return HTTP 503 and do not store submitted data, create accounts, issue credentials, or start an authorization flow. No login or token exchange is active.

## Available public service

The read-only article lookup works without authentication. See the [API contract](/openapi.json), [agent instructions](/ai/), and [public article search and read endpoint](/api/agent/articles).
