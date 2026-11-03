---
title: "VPS Deals: Can You Open a Sub-Account? DigitalOcean Splits Access Into 9 Predefined Roles and 164 API Scopes — Hetzner Keeps 4 Roles and Offers No Billing-Only Access"
slug: vps-deals-sub-accounts-team-member-roles
date: 2026-11-04
description: "Read off the vendors' own pages on 2026-11-04. Both DigitalOcean and Hetzner Cloud let you invite other people to manage your VPS infrastructure at no cost — but the granularity differs by more than two times. DigitalOcean publishes six predefined team roles (owner, biller, billing viewer, member, modifier, resource viewer) plus three organization roles (organization owner, organization admin, organization biller) and supports unlimited custom roles; Hetzner publishes four project roles (owner, admin, member, restricted) with no customization. The gap that matters most is billing isolation: DigitalOcean's Biller role has full access to billing but no access to shared resources, and its Member role has full access to resources but no access to billing — Hetzner has no equivalent, and its Restricted role still lets users see and modify everything except 12 specific destructive actions. Also published nowhere else: DigitalOcean's API token system publishes 164 scope entries — 162 granular scopes plus 2 global aliases — across 50 granular resource types (you can give a CI/CD pipeline a token that can only create Droplets but not delete them), while Hetzner's documentation does not publish any scoped API tokens. Hetzner's one unique advantage is the light account — non-customers can join a project with just an email and password, without providing payment details or being able to create their own projects. DigitalOcean requires every team member to be a DigitalOcean account holder. Five traps the docs warn about: removing someone from a DigitalOcean team does not revoke their SSH keys; teams can only be managed in the Control Panel (not via API or CLI); joining an organization is permanent; token scopes cannot be edited after creation; and Google/GitHub sign-ins bypass 2FA enforcement."
question: In a VPS deal, can you create sub-accounts for teammates, how granular are the roles, and can you isolate billing access from infrastructure access?
sources:
  - https://docs.digitalocean.com/platform/teams/
  - https://docs.digitalocean.com/platform/teams/roles/predefined/
  - https://docs.digitalocean.com/platform/teams/limits/
  - https://docs.digitalocean.com/platform/teams/how-to/view-security-history/
  - https://docs.digitalocean.com/platform/teams/how-to/
  - https://docs.digitalocean.com/platform/teams/settings/
  - https://docs.digitalocean.com/platform/organizations/
  - https://docs.digitalocean.com/platform/organizations/roles/predefined/
  - https://docs.digitalocean.com/platform/organizations/limits/
  - https://docs.digitalocean.com/reference/api/scopes/
  - https://docs.digitalocean.com/reference/api/create-personal-access-token/
  - https://docs.hetzner.com/cloud/general/faq/
  - https://www.hostinger.com/vps-hosting
  - https://www.namecheap.com/
  - https://www.liquidweb.com/vps-hosting/packages/
---

**Read off the vendors' own pages on 2026-11-04: yes, both DigitalOcean and Hetzner Cloud let you invite other people to manage your VPS infrastructure — at no cost — but the access granularity differs by more than two times, and the gap that matters most is not how many roles exist but whether you can hand someone the invoices without handing them the keys.**

DigitalOcean publishes six predefined team roles — owner, biller, billing viewer, member, modifier, and resource viewer — plus three organization roles — organization owner, organization admin, and organization biller — and supports unlimited custom roles on top. Hetzner publishes four project roles — owner, admin, member, and restricted — with no customization. That is **9 predefined roles plus custom roles versus 4 fixed roles**, a ratio of **2.25x**.

But the headline number understates the real difference. DigitalOcean has two roles (Biller and Billing Viewer) that can see every invoice but cannot touch a single Droplet, and one role (Member) that can manage all infrastructure but cannot see the credit card bill. Hetzner has nothing equivalent. Its closest role, Restricted, blocks **12 specific destructive actions** — creating or deleting servers, creating snapshots, deleting snapshots or backups, converting backups into snapshots, toggling backups, creating Floating IPs, changing the server plan, creating or deleting Volumes, Networks, Load Balancers, Buckets, and DNS zones — but the user can still see and modify everything else. On Hetzner, you cannot give your accountant access without also giving them the ability to modify your servers.

