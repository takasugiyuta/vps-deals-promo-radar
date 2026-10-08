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
identity_types_supported: anonymous
anonymous_registration: planned only; not available

Anonymous agent registration is a future design only. While `available` is `false`, do not call the registration endpoint or attempt to create an identity. The reserved endpoint currently returns HTTP 503 and does not store submitted data, create accounts, issue credentials, or start an authorization flow. No login or token exchange is active.

## Available public service

The read-only article lookup works without authentication. See the [API contract](/openapi.json), [agent instructions](/ai/), and [public article search and read endpoint](/api/agent/articles).
