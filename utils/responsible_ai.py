# Responsible AI utilities: content filtering, privacy, transparency

def filter_inappropriate_content(text):
    """Simple content filter example. Returns True if content is appropriate."""
    banned_words = ['badword1', 'badword2']
    for word in banned_words:
        if word in text.lower():
            return False
    return True

def get_privacy_notice():
    """Returns a privacy notice string."""
    return (
        "Your data is processed securely and only used to provide AI assistant responses. "
        "No personal information is stored."
    )

def log_transparency(event, details=None):
    """Logs actions for transparency (stub)."""
    print(f"[TRANSPARENCY LOG] Event: {event}, Details: {details}")
