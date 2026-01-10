import os

"""EXAMPLE Configuration - Change values and save as config.py"""

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, ".."))

ADMIN_PASSWORD = "YOUR_SECRET_PHRASE_HERE"
NUMBER_OF_ATTEMPTS = 5

REQUIRED_AVG_SPEED = 0.2
ALLOW_PASTE = False

PRANK_MODE_ACTIVATED = True
CAPTURE_INTERVAL = 15

LOG_FILE = os.path.join(PROJECT_ROOT, "vault", "logs", "security_audit.log")
CAPTURES_DIR = os.path.join(PROJECT_ROOT, "vault", "captures")
GO_AGENT_EXE = os.path.join(PROJECT_ROOT, "core", "agent_go", "watcher.exe")
FAKE_DB = os.path.join(PROJECT_ROOT, "vault", "fake_secrets.json")

VOICE_RATE = 150
VOICE_VOLUME = 1.0

GREETING_MSG = "Welcome message here"
ALARM_MSG = "Breach message here"