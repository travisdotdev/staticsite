# 🌱 WattPrint — HackEurope

![LandingPage](/images/wattprintdashboard.png)
_React · Node.js · Stripe · AWS Lambda · Supabase_

A carbon emissions tracking platform built at HackEurope. Tracks device energy usage, processes carbon offset purchases via Stripe Climate, and visualises everything through a React dashboard.

[View on GitHub](https://github.com/travisdotdev/WattPrint-HackEurope)

## What it does

- Fetches live Stripe Climate pricing per metric ton of carbon
- Runs Stripe Checkout in test mode and tracks paid emissions via webhook
- Automatically creates a Stripe Climate order when 5 tons are accumulated
- Renders a React dashboard with summary cards, charts, breakdowns, exports, and receipts
- Ingests device energy metrics (JSON/JSONL) into Supabase Postgres via an AWS Lambda handler
- Includes a silent Windows client that reports hourly device energy usage automatically

## Architecture

The project has three main components:

**Backend (Node.js)** — handles Stripe webhooks, accumulates emission totals, and exposes dashboard APIs.

**React Dashboard** — visualises energy data with filtering by team, service, user, device, and region. Pulls live data from Supabase if configured, otherwise falls back to mock data.

**AWS Lambda** — a serverless metrics ingestion handler that accepts JSON or JSONL payloads and writes to a Supabase Postgres table.

## Windows Client

A lightweight background agent that silently collects laptop battery drain and grid zone data, reporting hourly to the dashboard.

[← Projects](/projects)
