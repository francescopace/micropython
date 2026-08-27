# Test the ESP32 WLAN CSI control API without requiring an access point or traffic.
try:
    import network
except ImportError:
    print("SKIP")
    raise SystemExit

wlan = network.WLAN(network.WLAN.IF_STA)
if not hasattr(wlan, "csi_enable"):
    print("SKIP")
    raise SystemExit


def check_value_error(name, **kwargs):
    try:
        wlan.csi_enable(**kwargs)
    except ValueError:
        print(name, "ValueError")
    else:
        print(name, "FAIL")
        wlan.csi_disable()


wlan.csi_disable()
print("initial", wlan.csi_available(), wlan.csi_dropped(), wlan.csi_callbacks())

check_value_error("buffer_size=0", buffer_size=0)
check_value_error("buffer_size=65535", buffer_size=65535, max_data_len=1)
check_value_error("max_data_len=0", max_data_len=0)
check_value_error("max_data_len=513", max_data_len=513)

wlan.active(True)
wlan.csi_enable(buffer_size=1, max_data_len=1)
print("enabled", wlan.csi_available() >= 0, wlan.csi_dropped() >= 0, wlan.csi_callbacks() >= 0)
wlan.csi_disable()
print("disabled", wlan.csi_available(), wlan.csi_dropped(), wlan.csi_callbacks())
wlan.csi_disable()
print("idempotent")
wlan.active(False)
