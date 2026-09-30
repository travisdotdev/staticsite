# ❄️ NixOS Dotfiles

![Desktop](/images/nixos-desktop.jpg)

_Nix · Home Manager · Hyprland · Lua_

A declarative NixOS configuration for a Hyprland desktop, managed with flakes and Home Manager. Built from scratch rather than forked, and kept deliberately minimal with a terminal-focused workflow.

[View on GitHub](https://github.com/travisdotdev/nixos-dotfiles)

## What's in it

- **Compositor** — Hyprland (with XWayland)
- **Bar** — Waybar
- **Terminal** — foot
- **Launcher** — fuzzel
- **Editor** — Neovim
- **File manager** — yazi
- **Display manager** — SDDM (Wayland, Catppuccin Mocha)
- **Lock / idle** — hyprlock and hypridle
- **Audio** — PipeWire with ALSA and PulseAudio compatibility

## Structure

The system is split between Nix and native config files. Anything Nix can express declaratively lives in `home.nix`, while programs with their own config languages keep their native files under `config/`.

```
nixos-dotfiles/
├── flake.nix                   # inputs and the system definition
├── configuration.nix           # system-level config
├── hardware-configuration.nix  # generated, machine-specific
├── home.nix                    # user environment via Home Manager
└── config/                     # symlinked into ~/.config
    ├── hypr/
    ├── nvim/
    ├── waybar/
    ├── foot/
    └── fuzzel/
```

## Editing without rebuilding

Normally Home Manager copies config files into the read-only Nix store, so every tweak to a Lua or INI file means a full rebuild. Instead, `config/` is linked into `~/.config` with out of store symlinks that point straight at the working tree:

```
create_symlink = path: config.lib.file.mkOutOfStoreSymlink path;
xdg.configFile = builtins.mapAttrs (name: subpath: {
  source = create_symlink "${dotfiles}/${subpath}";
  recursive = true;
}) configs;
```

Edits take effect immediately while everything stays under version control. The trade off is that these files aren't part of a system generation, so a rollback won't undo them. Git covers that instead.

## Fixing Bluetooth audio

By default PipeWire lets the laptop act as a Bluetooth speaker, so headsets connected as an audio source instead of an output and produced no sound. Restricting the Bluetooth roles in WirePlumber fixes it, at the cost of the laptop no longer working as a speaker for a phone:

```
wireplumber.extraConfig."51-bluez-roles" = {
  "monitor.bluez.properties" = {
    "bluez5.roles" = [ "a2dp_source" "hsp_ag" "hfp_ag" ];
  };
};
```

## Housekeeping

- One command rebuilds the whole system, aliased to `rebuild`
- Garbage collection runs weekly with 30-day retention
- Store optimisation is automatic, so nothing needs cleaning by hand

> Not intended as a drop-in config the hardware file and username are specific to this machine. It's more useful as a reference for how the pieces fit together.

[← Projects](/projects)
