def setup_toggle():
    polarity = False
    def toggle():
        nonlocal polarity
        polarity = not polarity
        return polarity
    return toggle