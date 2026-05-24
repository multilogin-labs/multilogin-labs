# Security Policy

## Reporting vulnerabilities

If you find a security issue in **this repository's scripts or docs**, please open a private report via GitHub Security Advisories or email the maintainer — do not open public issues for exploit details.

## Secrets

- Never commit `.env`, API tokens, or profile UUIDs.
- Rotate `MULTILOGIN_TOKEN` if exposed.
- Use workspace 2FA on your Multilogin account.

## Script safety

Scripts in `scripts/` connect to **your local Multilogin launcher** only. Review code before running. This repo does not distribute malware or credential stealers.

## Affiliate transparency

This project contains partner links to Multilogin. No extra cost to you. See README disclaimer.

## Multilogin platform security

For product security questions, contact Multilogin support: support@multilogin.com
