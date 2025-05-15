def explain_state(state: str) -> str:
    if "VIBRATION" in state:
        return "Thiết bị đang rung mạnh bất thường."
    elif "TIPPING" in state:
        return "Thiết bị bị nghiêng quá giới hạn an toàn."
    elif "STABLE" in state:
        return "Thiết bị hoạt động ổn định."
    else:
        return "Không rõ trạng thái thiết bị."