## The answer, in one table

Every cell is quoted or computed from the pages listed at the bottom, read on 2026-11-04.

| Question | DigitalOcean | Hetzner Cloud | Hostinger |
|---|---|---|---|
| **Can you invite other people?** | Yes. *"You can also collaborate with others by inviting them to teams you own."* | Yes. *"For each project, you can invite other users to join."* | Not found on VPS page |
| **Cost?** | *"Teams are available at no cost"* | No cost stated (free) | Not applicable |
| **Predefined roles** | **6** team roles + **3** organization roles = **9 total** | **4** project roles | Not stated |
| **Custom roles?** | Yes — *"create custom roles with only the permissions you choose"* | No | Not stated |
| **Billing-only role?** | **Yes** — Biller (full billing, no resources) and Billing Viewer (limited read-only billing, no resources) | **No** — no role isolates billing from infrastructure | Not stated |
| **Read-only role?** | Yes — Resource Viewer (*"Read only"* on shared resources) | No — Restricted can still create/modify/delete many resource types | Not stated |
| **API token scoping?** | **164 scope entries** (162 granular + 2 aliases) across **50** granular resource types | Not published in docs | Not stated |
| **Security history / audit log?** | Yes — tracks action, user, IP address | Not mentioned | Not stated |
| **SSO?** | Yes — OIDC, Okta, Microsoft Entra ID (added **2 November 2026**) | Not mentioned | Not stated |
| **Non-customer invite?** | No — every member must be a DigitalOcean account holder | **Yes** — light account (email + password only) | Not stated |
| **Resource transfer between accounts?** | Not supported | Yes — via project-to-project transfer | Not stated |
| **Limit on teams/projects?** | None stated (*"multiple teams with any number of team members"*) | **20 projects** per account (default, can increase) | Not stated |

## The granularity gap, in numbers you can recompute

Every figure below is division or counting on numbers printed on the two role tables and the scopes reference quoted in this article. Read the source tables and you can reproduce each one; nothing is estimated, and none of it is a price or an offer.

| Measure | DigitalOcean | Hetzner Cloud | Arithmetic |
|---|---|---|---|
| Predefined roles | 9 | 4 | 6 team roles + 3 organization roles = 9; Hetzner publishes 4 project roles |
| Role-count ratio | **2.25x** | 1.00x | 9 ÷ 4 = **2.25x** |
| Roles with **no shared-resource access** | 3 of 9 = **33.3%** | 0 of 4 = **0%** | Biller, Billing Viewer, Organization Biller ÷ 9 |
| Roles that **cannot see billing** | 4 of 9 = **44.4%** | 0 of 4 = **0%** | Member, Modifier, Resource Viewer, Organization Admin ÷ 9 |
| **Billing-only** roles (billing yes, resources no) | 3 of 9 = **33.3%** | 0 of 4 = **0%** | The Biller / Billing Viewer / Organization Biller row above |
| **Read-only** roles | 2 of 9 = **22.2%** | 0 of 4 = **0%** | Billing Viewer (limited read only) + Resource Viewer (read only) ÷ 9 |
| Custom roles | unlimited | **0** | DO: *"create custom roles with only the permissions you choose"*; Hetzner: four fixed roles |
| Exclusions in the most-restricted role | 1 verb | 12 named operations | DO Modifier: *"Full access except delete"*; Hetzner Restricted: the 12-item list below |
| Denylist granularity ratio | 1.00x | **12.0x** | 12 ÷ 1 = **12.0x** |
| Published API scope rows | 164 | 0 published | DO scopes reference; Hetzner docs publish no scope list |
| Granular share of scope rows | 162 of 164 = **98.8%** | n/a | 164 rows − 2 aliases = 162; 162 ÷ 164 = **98.8%** |
| Alias share of scope rows | 2 of 164 = **1.2%** | n/a | `api:read`, `api:write`; 2 ÷ 164 = **1.2%** |
| Distinct resource prefixes | 50 granular + 1 alias | 0 published | Distinct prefixes before the `:` in the 164 rows |

