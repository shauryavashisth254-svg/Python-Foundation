# M6 Mini-Project: Data Deduplication using Sets
# Architecture: Utilizing Sets to filter noisy, corrupted data feeds.

def clean_sensor_data(raw_data: list) -> list:
    """Removes duplicate readings from a noisy sensor feed and returns a clean, sorted list."""

    # The Filter: Convert to Set (destroys duplicates), then back to List
    clean_data = list(set(raw_data))

    # Sort it so the final output is organized
    clean_data.sort()

    return clean_data


# TESTING DASHBOARD
# Simulating a glitchy temperature sensor that recorded the same values multiple times
noisy_feed = [72, 72, 73, 74, 74, 74, 75, 72, 71, 71]

scrubbed_feed = clean_sensor_data(noisy_feed)

print("--- DIAGNOSTICS ---")
print(f"Raw Input ({len(noisy_feed)} readings): {noisy_feed}")
print(f"Clean Output ({len(scrubbed_feed)} readings): {scrubbed_feed}")
