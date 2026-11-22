import requests

proxies_list = [
"http://agaulicr:gkgjy6rwczp0@31.59.20.176:6754",

]

live_proxies = []

for u in proxies_list:
    ip = u.split("@")[-1].split(":")[0]
    proxy_url = u if u.startswith("http") else f"http://{u}"
    proxy_dict = {"http": proxy_url, "https": proxy_url}
    try:
        res = requests.get("https://api.ipify.org", proxies=proxy_dict, timeout=10)
        r = res.text.strip()
        if res.status_code == 200 and r and not r.startswith("<") and "Bandwidth limit reached" not in r:
            try:
                geo_res = requests.get(f"https://ipinfo.io/{r}/json", timeout=5).json()
                geo = f"{geo_res.get('country', '?')} {geo_res.get('city', '?')}"
            except Exception:
                geo = "? ?"
            print(f"HIDUP: {ip} -> keluar {r} ({geo})")
            live_proxies.append({"proxy": u, "ip": ip, "out_ip": r, "geo": geo})
        else:
            print(f"LIMIT: {ip} -> kuota habis / respons invalid")
    except Exception as e:
        print(f"LIMIT: {ip} -> kuota habis / error")

print("\n" + "=" * 50)
print(f"SUMMARY: {len(live_proxies)} / {len(proxies_list)} HIDUP")
print("=" * 50)
for p in live_proxies:
    print(f"{p['proxy']} -> {p['out_ip']} ({p['geo']})")
