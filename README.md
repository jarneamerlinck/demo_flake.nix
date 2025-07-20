# Demo for a nix flake python project

This project is based on uv2nix.

Before we can build for nix we should lock uv

```bash
uv lock
```

now you can build for nix

```bash
nix build
```


```bash
nix build .#
```
