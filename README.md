# public-hosting

> Publicly-served static brand assets.

## What's here

`logos-and-icons/` — PNG and SVG logo, icon and favicon variants (light-ink,
dark-ink, transparent, several sizes). That is the entire repo: no
`package.json`, no build, no tests, no application code.

## Before you add anything

Anything committed here is **visible on github.com to anyone**. Never add
configuration, environment files, service documentation, internal architecture
notes, or anything referencing internal hostnames or schema names. Assets only.

A shared internal document belongs in `project/`, which is private.

## Branching

Same as every other repo — see `project/PLATFORM.md`. Note this repo currently
has no `develop` branch on the remote; changes go to `main`.
