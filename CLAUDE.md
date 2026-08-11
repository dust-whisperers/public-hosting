# public-hosting — notes for Claude

Publicly-served static brand assets. **This is the only public repo in the
`dust-whisperers` org.**

## What's here

`logos-and-icons/` — PNG and SVG logo/icon/favicon variants (light-ink, dark-ink,
transparent, multiple sizes). That is the entire repo. There is no `package.json`, no
build, no tests, and no application code.

## Before you add anything

This repo is **public**. Anything committed here is visible on github.com to anyone.
Never add configuration, environment files, service documentation, internal
architecture notes, or anything referencing internal hostnames or schema names.
Assets only.

If you need somewhere to put a shared internal document, it belongs in `project/`,
which is private.

## Branching

`develop` is the integration branch. Branch from it, PR into it. Never target `main`
directly.
