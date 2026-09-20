import time
import pyautogui

# ============================================================
# SETTINGS
# ============================================================

FIRST_WAIT_HOURS = 3
FIRST_WAIT_MINUTES = 30

SUBSEQUENT_WAIT_HOURS = 5
SUBSEQUENT_WAIT_MINUTES = 30

LOOP_COUNT = 2

FIRST_TEXT_TO_TYPE = "Awesome! start adding the categories and their bricks please using the agent"
TEXT_TO_TYPE = "Keep going!"

CLICK_X = 2890
CLICK_Y = 2012

# Delay between each typed character, in seconds.
# Higher = slower typing.
TYPE_INTERVAL = 0.15

# ============================================================
# SCRIPT
# ============================================================

# PyAutoGUI safety feature:
# Move the mouse to the top-left corner of the screen
# to immediately stop the script.
pyautogui.FAILSAFE = True

first_wait_seconds = (FIRST_WAIT_HOURS * 60 * 60) + (FIRST_WAIT_MINUTES * 60)
subsequent_wait_seconds = (SUBSEQUENT_WAIT_HOURS * 60 * 60) + (SUBSEQUENT_WAIT_MINUTES * 60)

print(f"First wait time: {FIRST_WAIT_HOURS} hours, {FIRST_WAIT_MINUTES} minutes")
print(f"Later wait time: {SUBSEQUENT_WAIT_HOURS} hours, {SUBSEQUENT_WAIT_MINUTES} minutes")
print(f"Number of loops: {LOOP_COUNT}")
print("Move the mouse to the TOP-LEFT corner to emergency-stop.")
print()

for loop_number in range(1, LOOP_COUNT + 1):
    if loop_number == 1:
        wait_hours = FIRST_WAIT_HOURS
        wait_minutes = FIRST_WAIT_MINUTES
        wait_seconds = first_wait_seconds
    else:
        wait_hours = SUBSEQUENT_WAIT_HOURS
        wait_minutes = SUBSEQUENT_WAIT_MINUTES
        wait_seconds = subsequent_wait_seconds

    print(f"Loop {loop_number}/{LOOP_COUNT}")
    print(f"Waiting {wait_hours}h {wait_minutes}m...")

    time.sleep(wait_seconds)

    print("Clicking...")
    pyautogui.click(CLICK_X, CLICK_Y)

    time.sleep(2)

    print("Typing...")
    if loop_number == 1:
        pyautogui.write(FIRST_TEXT_TO_TYPE, interval=TYPE_INTERVAL)
    else:
        pyautogui.write(TEXT_TO_TYPE, interval=TYPE_INTERVAL)

    time.sleep(2)

    print("Pressing Enter...")
    pyautogui.press("enter")

    print(f"Loop {loop_number} complete.")
    print()

print("All loops complete.")