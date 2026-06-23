# M6: Hardware State & Security Auditing
# Architecture: Sets (Math) and Frozensets (Immutability)


print("--- 1. FIRMWARE AUDIT (SET MATH) ---")
base_firmware = {"bootloader", "kernel", "radio_driver", "i2c_bus"}
scanned_modules = {"i2c_bus", "kernel", "spyware_node", "bootloader"}

# Identify rogue code using Difference (-)
rogue_code = scanned_modules - base_firmware
print(f"SECURITY ALERT: Rogue modules detected: {rogue_code}")

# Identify common modules using Intersection (&)
verified_modules = scanned_modules & base_firmware
print(f"Verified base modules: {verified_modules}\n")


print("--- 2. SECURE CONFIGURATION (FROZENSET HOT SWAP) ---")
# Locked hardware configuration (Immutable)
locked_config = frozenset({"pin_2", "pin_4", "pin_8"})
new_pin = "pin_10"
print(f"Initial locked state: {locked_config}")

# The Hot Swap Protocol
temp_config = set(locked_config)   # 1. Unfreeze to mutable set
temp_config.add(new_pin)           # 2. Mutate (Action only, no assignment to avoid NoneType)
updated_config = frozenset(temp_config) # 3. Refreeze to lock it down

print(f"Updated locked state: {updated_config}")