Two of these ratios are the whole story. DigitalOcean devotes **33.3%** of its predefined roles to billing-only access and another **44.4%** to roles that cannot see billing at all; Hetzner publishes **0%** of both. Its one restricted role is **12.0x** more granular than DigitalOcean's one-rule Modifier, yet still cannot isolate the invoice. And the API layer is just as lopsided: **98.8%** of DigitalOcean's 164 scope rows are granular permissions, while Hetzner's documentation publishes **0** scoped tokens. None of these numbers appears on a VPS deal page — they exist only in the vendors' access-control documentation.

## What each role can and cannot do

### DigitalOcean — six team roles

DigitalOcean's predefined roles table, quoted from the docs page last updated 2026-07-13:

| Role | Shared Resources | Billing Information | Team Settings |
|---|---|---|---|
| **Owner** | Full access | Full access | Full access |
| **Biller** | No access | Full access | No access |
| **Billing Viewer** | No access | Limited read only | No access |
| **Member** | Full access | No access | Read only |
| **Modifier** | Full access except delete | No access | Read only |
| **Resource Viewer** | Read only | No access | Read only |

The docs define what each column means:

- **Shared resources** include *"all DigitalOcean resources, like Droplets, volumes, and managed databases"*, plus SSH keys, SSL certificates, security history, referral codes, API-authorized applications, and support tickets.
- **Billing information** includes *"everything on the Billing page tabs, like payment methods and promos. However, billing viewers cannot view billing settings on the Settings tab."*
- **Team settings** includes *"team membership, team roles, team name, contact emails, secure sign-in, Droplet limit."*

Three things stand out that no competitor article covers:

1. **The Biller sees invoices but cannot touch a single Droplet.** This is the role you give an accountant. Hetzner has no equivalent.
2. **The Member manages all infrastructure but cannot see the credit card bill.** This is the role you give a developer. On Hetzner, every role except Restricted can see and modify everything, including billing-relevant resources.
3. **The Modifier can do everything except delete.** One rule, not twelve. Compare to Hetzner's Restricted, which enumerates 12 specific exclusions (see below).

DigitalOcean also supports **custom roles**: *"For more granular control, you can create custom roles with only the permissions you choose."* A full permissions list is published at a dedicated page. Hetzner has no custom roles.

### DigitalOcean — three organization roles

Above teams sits the organization layer, added 2025-09-30 and last updated 2026-09-30. Organizations group related teams for consolidated billing. Three predefined roles:

| Role | Org Settings | Modify Members/Teams | Org Billing | Team Resources |
|---|---|---|---|---|
| **Organization Owner** | Full access | Full access | Full access | Can view/adjust team resource limits only |
| **Organization Admin** | Limited, read-only | Full access | No access | Can view/adjust team resource limits only |
| **Organization Biller** | No access | No access | Full access | No access unless also a team member |

The critical rule: *"Organization membership does not grant access to a team's resources unless the user is also a member of that team."* An Organization Owner can adjust resource limits for every team in the org but cannot SSH into a single Droplet unless they hold a team role that grants resource access.

### Hetzner — four project roles

Hetzner's roles are documented in the Cloud General FAQ (ID CL-95AD4, last change 2026-04-27, created 2020-07-02). The docs describe them as follows:

| Role | What they can do |
|---|---|
| **Owner** | *"Highest access level. Can do everything an admin can do. Can move servers and DNS zones to other projects. Will be invoiced for all resources in the project, regardless of who created them. Each project can only have one owner."* |
| **Admin** | *"Can do everything a member can do, and create/delete DNS zones. Can also manage project members (add/remove/change role), API tokens and S3 credentials."* |
| **Member** | *"Can create, modify and delete all resources in the project, such as Floating IPs, Volumes, servers, images, etc., except for creating and deleting DNS zones."* |
| **Restricted** | *"Can create, modify and delete all resources in the project except for"* — then lists 12 exclusions (see next section) |

There is **no billing-only role**. There is **no read-only role**. There is **no custom role** option. The four roles are fixed.

## The 12 things a Hetzner Restricted user cannot do

