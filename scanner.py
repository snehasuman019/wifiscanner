import pywifi
import time

def scan_wifi():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    print("🔍 Scanning nearby WiFi networks...\n")
    iface.scan()
    time.sleep(3)

    results = iface.scan_results()

    if not results:
        print("❌ No WiFi networks found")
        return

    print("📡 Available WiFi Networks:\n")
    for i, net in enumerate(results, start=1):
        ssid = net.ssid if net.ssid else "Hidden Network"
        print(f"{i}. SSID: {ssid} | Signal Strength: {net.signal}")

if __name__ == "__main__":
    print("===== WiFi Scanner v1 =====\n")
    scan_wifi()
