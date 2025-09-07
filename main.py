from startup import voice_unlock

if __name__ == "__main__":
    access = voice_unlock()

    if access:
        print("✅ Access Granted! Now Jarvis is ready for your commands...")
        # Yaha se baaki features add karenge (YouTube, Music, etc.)
    else:
        print("❌ Access Denied! Jarvis locked.")