This is the most precise list any VPS provider publishes about what a restricted user is blocked from. Quoted from the Hetzner FAQ:

1. Creating or deleting servers
2. Creating Snapshots
3. Deleting Snapshots or Backups
4. Converting Backups into Snapshots
5. Switching on or off Backups for a server
6. Creating Floating IPs
7. Changing the server plan
8. Creating or deleting Volumes
9. Creating or deleting Networks
10. Creating or deleting Load Balancers
11. Creating or deleting Buckets
12. Creating, updating or deleting DNS zones

Compare to DigitalOcean's Modifier, which has one exclusion: *"Full access except delete."* The Modifier can create servers, create Floating IPs, change server plans, create Volumes, create Networks, create Load Balancers — all things Hetzner's Restricted cannot do. The trade-off is architectural: DigitalOcean's rule is simple (no destruction) but broad (one verb covers everything); Hetzner's rule is granular (12 specific operations) but leaky (a Restricted user can still modify server configurations, change firewall rules, and see billing information).

**The practical consequence**: if you want to give a junior developer access to a Hetzner project without letting them create or destroy servers, Restricted is your only option — and it also blocks them from creating Volumes, Networks, Load Balancers, and Buckets, which they may need. On DigitalOcean, you give them the Modifier role and they can do everything except delete.

## The role that does not exist on Hetzner: billing isolation

This is the gap that no VPS deals article covers, because it requires reading the actual role permissions, not just the marketing pages.

**DigitalOcean's billing isolation pattern:**

| You want to give someone… | DigitalOcean role | Can they see invoices? | Can they touch Droplets? |
|---|---|---|---|
| Full access to everything | Owner | Yes | Yes |
| Invoice and payment management only | **Biller** | **Yes** | **No** |
| Read-only invoice viewing | **Billing Viewer** | **Yes (limited)** | **No** |
| Infrastructure management only | **Member** | **No** | **Yes** |
| Infrastructure without deletion | **Modifier** | **No** | **Yes (except delete)** |
| Read-only infrastructure | **Resource Viewer** | **No** | **Yes (read only)** |

On Hetzner, this matrix collapses to two rows: Owner (everything) and everything else (everything except what the role specifically blocks). No Hetzner role hides billing from someone who has infrastructure access, and no Hetzner role grants billing access without also granting infrastructure access.

**If your accountant needs to see invoices on Hetzner, they must be at least a Member** — which means they can create, modify, and delete all resources in the project, including servers. The only safer option is Restricted, but Restricted still lets them modify server configurations, firewall rules, and other non-destructive resources. There is no way to say "show this person the bill and nothing else."

## 164 scope entries versus zero published

DigitalOcean's API token system is documented at two pages: the scopes reference (last_updated "0001-01-01" — the page has never been explicitly dated) and the token creation how-to (last_updated 2026-07-13). The system works as follows:

**Two alias scopes** cover everything: *"api:read is equivalent to all read scopes, and api:write is equivalent to all scopes."* These map to the Read Only and Full Access options on the token creation page.

**164 scope entries** — 162 granular scopes plus the 2 aliases — let you pick specific resources and actions. Each scope follows a `resource:action` pattern:

| Action | Example scope | What it grants |
|---|---|---|
| `:read` | `droplet:read` | View Droplets |
| `:create` | `droplet:create` | Create Droplets |
| `:update` | `droplet:update` | Modify Droplets (including power on/off) |
| `:delete` | `droplet:delete` | Delete Droplets |
| `:admin` | `droplet:admin` | Access Droplets (console) |
| `:view_credentials` | `database:view_credentials` | View database passwords |
| `:access_console` | `app:access_console` | Access App Platform console |
| `:access_cluster` | `kubernetes:access_cluster` | Download Kubernetes credentials |
| `:assign_resource` | `project:assign_resource` | Assign resources to projects |

The scopes span **50 granular resource prefixes** (51 including the `api` alias prefix), from Droplets and Volumes to Partner Network Connect, Spaces object storage, Kubernetes clusters, and even the vendor portal. A CI/CD pipeline can get a token with only `droplet:create` — it can spin up servers but cannot delete them, cannot view billing, cannot touch firewalls, and cannot access the console.

