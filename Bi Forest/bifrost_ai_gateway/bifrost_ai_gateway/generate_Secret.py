import re
import secrets
from pathlib import Path


def main() -> None:
    env_path = Path(__file__).resolve().with_name(".env")
    example_path = env_path.with_name(".env.example")
    if not env_path.is_file():
        raise FileNotFoundError(f".env file not found: {env_path}")
    if not example_path.is_file():
        raise FileNotFoundError(f".env.example file not found: {example_path}")

    with env_path.open("r", encoding="utf-8", newline="") as env_file:
        content = env_file.read()
    with example_path.open("r", encoding="utf-8") as example_file:
        example_content = example_file.read()

    entry_pattern = re.compile(
        r"^([ \t]*)([A-Za-z_][A-Za-z0-9_]*)([ \t]*=[ \t]*)(.*)$"
    )
    expected_keys = {
        match.group(1)
        for line in example_content.splitlines()
        if (match := entry_pattern.match(line))
    }

    lines = []
    existing_values = {}
    existing_lines = {}
    existing_keys = set()
    changed = False
    for line in content.splitlines(keepends=True):
        if line.endswith("\r\n"):
            body = line[:-2]
        elif line.endswith(("\n", "\r")):
            body = line[:-1]
        else:
            body = line
        lines.append(line)
        key_match = entry_pattern.match(body)
        if key_match:
            key = key_match.group(2)
            if key in existing_keys:
                raise ValueError(f"Duplicate {key} entries found in {env_path}.")
            existing_keys.add(key)
            value = key_match.group(4).strip().strip("\"'")
            existing_values[key] = value
            existing_lines[key] = (len(lines) - 1, key_match, line)

    missing_keys = expected_keys - existing_keys
    secret_keys = {
        key
        for key in expected_keys | existing_keys
        if key.endswith("_KEY") or key.endswith("_TOKEN")
    }
    empty_keys = sorted(
        key for key in secret_keys if not existing_values.get(key, "").strip()
    )
    if missing_keys or empty_keys:
        newline = "\r\n" if "\r\n" in content else "\n"
        if lines and not lines[-1].endswith(("\n", "\r")):
            lines[-1] += newline
        for key in empty_keys:
            secret = secrets.token_urlsafe(32)
            if key in existing_lines:
                index, match, original_line = existing_lines[key]
                line_ending = original_line[len(original_line.rstrip("\r\n")) :]
                lines[index] = (
                    f"{match.group(1)}{key}{match.group(3)}{secret}{line_ending}"
                )
            else:
                lines.append(f"{key}={secret}{newline}")
            changed = True
        for key in sorted(missing_keys):
            value = secrets.token_urlsafe(32) if key in secret_keys else ""
            lines.append(f"{key}={value}{newline}")
            changed = True
        if changed:
            with env_path.open("w", encoding="utf-8", newline="") as env_file:
                env_file.write("".join(lines))
        if missing_keys or empty_keys:
            print(f"Generated secrets for empty or missing key/token entries in {env_path}.")
            print(
                "BIFROST_SETUP_TOKEN is a generated local setup secret. Random "
                "*_KEY placeholders are not provider credentials or valid "
                "Bifrost virtual keys; replace them before making API calls."
            )
    else:
        print(f"All entries from .env.example already exist and are non-empty in {env_path}.")

    unconfigured = sorted(
        key for key in expected_keys - secret_keys
        if not existing_values.get(key, "").strip()
    )
    if unconfigured:
        print("These keys still need valid values: " + ", ".join(unconfigured))
        print("Add credentials issued by the corresponding provider or Bifrost.")


if __name__ == "__main__":
    main()
