# AGENTS.md

## Architecture & Module Boundaries

This repository is organized into a modular architecture to support diverse image processing and computer vision domains:

- **`image_processing.core`**:
  - `core.io`: Centralized image loading and format-aware saving (e.g., handling alpha channels for JPEG, multi-size icon exports for ICO).
- **`image_processing.fields`**:
  - Domain-specific tool collections categorized by field:
    - `fields.image_processing`: General image operations (e.g., `tools.transparency`).
    - `fields.computer_vision`: Placeholder for future computer vision features (e.g., classification, detection).
- **`image_processing.cli`**:
  - Unified command router implementing the `<field> <tool_name> [options]` command pattern.

## Build and Run Pipeline

- **Packaging**: Managed via `pyproject.toml` with `uv_build` backend.
- **Project Name**: `image-processing`
- **CLI Entrypoint**: `image-processing = "image_processing.cli:main"`
- **Execution**:
  - Via script: `python main.py <field> <tool_name> [args]`
  - Via installed binary / uv: `uv run image-processing <field> <tool_name> [args]`