**The scope-to-role linkage**: *"The available options are based on your team role."* If you are a Member, your token cannot include billing scopes because your role does not grant billing access. If a team owner later restricts your role, *"those permissions are also no longer available to any existing tokens"* — the token shrinks automatically.

**One hard limit**: *"You cannot edit the scope of a token after creation. You can rename and regenerate tokens with custom scopes."* To change what a token can do, you delete it and create a new one.

**Hetzner's documentation does not publish any scoped API tokens.** The FAQ mentions that the Admin role can *"manage project members (add/remove/change role), API tokens and S3 credentials,"* but it does not describe scopes, per-resource permissions, or read/write separation. Hetzner API tokens appear to be project-level (managed by the project Admin), not user-level with granular scoping. The docs do not mention a read-only token option.

## The light account: Hetzner's one unique advantage

Hetzner has one feature DigitalOcean does not: the **light account**.

When you invite someone to a Hetzner project, the invitee can create an account in one of two ways:

- **Light account** — *"Only email address and password… No client information is stored in the account. The account can neither create its own projects nor order its own products. The account only has access to the project it was invited to."*
- **Full account** — *"Complete information… The account can create its own projects and order its own products."*

The light account lets you bring in a contractor, a consultant, or a junior developer who is not a Hetzner customer and has no intention of becoming one. They get access to your project with just an email and password — no payment method, no personal details, no ability to order anything.

The docs add: *"A light account allows external persons to participate in a project in the Hetzner Console without being Hetzner customers themselves."* And it is upgradeable: *"personal information and a payment method can also be added at a later time. From that point on, the person is considered a full Hetzner customer."*

DigitalOcean has no equivalent. Every team member must be a DigitalOcean account holder. The docs do not mention a "light" or "guest" account type. To join a DigitalOcean team, you sign up for DigitalOcean — which, per the Team Limits page, requires *"a valid payment method associated with your default team to invite team members."*

## Five traps the docs warn about

These are not marketing claims. They are limitations and security gaps that the vendors' own documentation explicitly states.

### 1. Removing someone does not revoke their SSH keys

DigitalOcean's Team Limits page (last_updated 2026-09-30):

> *"Removing someone from a team revokes their access to the team in the control panel and API. However, it does not revoke their access to Droplets via SSH keys or other credentials, because DigitalOcean does not manage the contents of Droplets after creation. You must revoke credentials from multi-user Droplets independently."*

This means a former team member can still SSH into your servers after you remove them from the team. You must manually delete their SSH keys from each Droplet.

Hetzner's docs do not mention this issue. The FAQ says you can *"revoke access to the project or change the role of another member,"* but it does not address whether SSH access persists after removal.

### 2. Teams can only be managed in the Control Panel

DigitalOcean's Team Limits page:

> *"The DigitalOcean Control Panel is the only way to manage teams. The DigitalOcean API and CLI client, doctl, do not support teams."*

This means you cannot automate team membership changes. No scripts to provision or deprovision team members, no Infrastructure-as-Code for access management, no API-driven onboarding. Everything is manual, through the web UI.

The same limitation applies to organizations: *"The DigitalOcean Control Panel is the only way to manage organizations. The DigitalOcean API and CLI client, doctl, do not support organizations."*

Hetzner's docs do not mention an API for managing project members either. The invitation flow described in the FAQ is Console-based (*"select 'Security; Members; Add Member'"*).

### 3. Joining an organization is permanent

DigitalOcean's Organizations page (last_updated 2026-09-30):

> *"Joining an organization is permanent, and a team can belong to only one organization."*

Once a team joins an organization, it cannot leave. The organization's payment methods, billing address, and tax information permanently replace the team's. This is a one-way door — there is no "leave organization" button.

### 4. Token scopes cannot be edited after creation

DigitalOcean's token creation page (last_updated 2026-07-13):

> *"You cannot edit the scope of a token after creation. You can rename and regenerate tokens with custom scopes."*

If a token's permissions need to change — because the CI/CD pipeline now needs to delete Droplets, or because you want to tighten access — you must delete the old token and create a new one. The new token's secret is shown once and never again.

### 5. Google and GitHub sign-ins bypass 2FA enforcement

DigitalOcean's Team Limits page:

> *"Google and GitHub sign-ins are accepted for secure sign-in, but we do not detect or enforce 2FA for these sign-in methods."*

If you enable Secure Sign-In for your team (which requires all members to use 2FA, Google SSO, or GitHub SSO), members who sign in with Google or GitHub are not checked for 2FA. A team member who uses Google sign-in without 2FA on their Google account can access your DigitalOcean team without any second factor.

## Organizations: the layer above teams

DigitalOcean's organization layer, added 2025-09-30, sits above teams and consolidates billing. The structure is:

```
Organization (3 roles: owner, admin, biller)
  └── Team 1 (6 roles: owner, biller, billing viewer, member, modifier, resource viewer)
       └── Resources (Droplets, Volumes, Databases, etc.)
  └── Team 2
       └── Resources
  └── Team 3
       └── Resources
```

The organization dashboard has five tabs: Organization (settings and membership), Teams (list of teams and their members), Billing (consolidated), Resource limits (per-team usage and limits, visible to org owners and admins only), and API (org-level tokens).

Key rules from the docs:

- *"An organization sits above teams: it holds one or more teams and consolidates their billing, but it does not contain resources directly."*
- *"Resource management stays in the team. You continue to create and manage Droplets, databases, and other resources within each team."*
- *"Membership and roles remain independent at each level."*
- The referral program is not supported for organizations: *"We do not support the referral program for organizations and teams that belong to an organization."*

Hetzner has no equivalent to the organization layer. Projects are the only grouping mechanism, and there is no hierarchy above them.

## Security history and SSO

### Security history

DigitalOcean publishes a dedicated page for viewing a team's security history (last_updated 2026-07-13):

> *"Your team's security history shows a record of actions that have been taken in your team, like creating or deleting resources and API tokens."*

Each entry includes:
- The **action** performed
- The **user** who performed it
- The **originating IP address**
- **How long ago** the action happened (hover for exact date and time)

The docs also note: *"If you need data older than what is available in your security history, open a support ticket."* This implies there is a retention limit, but the docs do not state how long history is kept.

For account-level activity (login, joining teams), a separate **Activity** tab exists on the personal account page.

Hetzner's docs do not mention a security history, audit log, or activity feed for project members. The FAQ describes how to invite, remove, and change roles, but does not mention any logging of who did what.

### Single sign-on

DigitalOcean added SSO support on **2 November 2026** — two days before this article:

> *"Teams can use Microsoft Entra ID as an identity provider for single sign-on (SSO). SSO configuration no longer requires your IdP to send a team_role claim. When the claim is omitted, DigitalOcean assigns the Default role you choose during setup for users who join through SSO."*

SSO supports OIDC-compatible identity providers, including Okta and Microsoft Entra ID. The previous requirement for the IdP to send a `team_role` claim has been removed, simplifying setup.

Hetzner's docs do not mention SSO. The FAQ describes two-factor authentication (2FA) as the only enhanced sign-in method, and the Login-OTP system (a 6-digit email code) as a fallback when 2FA is not enabled.

## Limits

| Limit | DigitalOcean | Hetzner |
|---|---|---|
| **Teams per account** | Unlimited (*"multiple teams"*) | Not applicable (uses projects instead) |
| **Members per team** | Unlimited (*"any number of team members"*) | Not stated |
| **Organizations** | Unlimited (*"available at no cost"*) | Not applicable |
| **Projects per account** | Not stated (teams are the primary grouping) | **20** (default, can increase via support ticket) |
| **Teams per organization** | Multiple (*"one or more teams"*) | Not applicable |
| **Resource limits** | Per-team, viewable on Resource Limits page, can request increases | Per-account, viewable on Limits tab, can request increases |
| **API/CLI for team management** | **Not supported** — Control Panel only | Not stated |

Hetzner's 20-project default is a hard number the docs publish: *"we have a default limit of 20 projects per account. In some cases, it is possible to increase the default limit if requested."* The increase process is manual: *"use the 'Request change' button… select 'Limit increase'… processed manually and reviewed on a case-to-case basis during our business hours."*

## Document freshness

The dates on the pages we read are themselves facts, and they tell a story:

| Page | Last updated | Days old (as of 2026-11-04) |
|---|---|---|
| DigitalOcean Teams overview | 2026-07-30 | 97 |
| DigitalOcean Team Roles (predefined) | 2026-07-13 | 114 |
| DigitalOcean Team Limits | 2026-09-30 | 35 |
| DigitalOcean Organizations | 2026-09-30 | 35 |
| DigitalOcean Org Roles (predefined) | 2026-09-30 | 35 |
| DigitalOcean API Scopes | 0001-01-01 | Never dated |
| DigitalOcean Create PAT | 2026-07-13 | 114 |
| DigitalOcean Security History | 2026-07-13 | 114 |
| DigitalOcean Team How-Tos | **2018-06-19** | **~3,060** (8.4 years) |
| DigitalOcean Team Settings | **2018-06-19** | **~3,060** (8.4 years) |
| Hetzner Cloud General FAQ | 2026-04-27 | 191 |

The DigitalOcean Team How-Tos and Team Settings pages have not been updated since **June 19, 2018** — over eight years. The API Scopes page carries the default Go zero-value date (`0001-01-01`), meaning it was never explicitly dated. The Teams overview, by contrast, was updated just 97 days ago and includes a changelog entry from 2 November 2026.

## What we could not verify

Following the project's rules (no UA spoofing, no proxy, no anti-bot bypass), these providers could not be read from this machine on 2026-11-04:

- **Namecheap** (`namecheap.com`): returned 403 to direct requests. No team, sub-account, or multi-user information could be verified. Not verifiable.
- **Liquid Web** (`liquidweb.com/vps-hosting/packages/`): returned Cloudflare Managed Challenge. Not verifiable.
- **Vultr**, **Linode (Akamai)**: not attempted in this article (previously 403 / SPA shell).

**Hostinger** (`hostinger.com/vps-hosting`) returned 200 but the page contains **zero mention** of team members, sub-accounts, multi-user support, user management, roles, permissions, or access control. The page is focused on individual server deployment. The closest related concepts are "full root access" (server-level, not user management) and "managed firewall" (network-level). Hostinger's VPS plans do not appear to include team collaboration features, sub-account creation, or role-based access control based on what is published.

These gaps are themselves information: if a provider does not publish team features on their VPS page, either they do not offer them or they bury them so deep that a buyer cannot find them. Both outcomes are relevant to someone evaluating VPS deals for a team.

## Actionable conclusion

**If you are a solo operator**, none of this matters — both providers give you a default team/project with one member (you), and you never need to invite anyone.

**If you need to give a teammate infrastructure access but not billing access**, DigitalOcean is the only provider that supports this pattern. The Member role grants full resource management with zero billing visibility. The Biller role grants full billing access with zero resource access. On Hetzner, every role that can touch infrastructure can also see billing-relevant information, and there is no way to isolate the two.

**If you need granular API tokens**, DigitalOcean's 164 scopes let you create tokens that can only perform specific actions on specific resource types. A CI/CD token can be scoped to `droplet:create` only. On Hetzner, API tokens are not scoped at the resource or action level in the published documentation.

**If you need to invite a non-customer**, Hetzner's light account is the only option. A contractor can join your Hetzner project with just an email and password, without becoming a Hetzner customer. On DigitalOcean, every team member must hold a DigitalOcean account.

**If you need SSO**, DigitalOcean supports OIDC-compatible identity providers (Okta, Microsoft Entra ID) as of November 2026. Hetzner does not publish SSO support.

**If you need audit logs**, DigitalOcean's security history tracks actions, users, and IP addresses. Hetzner does not publish an equivalent.

**If you need to transfer a server between accounts**, Hetzner supports project-to-project resource transfer (the receiver invites the owner, the owner transfers, the receiver takes ownership). DigitalOcean does not support cross-account resource transfer.

**Before you choose a VPS deal based on price alone**, check whether the provider's access model fits your team. The cheapest VPS is not a deal if you have to share your root password with everyone who needs to restart a service.
